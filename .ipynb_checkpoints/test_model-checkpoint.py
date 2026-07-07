"""
File: test_model.py
Description: Command Line Interface (CLI) testing utility script to verify 
             the correctness of chatbot response logic interactively.
"""

from chatbot import LogisticsChatbot

def run_cli_test_session():
    print("============================================================")
    print("Initializing Logistics Support Chatbot CLI test harness...")
    print("============================================================")
    
    try:
        # Initialize chatbot instance
        bot = LogisticsChatbot(confidence_threshold=0.35)
        print("[STATUS] Chatbot loaded successfully. Type 'exit' or 'quit' to close.")
        print("-" * 60)
        
        while True:
            user_input = input("You: ")
            if user_input.lower() in ['exit', 'quit']:
                print("🤖 Session ended by user. Goodbye!")
                break
                
            if user_input.strip() == "":
                continue
                
            response, intent, score = bot.get_bot_response(user_input)
            print(f"Bot: {response}")
            print(f"📊 [Metadata] -> Intent: {intent} | Confidence: {score:.2%}")
            print("-" * 60)
            
    except Exception as e:
        print(f"[FATAL CRASH] Error initializing chatbot execution pipeline: {e}")

if __name__ == "__main__":
    run_cli_test_session()