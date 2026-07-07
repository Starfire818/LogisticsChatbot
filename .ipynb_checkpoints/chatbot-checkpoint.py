"""
File: chatbot.py
Description: The core backend logical engine for parsing user inputs, 
             predicting intents, handling low-confidence fallbacks, and mapping 
             responses from JSON structure.
"""

import os
import json
import random
import pickle
import numpy as np

class LogisticsChatbot:
    def __init__(self, confidence_threshold=0.35):
        self.threshold = confidence_threshold
        self.vectorizer_path = 'model/vectorizer.pkl'
        self.model_path = 'model/chatbot_model.pkl'
        self.intents_json_path = 'data/intents.json'
        
        # Core assets holders
        self.vectorizer = None
        self.model = None
        self.responses = {}
        
        # Bootstrap initialization
        self.load_artifacts()

    def load_artifacts(self):
        # Exception Handling: Validate model files existence
        if not os.path.exists(self.vectorizer_path) or not os.path.exists(self.model_path):
            raise FileNotFoundError("Trained model files are missing. Please run train_model.py first.")
            
        if not os.path.exists(self.intents_json_path):
            raise FileNotFoundError(f"Configuration file missing at {self.intents_json_path}")
            
        # Load binary pkl objects
        with open(self.vectorizer_path, 'rb') as f:
            self.vectorizer = pickle.load(f)
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
            
        # Hotfix for scikit-learn compatibility: ensure multi_class attribute exists
        #if not hasattr(self.model, 'multi_class'):
        #   self.model.multi_class = 'ovr'
            
        # Load intent configuration mapping
        with open(self.intents_json_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
            self.responses = config_data.get("responses", {})

    def get_bot_response(self, user_message):
        if not user_message.strip():
            return "Please say something, I am listening.", "empty_input", 1.0
            
        # Vectorize text input
        transformed_text = self.vectorizer.transform([user_message])
        
        # Model Prediction and probability extraction
        predicted_intent = self.model.predict(transformed_text)[0]
        probabilities = self.model.predict_proba(transformed_text)
        max_confidence = np.max(probabilities)
        
        # Validation Rule: Handling Out-of-Domain or low-confidence inputs
        if max_confidence < self.threshold:
            fallback_reply = random.choice(self.responses.get("default", ["I cannot understand your request clearly."]))
            return fallback_reply, "unknown_fallback", max_confidence
            
        # Response Mapping
        if predicted_intent in self.responses:
            reply = random.choice(self.responses[predicted_intent])
        else:
            reply = f"Intent [{predicted_intent}] detected, but no matching response configured in data/intents.json."
            
        return reply, predicted_intent, max_confidence