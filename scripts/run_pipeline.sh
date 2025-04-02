#!/bin/bash

echo "🚀 Installing Dependencies..."
pip install --no-cache-dir -r requirements.txt
python -m spacy download en_core_web_sm


echo "📊 Training sentiment model..."
python model/model.py

echo "🚀 Starting Flask Web App..."
python src/app.py
