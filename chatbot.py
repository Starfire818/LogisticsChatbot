"""
File: chatbot.py
Description: The core backend logical engine for parsing user inputs, 
             predicting intents, handling low-confidence fallbacks, and mapping 
             responses from JSON structure. (Enhanced with Regex DB Lookup)
"""

import os
import json
import random
import pickle
import re  # Imported for regex tracking ID validation
import numpy as np

class LogisticsChatbot:
    def __init__(self, confidence_threshold=0.10): # Defaults to 0.10 to match your current app.py settings
        self.threshold = confidence_threshold
        self.vectorizer_path = 'model/vectorizer.pkl'
        self.model_path = 'model/chatbot_model.pkl'
        self.intents_json_path = 'data/intents.json'
        self.db_json_path = 'data/logistics_db.json' # Registered path for the mock database
        
        # Core assets holders
        self.vectorizer = None
        self.model = None
        self.responses = {}
        self.mock_db = {} # Holder for package tracking database
        
        # Bootstrap initialization
        self.load_artifacts()

    def load_artifacts(self):
        # Exception Handling: Validate model and config files existence
        if not os.path.exists(self.vectorizer_path) or not os.path.exists(self.model_path):
            raise FileNotFoundError("Trained model files are missing. Please run train_model.py first.")
            
        if not os.path.exists(self.intents_json_path):
            raise FileNotFoundError(f"Configuration file missing at {self.intents_json_path}")
            
        if not os.path.exists(self.db_json_path):
            raise FileNotFoundError(f"Database registry file missing at {self.db_json_path}")
            
        # Load binary pkl objects
        with open(self.vectorizer_path, 'rb') as f:
            self.vectorizer = pickle.load(f)
        with open(self.model_path, 'rb') as f:
            self.model = pickle.load(f)
            
        # Load intent configuration mapping
        with open(self.intents_json_path, 'r', encoding='utf-8') as f:
            config_data = json.load(f)
            self.responses = config_data.get("responses", {})

        # Load simulated logistics database records
        with open(self.db_json_path, 'r', encoding='utf-8') as f:
            db_data = json.load(f)
            self.mock_db = db_data.get("mock_database", {}).get("orders", {})

    def get_bot_response(self, user_message):
        cleaned_message = user_message.strip()
        if not cleaned_message:
            return "Please say something, I am listening.", "empty_input", 1.0
            
        # ====================================================================
        # BUSINESS RULE VALIDATION: REGEX TRACKING ID DETECTION
        # ====================================================================
        # Scans user text for patterns like TRK1001 or trk1002 (Case-Insensitive)
        tracking_match = re.search(r'\b(TRK\d{4})\b', cleaned_message, re.IGNORECASE)
        
        if tracking_match:
            tracking_id = tracking_match.group(1).upper()
            
            # Cross-reference tracking ID with our mock JSON database
            if tracking_id in self.mock_db:
                order_info = self.mock_db[tracking_id]
                reply = (f"🔍 **System Database Registry Found!**\n\n"
                         f"📦 **Tracking ID:** {tracking_id}\n"
                         f"📍 **Current Status:** {order_info['status']}\n"
                         f"🗺️ **Destination:** {order_info['destination']}\n"
                         f"📅 **Estimated Arrival (ETA):** {order_info['eta']}")
                return reply, "database_tracking_lookup", 1.0
            else:
                reply = f"❌ **Tracking ID '{tracking_id}' format detected, but no records exist in our database.**"
                return reply, "database_tracking_failed", 1.0
        # ====================================================================
        
        # Vectorize text input if no tracking ID was present
        transformed_text = self.vectorizer.transform([cleaned_message])
        
        # Model Prediction and probability extraction
        predicted_intent = self.model.predict(transformed_text)[0]

        # Robust confidence extraction: some environments / pickled models
        # may not support `predict_proba` (or may raise AttributeError
        # due to sklearn version mismatches). Try `predict_proba` first,
        # fall back to `decision_function` (converted to probabilities),
        # and finally use a safe default confidence.
        max_confidence = 1.0
        try:
            probabilities = self.model.predict_proba(transformed_text)
            # probabilities shape may be (n_samples, n_classes)
            if hasattr(probabilities, 'ndim') and probabilities.ndim > 1:
                max_confidence = float(np.max(probabilities))
            else:
                max_confidence = float(np.max(probabilities))
        except Exception:
            # predict_proba failed (possibly AttributeError on multi_class)
            try:
                if hasattr(self.model, 'decision_function'):
                    scores = self.model.decision_function(transformed_text)
                    # Convert scores to probabilities
                    if np.ndim(scores) == 1:
                        # Binary case: apply sigmoid
                        probs = 1.0 / (1.0 + np.exp(-scores))
                        probs = np.ravel(probs)
                        # take the higher of prob and 1-prob as confidence
                        max_confidence = float(max(probs.max(), 1.0 - probs.min()))
                    else:
                        # Multiclass: softmax
                        exp_scores = np.exp(scores - np.max(scores, axis=1, keepdims=True))
                        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
                        max_confidence = float(np.max(probs))
                else:
                    max_confidence = 1.0
            except Exception:
                max_confidence = 1.0
        
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