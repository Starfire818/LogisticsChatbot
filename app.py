"""
File: app.py
Description: Streamlit based Graphical User Interface (GUI) wrapper 
             offering an elegant interactive chat platform for user presentation.
"""

import streamlit as st
from chatbot import LogisticsChatbot

# Page Layout configurations
st.set_page_config(page_title="Logistics AI Agent", page_icon="📦", layout="centered")

st.title("📦 Logistics Customer Support System")
st.markdown("### Intelligent NLP Intent Recognition Prototype")
st.write("Ask queries regarding tracking, shipping addresses, refunds, account setup, etc.")
st.write("---")

# Resource Caching for optimized loading performance
@st.cache_resource
def initialize_system_backend():
    return LogisticsChatbot(confidence_threshold=0.35)

try:
    chatbot_instance = initialize_system_backend()
except Exception as e:
    st.error(f"❌ Failed to load the AI core pipeline. Details: {e}")
    st.info("💡 Advice: Ensure you have successfully populated data files and run `train_model.py` to compile the artifacts.")
    st.stop()

# State management for preserving chat logs between rerenders
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Display past messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        if message["role"] == "assistant" and "metadata" in message:
            st.caption(f"⚙️ [Intent: **{message['metadata']['intent']}** | Confidence: **{message['metadata']['conf']:.2%}**]")

# Capture dynamic user input
if prompt := st.chat_input("Enter your inquiries here (e.g., 'How do I track my delivery?')"):
    
    # Render user prompt
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.chat_history.append({"role": "user", "content": prompt})
    
    # Fetch response data from backend inference engine
    bot_reply, matched_intent, conf_score = chatbot_instance.get_bot_response(prompt)
    
    # Render system response
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
        st.caption(f"⚙️ [Intent: **{matched_intent}** | Confidence: **{conf_score:.2%}**]")
        
    # Append structured history elements
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": bot_reply,
        "metadata": {"intent": matched_intent, "conf": conf_score}
    })