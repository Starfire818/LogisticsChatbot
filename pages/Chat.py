"""
Chat Page
Logistics NLP Assistant
"""


import streamlit as st

from chatbot import LogisticsChatbot



st.set_page_config(
    page_title="ParcelPal AI",
    page_icon="🤖",
    layout="wide"
)



# =========================
# Backend
# =========================


@st.cache_resource
def load_chatbot(threshold):

    return LogisticsChatbot(
        confidence_threshold=threshold
    )



# =========================
# Sidebar
# =========================


st.sidebar.title(
"⚙️ Settings"
)


confidence = st.sidebar.slider(
    "Confidence Threshold",
    0.0,
    1.0,
    0.20,
    0.01
)



st.sidebar.divider()


if st.sidebar.button(
    "🗑 Clear Chat"
):

    st.session_state.messages = []



# =========================
# Load Model
# =========================


chatbot = load_chatbot(
    confidence
)



# =========================
# Session
# =========================


if "messages" not in st.session_state:

    st.session_state.messages = []



# =========================
# Header
# =========================


col1,col2 = st.columns([1,6])


with col1:

    if st.button("⬅ Back"):

        st.switch_page(
            "app.py"
        )



with col2:

    st.title(
        "🤖 ParcelPal AI"
    )



# =========================
# Chat History
# =========================


for message in st.session_state.messages:


    with st.chat_message(
        message["role"]
    ):

        st.markdown(
            message["content"]
        )


# =========================
# Input
# =========================


prompt = st.chat_input(
    "Ask about your parcel, delivery or shipping..."
)



if prompt:


    # User message

    st.session_state.messages.append(
        {
            "role":"user",
            "content":prompt
        }
    )


    with st.chat_message(
        "user"
    ):

        st.markdown(prompt)



    # Bot response

    response, intent, confidence_score = chatbot.get_bot_response(
        prompt
    )


    bot_text = f"""
{response}


---
⚙️ Intent: `{intent}`

Confidence:
`{confidence_score:.2%}`
"""


    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":bot_text
        }
    )


    with st.chat_message(
        "assistant"
    ):

        st.markdown(bot_text)