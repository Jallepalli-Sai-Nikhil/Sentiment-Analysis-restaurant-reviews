from flask import Flask, render_template, request
import joblib
import spacy
import yaml
from sklearn.feature_extraction.text import CountVectorizer

# Load configuration
with open("utils/config.yml", "r") as file:
    config = yaml.safe_load(file)
    
MODEL_PATH = config["model_path"]
VECTORIZER_PATH = config["vectorizer_path"]  # Load vectorizer path from config

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

# Load trained model and vectorizer
model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)

def preprocess_text(text):
    """Cleans and tokenizes text using spaCy."""
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Initialize Flask app
app = Flask(__name__, template_folder="../templates")

@app.route("/", methods=["GET", "POST"])
def index():
    sentiment = None
    user_text = ""
    
    if request.method == "POST":
        user_text = request.form["review"]
        processed_text = preprocess_text(user_text)
        prediction = model.predict(vectorizer.transform([processed_text]))[0]  # Remove .toarray()
        sentiment = "Positive 😊" if prediction == 1 else "Negative 😞"
        
    return render_template("index.html", sentiment=sentiment, user_text=user_text)
    
if __name__ == "__main__":
    app.run(debug=True)
