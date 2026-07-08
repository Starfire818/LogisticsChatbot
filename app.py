"""
Main Page
Smart Logistics Assistant
"""

import streamlit as st


st.set_page_config(
    page_title="Smart Logistics Assistant",
    page_icon="📦",
    layout="wide"
)


# =========================
# CSS
# =========================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        180deg,
        #f8fbff 0%,
        #ffffff 100%
    );
}


.hero {
    background: linear-gradient(
        135deg,
        #2563eb,
        #60a5fa
    );
    padding:40px;
    border-radius:25px;
    color:white;
    margin-bottom:30px;
}


.card {

    background:white;
    padding:30px;
    border-radius:25px;
    box-shadow:
    0 10px 30px rgba(0,0,0,0.08);

    margin-bottom:20px;

}


.title {

font-size:35px;
font-weight:700;

}


.subtitle {

font-size:18px;

}


</style>
""",
unsafe_allow_html=True)



# =========================
# Header
# =========================


st.markdown("""
<div class="hero">

<div class="title">
📦 Smart Logistics Assistant
</div>

<div class="subtitle">
AI-powered customer support chatbot for logistics enquiries
</div>

</div>
""",
unsafe_allow_html=True)



# =========================
# Description
# =========================


st.markdown("""
<div class="card">

<h3>
Welcome 👋
</h3>


<p>
Our AI assistant can help you with:
</p>


<ul>

<li>
📦 Parcel tracking
</li>

<li>
🚚 Delivery status
</li>

<li>
🏠 Change delivery address
</li>

<li>
💰 Refund and shipping enquiries
</li>

</ul>


</div>
""",
unsafe_allow_html=True)



st.divider()


st.subheader(
"Choose Your Assistant"
)



col1,col2 = st.columns(2)



# =========================
# AI Bot
# =========================

with col1:


    st.markdown("""
    <div class="card">

    <h2>
    🤖 ParcelPal AI
    </h2>

    <p>
    Logistics customer support assistant.
    </p>


    </div>
    """,
    unsafe_allow_html=True)



    if st.button(
        "Start Chat",
        use_container_width=True
    ):

        st.switch_page(
            "pages/Chat.py"
        )




# =========================
# Future Bot
# =========================


with col2:


    st.markdown("""
    <div class="card">

    <h2>
    🧑 TEONGKAIZHE XJJ
    </h2>

    <p>
    Coming Soon
    </p>


    </div>
    """,
    unsafe_allow_html=True)



    st.button(
        "Unavailable",
        disabled=True,
        use_container_width=True
    )



# =========================
# Footer
# =========================

st.caption(
"Smart Logistics Assistant | NLP Customer Support System"
)