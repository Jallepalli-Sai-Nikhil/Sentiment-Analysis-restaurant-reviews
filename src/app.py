from flask import Flask, render_template, request
import joblib
import spacy
import yaml
import os
from sklearn.feature_extraction.text import CountVectorizer

# Load configuration
CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../utils/config.yml")

try:
    with open(CONFIG_PATH, "r") as file:
        config = yaml.safe_load(file)
    MODEL_PATH = config.get("model_path", "model.pkl")  # Default fallback
    VECTORIZER_PATH = config.get("vectorizer_path", "vectorizer.pkl")
except Exception as e:
    print(f"⚠️ Error loading config: {e}")
    MODEL_PATH, VECTORIZER_PATH = "model.pkl", "vectorizer.pkl"

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except Exception as e:
    print(f"⚠️ Error loading spaCy model: {e}")
    nlp = None  # Prevent crashes

# Load trained model & vectorizer
try:
    model = joblib.load(MODEL_PATH)
    vectorizer = joblib.load(VECTORIZER_PATH)
except Exception as e:
    print(f"⚠️ Error loading model/vectorizer: {e}")
    model, vectorizer = None, None

def preprocess_text(text):
    """Cleans and tokenizes text using spaCy."""
    if not nlp:
        return text  # Return raw text if spaCy isn't loaded
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Initialize Flask app
app = Flask(__name__, template_folder=config["template_folder"])

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    user_text = ""

    if request.method == "POST":
        user_text = request.form.get("review", "").strip()
        
        if user_text and model and vectorizer:
            processed_text = preprocess_text(user_text)
            prediction = model.predict(vectorizer.transform([processed_text]))[0]
            sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"
        else:
            sentiment = "⚠️ Error: Missing model, vectorizer, or input."

    return render_template("index.html", sentiment=sentiment, user_text=user_text)

if __name__ == "__main__":
    app.run(debug=True)
