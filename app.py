import streamlit as st
from utils import get_best_answer

st.set_page_config(
    page_title="AI FAQ Chatbot",
    page_icon="🤖",
    layout="wide"
)
# ============================================================
# Sidebar
# ============================================================

with st.sidebar:

    st.title("🤖 AI FAQ Chatbot")

    st.markdown("---")

    st.subheader("📌 Project Information")

    st.write("**Model:** TF-IDF + Cosine Similarity")

    st.write("**Dataset:** Customer Support FAQ")

    st.write("**Questions:** 500")

    st.write("**Technology:** NLP, Streamlit")

    st.markdown("---")

    st.subheader("🧠 Features")

    st.success("✔ Intelligent FAQ Retrieval")

    st.success("✔ NLP Text Cleaning")

    st.success("✔ TF-IDF Vectorization")

    st.success("✔ Cosine Similarity Search")

    st.success("✔ Streamlit Web App")

    st.markdown("---")

    st.subheader("👩‍💻 Developed By")

    st.info("Panuganti Varshini")

    st.markdown("---")

    st.caption("CodeAlpha Artificial Intelligence Internship")

st.title("🤖 AI FAQ Chatbot")

st.markdown("### CodeAlpha Artificial Intelligence Internship")

st.write(
    "Ask any customer support question and receive the most relevant answer using NLP and Machine Learning."
)

st.divider()

if "history" not in st.session_state:
    st.session_state.history = []

question = st.text_input(
    "💬 Ask your question"
)

if st.button("🚀 Get Answer"):

    if question.strip():

        answer, score = get_best_answer(question)

        st.session_state.history.append(
            (question, answer, score)
        )

st.subheader("Conversation")

for q, a, s in reversed(st.session_state.history):

    st.markdown(f"**🧑 You:** {q}")

    st.success(a)

    st.caption(f"Similarity Score: {round(s*100,2)}%")

if st.button("🗑 Clear Chat"):
    st.session_state.history = []