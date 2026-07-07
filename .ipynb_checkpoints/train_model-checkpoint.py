"""
File: train_model.py
Description: Loads the logistics dataset, performs TF-IDF feature extraction,
             trains a Logistic Regression classifier, evaluates the performance,
             and exports the trained artifacts.
"""

import os
import pickle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

def train_logistics_model():
    dataset_path = 'Training-dataset-for-chatbots.csv'
    
    # Exception Handling: Check if dataset file exists
    if not os.path.exists(dataset_path):
        print(f"[ERROR] Dataset file '{dataset_path}' not found! Please check the path.")
        return

    print("--> Loading chatbot training dataset...")
    df = pd.read_csv(dataset_path)
    
    # Data Cleaning: Drop missing rows in critical columns
    df = df.dropna(subset=['utterance', 'intent'])
    
    X = df['utterance']
    y = df['intent']
    
    # Split data: 80% Training, 20% Testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"--> Dataset split complete. Train size: {len(X_train)}, Test size: {len(X_test)}")
    
    # NLP Feature Extraction: TF-IDF with Unigrams & Bigrams
    print("--> Vectorizing text using TF-IDF...")
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2), max_features=8000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train Supervised ML Classifier (Removed multi_class parameter for scikit-learn 1.5+ compatibility)
    print("--> Training Logistic Regression model (In progress)...")
    model = LogisticRegression(max_iter=600, C=1.0, solver='lbfgs')
    model.fit(X_train_tfidf, y_train)
    
    # Evaluate Model Performance (Required for Assignment Metrics)
    y_pred = model.predict(X_test_tfidf)
    print("\n=================== MODEL PERFORMANCE REPORT ===================")
    print(classification_report(y_test, y_pred))
    print(f"Overall Accuracy: {accuracy_score(y_test, y_pred):.4f}")
    print("================================================================\n")
    
    # Ensure model export directory exists
    os.makedirs('model', exist_ok=True)
    
    # Persist artifacts using pickle
    print("--> Saving Vectorizer to model/vectorizer.pkl...")
    with open('model/vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
        
    print("--> Saving Model to model/chatbot_model.pkl...")
    with open('model/chatbot_model.pkl', 'wb') as f:
        pickle.dump(model, f)
        
    print("[SUCCESS] Model training pipeline executed successfully!")

if __name__ == "__main__":
    train_logistics_model()