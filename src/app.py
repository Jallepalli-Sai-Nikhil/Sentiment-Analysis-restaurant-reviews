from flask import Flask, render_template, request
import joblib
import spacy
import yaml
import os
import logging
from sklearn.feature_extraction.text import CountVectorizer

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load configuration
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../utils/config.yml")
DEFAULT_MODEL_PATH = "../model/model.pkl"
DEFAULT_VECTORIZER_PATH = "../model/vectorizer.pkl"
DEFAULT_TEMPLATE_PATH = "../templates"

try:
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)
    
    MODEL_PATH = config.get("model_path", DEFAULT_MODEL_PATH)
    VECTORIZER_PATH = config.get("vectorizer_path", DEFAULT_VECTORIZER_PATH)
    TEMPLATE_PATH = config.get("template_folder", DEFAULT_TEMPLATE_PATH)

    logging.info("✅ Configuration loaded successfully.")
except Exception as e:
    logging.error(f"⚠️ Error loading config: {e}")
    MODEL_PATH, VECTORIZER_PATH, TEMPLATE_PATH = DEFAULT_MODEL_PATH, DEFAULT_VECTORIZER_PATH, DEFAULT_TEMPLATE_PATH

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
    logging.info("✅ spaCy model loaded successfully.")
except Exception as e:
    logging.error(f"⚠️ Error loading spaCy model: {e}")
    nlp = None  # Prevent crashes

# Load trained model & vectorizer
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
    logging.info("✅ Model and vectorizer loaded successfully.")
except Exception as e:
    logging.error(f"⚠️ Error loading model/vectorizer: {e}")
    model, vectorizer = None, None  # Prevent crashes

def preprocess_text(text):
    """Cleans and tokenizes text using spaCy."""
    if not nlp:
        logging.warning("⚠️ spaCy model not loaded. Returning raw text.")
        return text  # Return raw text if spaCy isn't loaded
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Initialize Flask app
app = Flask(__name__, template_folder=TEMPLATE_PATH)

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("review", "").strip()
        
        if user_text:
            if model and vectorizer:
                processed_text = preprocess_text(user_text)
                try:
                    prediction = model.predict(vectorizer.transform([processed_text]))[0]
                    sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"
                except Exception as e:
                    logging.error(f"⚠️ Prediction error: {e}")
                    sentiment = "⚠️ Error during prediction."
            else:
                sentiment = "⚠️ Model or vectorizer is missing."
        else:
            sentiment = "⚠️ Please enter a review."

    return render_template("index.html", sentiment=sentiment, user_text=user_text)

if __name__ == "__main__":
    app.run(debug=True)
