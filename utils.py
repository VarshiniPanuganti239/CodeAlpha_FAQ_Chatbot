import os
import re
import joblib
from sklearn.metrics.pairwise import cosine_similarity

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

tfidf_vectorizer = joblib.load(
    os.path.join(BASE_DIR, "tfidf_vectorizer.pkl")
)

faq_vectors = joblib.load(
    os.path.join(BASE_DIR, "faq_vectors.pkl")
)

faq_df = joblib.load(
    os.path.join(BASE_DIR, "faq_dataset.pkl")
)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"www\S+", "", text)
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def get_best_answer(question):
    cleaned = clean_text(question)

    user_vector = tfidf_vectorizer.transform([cleaned])

    similarity = cosine_similarity(user_vector, faq_vectors)

    best_index = similarity.argmax()

    score = similarity[0][best_index]

    if score < 0.35:
        return (
            "Sorry, I couldn't find a relevant answer. Please try rephrasing your question.",
            score,
        )

    answer = faq_df.iloc[best_index]["answer"]

    return answer, score