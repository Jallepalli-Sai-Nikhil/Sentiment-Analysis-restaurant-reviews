import pandas as pd
import spacy
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import StratifiedKFold, GridSearchCV, train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    """Cleans and tokenizes text using spaCy."""
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and not token.is_stop]
    return " ".join(tokens)

# Load dataset
df = pd.read_csv("data/dataset.tsv", delimiter='\t', quoting=3)
df['Cleaned_Review'] = df['Review'].apply(preprocess_text)
X = df['Cleaned_Review']
y = df['Liked']

# Vectorization
vectorizer = CountVectorizer(max_features=1500)
X_vectorized = vectorizer.fit_transform(X)

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42, stratify=y)

# Define base estimator
base_estimator = DecisionTreeClassifier(max_depth=1, random_state=42)

# Define AdaBoost classifier
adaboost = AdaBoostClassifier(estimator=base_estimator, random_state=42)

# Hyperparameter tuning using Stratified KFold + GridSearchCV
param_grid = {
    'n_estimators': [50, 100, 200],
    'learning_rate': [0.01, 0.1, 1.0]
}

cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
grid_search = GridSearchCV(adaboost, param_grid, cv=cv, scoring='accuracy', n_jobs=-1)
grid_search.fit(X_train, y_train)

# Best model
best_model = grid_search.best_estimator_
y_pred = best_model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Best Model Accuracy: {accuracy * 100:.2f}%")

# Save model & vectorizer
joblib.dump(best_model, "model/model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")  # Save vectorizer
