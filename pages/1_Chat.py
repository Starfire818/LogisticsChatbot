"""
File: pages/1_Chat.py
Description: ChatGPT-style chat page for interacting with LogiBot.
             Displays chat history with proper message bubbles and scrolling.
"""

import streamlit as st
from chatbot import LogisticsChatbot

# Page configuration
st.set_page_config(
    page_title="LogiBot - Smart Logistics Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
* {
  box-sizing: border-box;
}

:root {
  color-scheme: light dark;
}

/* Light Mode */
body, .stApp, .main, .block-container {
  background: #FFFFFF !important;
}

#MainMenu, footer {
  visibility: hidden;
}

/* Full-height layout */
.stApp {
  display: flex;
  flex-direction: column;
  height: 100vh;
}

.main {
  display: flex;
  flex-direction: column;
  height: 100vh;
  padding: 0 !important;
  overflow: hidden;
}

.block-container {
  padding: 0 !important;
  display: flex;
  flex-direction: column;
  height: 100vh;
}

/* Header */
.chat-header {
  flex-shrink: 0;
  background: linear-gradient(135deg, #2563EB 0%, #60A5FA 100%);
  color: white;
  padding: 16px 24px;
  display: flex;
  align-items: center;
  gap: 16px;
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.15);
}

.back-button {
  background: rgba(255, 255, 255, 0.2);
  border: none;
  color: white;
  width: 40px;
  height: 40px;
  border-radius: 8px;
  font-size: 20px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.back-button:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateX(-2px);
}

.back-button:active {
  transform: translateX(0);
}

.header-text h1 {
  margin: 0;
  font-size: 1.3rem;
  font-weight: 700;
}

.header-text p {
  margin: 2px 0 0 0;
  font-size: 0.85rem;
  opacity: 0.9;
}

/* Chat container */
.chat-container {
  flex: 1;
  display: flex;
  flex-direction: column;
  overflow: hidden;
  background: #F8FAFC;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 12px;
  scroll-behavior: smooth;
}

/* Custom scrollbar */
.chat-messages::-webkit-scrollbar {
  width: 8px;
}

.chat-messages::-webkit-scrollbar-track {
  background: transparent;
}

.chat-messages::-webkit-scrollbar-thumb {
  background: rgba(148, 163, 184, 0.3);
  border-radius: 4px;
}

.chat-messages::-webkit-scrollbar-thumb:hover {
  background: rgba(148, 163, 184, 0.5);
}

/* Empty state */
.empty-state {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  color: #94A3B8;
  text-align: center;
}

.empty-state-icon {
  font-size: 4rem;
  margin-bottom: 16px;
  opacity: 0.3;
}

.empty-state-title {
  font-size: 1.2rem;
  font-weight: 600;
  color: #475569;
  margin-bottom: 8px;
}

.empty-state-text {
  font-size: 0.95rem;
  color: #94A3B8;
}

/* Message wrapper */
.message-group {
  display: flex;
  margin: 0;
  padding: 0;
}

.message-group.user {
  justify-content: flex-end;
}

.message-group.assistant {
  justify-content: flex-start;
}

/* Message bubble */
.message-bubble {
  max-width: 65%;
  word-wrap: break-word;
  line-height: 1.5;
  font-size: 0.95rem;
  padding: 12px 16px;
  border-radius: 16px;
  animation: slideIn 0.3s ease-out;
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(8px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.message-bubble.user {
  background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
  color: white;
  border-bottom-right-radius: 4px;
  box-shadow: 0 2px 8px rgba(37, 99, 235, 0.2);
}

.message-bubble.assistant {
  background: white;
  color: #0F172A;
  border-bottom-left-radius: 4px;
  box-shadow: 0 2px 8px rgba(15, 23, 42, 0.08);
  border: 1px solid #E2E8F0;
}

.message-metadata {
  font-size: 0.75rem;
  color: #64748B;
  margin-top: 4px;
  opacity: 0.7;
}

/* Input area */
.input-section {
  flex-shrink: 0;
  background: white;
  border-top: 1px solid #E2E8F0;
  padding: 16px 24px 24px;
}

.input-wrapper {
  display: flex;
  gap: 12px;
  align-items: flex-end;
}

.text-input-container {
  flex: 1;
  display: flex;
  flex-direction: column;
}

.input-box {
  width: 100%;
  background: white;
  border: 1.5px solid #E2E8F0;
  border-radius: 20px;
  padding: 12px 18px;
  font-size: 0.95rem;
  font-family: inherit;
  resize: none;
  transition: all 0.2s ease;
}

.input-box:focus {
  outline: none;
  border-color: #2563EB;
  box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.1);
}

.input-box::placeholder {
  color: #94A3B8;
}

.send-btn {
  background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
  color: white;
  border: none;
  border-radius: 16px;
  padding: 10px 20px;
  font-weight: 600;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
  height: 42px;
}

.send-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
}

.send-btn:active {
  transform: translateY(0);
}

.clear-btn {
  background: #F1F5F9;
  color: #64748B;
  border: 1px solid #E2E8F0;
  border-radius: 16px;
  padding: 10px 16px;
  font-weight: 500;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.2s ease;
  height: 42px;
}

.clear-btn:hover {
  background: #E2E8F0;
  color: #475569;
}

.clear-btn:active {
  transform: translateY(0);
}

/* Dark Mode */
@media (prefers-color-scheme: dark) {
  body, .stApp, .main, .block-container {
    background: #0B1220 !important;
    color: #F8FAFC !important;
  }
  
  .chat-header {
    background: linear-gradient(135deg, #1D4ED8 0%, #1E40AF 100%);
    box-shadow: 0 4px 12px rgba(15, 23, 42, 0.5);
  }
  
  .chat-container {
    background: #0F172A;
  }
  
  .chat-messages::-webkit-scrollbar-thumb {
    background: rgba(71, 85, 105, 0.4);
  }
  
  .chat-messages::-webkit-scrollbar-thumb:hover {
    background: rgba(71, 85, 105, 0.6);
  }
  
  .empty-state-icon {
    opacity: 0.2;
  }
  
  .empty-state-title {
    color: #CBD5E1;
  }
  
  .empty-state-text {
    color: #64748B;
  }
  
  .message-bubble.assistant {
    background: #1E293B;
    color: #E2E8F0;
    border-color: #334155;
  }
  
  .input-section {
    background: #0F172A;
    border-top-color: #1E293B;
  }
  
  .input-box {
    background: #1E293B;
    border-color: #334155;
    color: #F8FAFC;
  }
  
  .input-box:focus {
    border-color: #2563EB;
    box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.2);
  }
  
  .input-box::placeholder {
    color: #64748B;
  }
  
  .clear-btn {
    background: #1E293B;
    color: #94A3B8;
    border-color: #334155;
  }
  
  .clear-btn:hover {
    background: #334155;
    color: #CBD5E1;
  }
}

/* Responsive */
@media (max-width: 768px) {
  .message-bubble {
    max-width: 85%;
  }
  
  .header-text h1 {
    font-size: 1.1rem;
  }
  
  .input-section {
    padding: 12px 16px 16px;
  }
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize chatbot
@st.cache_resource
def initialize_chatbot(conf_threshold=0.20):
    return LogisticsChatbot(confidence_threshold=conf_threshold)

try:
    chatbot = initialize_chatbot()
except Exception as e:
    st.error(f"❌ Failed to load the AI core pipeline. Details: {e}")
    st.info("💡 Advice: Ensure you have successfully populated data files and run `train_model.py` to compile the artifacts.")
    st.stop()

# Header with back button
col_back, col_header = st.columns([0.8, 5], gap="medium")

with col_back:
    if st.button("← Back", key="back_btn", use_container_width=True):
        st.switch_page("app.py")

with col_header:
    st.markdown("""
    <div class='header-text'>
        <h1>🤖 LogiBot</h1>
        <p>AI Logistics Customer Support</p>
    </div>
    """, unsafe_allow_html=True)

# Chat messages area
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
chat_placeholder = st.empty()

def render_messages():
    with chat_placeholder.container():
        if len(st.session_state.messages) == 0:
            st.markdown("""
            <div class='empty-state'>
                <div class='empty-state-icon'>💬</div>
                <div class='empty-state-title'>Start a conversation</div>
                <div class='empty-state-text'>Ask about tracking, deliveries, refunds, shipping, or any logistics question</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("<div class='chat-messages'>", unsafe_allow_html=True)
            
            for msg in st.session_state.messages:
                role = msg["role"]
                content = msg["content"]
                
                if role == "user":
                    st.markdown(f"""
                    <div class='message-group user'>
                        <div class='message-bubble user'>{content}</div>
                    </div>
                    """, unsafe_allow_html=True)
                else:
                    metadata_html = ""
                    if "metadata" in msg:
                        intent = msg["metadata"].get("intent", "n/a")
                        conf = msg["metadata"].get("conf", 0.0)
                        metadata_html = f"<div class='message-metadata'>⚙️ {intent} · {conf:.1%}</div>"
                    
                    st.markdown(f"""
                    <div class='message-group assistant'>
                        <div class='message-bubble assistant'>
                            {content}
                            {metadata_html}
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
            
            st.markdown("</div>", unsafe_allow_html=True)

render_messages()
st.markdown("</div>", unsafe_allow_html=True)

# Input area
st.markdown("<div class='input-section'>", unsafe_allow_html=True)

col_input, col_send, col_clear = st.columns([5, 0.8, 0.8], gap="small")

with col_input:
    user_text = st.text_area(
        "message",
        key="user_message",
        placeholder="Type your message... (Shift+Enter for new line)",
        height=44,
        label_visibility="collapsed"
    )

with col_send:
    send_btn = st.button("Send", key="send_button", use_container_width=True, help="Send message")

with col_clear:
    clear_btn = st.button("Clear", key="clear_button", use_container_width=True, help="Clear chat history")

st.markdown("</div>", unsafe_allow_html=True)

# Handle message sending
if send_btn and user_text.strip():
    user_message = user_text.strip()
    
    # Add user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })
    
    # Get response from backend
    bot_response, intent, confidence = chatbot.get_bot_response(user_message)
    
    # Add assistant message
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response,
        "metadata": {
            "intent": intent,
            "conf": confidence
        }
    })
    
    # Clear input and rerun
    st.session_state.user_message = ""
    st.rerun()

# Handle clear chat
if clear_btn:
    st.session_state.messages = []
    st.rerun()

# Auto-scroll to latest message
st.components.v1.html("""
<script>
function scrollToBottom() {
  setTimeout(() => {
    const chatMessages = document.querySelector('.chat-messages');
    if (chatMessages) {
      chatMessages.scrollTop = chatMessages.scrollHeight;
    }
  }, 100);
}

scrollToBottom();

const observer = new MutationObserver(scrollToBottom);
const container = document.querySelector('.chat-container');
if (container) {
  observer.observe(container, { childList: true, subtree: true });
}
</script>
""", height=0, width=0)
