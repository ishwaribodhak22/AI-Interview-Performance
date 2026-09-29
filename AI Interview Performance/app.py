import streamlit as st
import joblib

from streamlit_mic_recorder import mic_recorder
from utils.pdf_report import generate_pdf
from utils.report import create_report
from utils.filler import count_fillers
from utils.sentiment import analyze_sentiment
from utils.grammar import grammar_check
from utils.score import communication_score
from utils.feedback import generate_feedback
from utils.charts import (
    gauge_chart,
    performance_chart,
    donut_chart,
    radar_chart
)

# -----------------------------
# Load CSS
# -----------------------------
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="AI Interview Performance Analyzer",
    page_icon="🎤",
    layout="wide"
)

load_css()

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

# -----------------------------
# Header
# -----------------------------
st.title("🎤 AI Interview Performance Analyzer")
st.markdown("### 🤖 Machine Learning + NLP Powered Interview Coach")

st.divider()

# -----------------------------
# User Input
# -----------------------------
candidate_name = st.text_input(
    "👤 Candidate Name",
    placeholder="Enter your name"
)

answer = st.text_area(
    "📝 Enter your Interview Answer",
    height=220,
    placeholder="Example: Tell me about yourself..."
)

st.markdown("### 🎤 Or Record Your Answer")

audio = mic_recorder(
    start_prompt="🎙️ Start Recording",
    stop_prompt="⏹️ Stop Recording",
    key="recorder"
)

# -----------------------------
# Analyze
# -----------------------------
if st.button("🚀 Analyze Interview"):

    # ML Prediction
    answer_vector = vectorizer.transform([answer])
    interview_score = model.predict(answer_vector)[0]

    # NLP Analysis
    grammar_errors = grammar_check(answer)
    filler_words = count_fillers(answer)
    sentiment = analyze_sentiment(answer)

    # Communication Score
    final_score = communication_score(
        interview_score,
        grammar_errors,
        filler_words,
        sentiment
    )

    # Feedback
    feedback = generate_feedback(
        grammar_errors,
        filler_words,
        sentiment
    )

    # -----------------------------
    # Main Metrics
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🎯 Interview Score",
            f"{round(interview_score,2)}/10"
        )

    with col2:
        st.metric(
            "🏆 Communication Score",
            f"{final_score}/100"
        )

    st.divider()

    # -----------------------------
    # Secondary Metrics
    # -----------------------------
    col3, col4, col5 = st.columns(3)

    with col3:
        st.metric(
            "📝 Grammar Errors",
            grammar_errors
        )

    with col4:
        st.metric(
            "🎯 Filler Words",
            filler_words
        )

    with col5:
        st.metric(
            "💬 Sentiment",
            sentiment
        )

    st.divider()

    # -----------------------------
    # Rating
    # -----------------------------
    if final_score >= 90:
        st.success("⭐⭐⭐⭐⭐ Outstanding")

    elif final_score >= 75:
        st.success("⭐⭐⭐⭐ Excellent")

    elif final_score >= 60:
        st.warning("⭐⭐⭐ Good")

    elif final_score >= 40:
        st.warning("⭐⭐ Average")

    else:
        st.error("⭐ Needs Improvement")

    st.divider()
    # -----------------------------
    # Analytics Dashboard
    # -----------------------------
    st.subheader("📊 Analytics Dashboard")

    # -----------------------------
    # First Row
    # -----------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.plotly_chart(
            gauge_chart(final_score),
            use_container_width=True
        )

    with col2:
        st.plotly_chart(
            performance_chart(
                round(interview_score, 2),
                grammar_errors,
                filler_words
            ),
            use_container_width=True
        )

    # -----------------------------
    # Second Row
    # -----------------------------
    col3, col4 = st.columns(2)

    with col3:
        st.plotly_chart(
            donut_chart(
                round(interview_score, 2),
                grammar_errors,
                filler_words
            ),
            use_container_width=True
        )

    with col4:
        st.plotly_chart(
            radar_chart(
                final_score,
                grammar_errors,
                filler_words,
                sentiment
            ),
            use_container_width=True
        )

    st.divider()

    # -----------------------------
    # Suggestions
    # -----------------------------
    left_col, right_col = st.columns([2, 1])

    with left_col:

        st.subheader("💡 AI Suggestions")

        for item in feedback:
            st.success(item)

        st.divider()

        st.subheader("📄 Download Interview Report")

        report = create_report(
            interview_score,
            final_score,
            grammar_errors,
            filler_words,
            sentiment,
            feedback
        )

        st.download_button(
            label="📥 Download Report",
            data=report,
            file_name="Interview_Report.txt",
            mime="text/plain"
        )

        st.divider()

        st.subheader("📄 PDF Report")

        generate_pdf(
            candidate_name,
            interview_score,
            final_score,
            grammar_errors,
            filler_words,
            sentiment,
            feedback
        )

        with open("Interview_Report.pdf", "rb") as pdf_file:
            st.download_button(
                label="📥 Download PDF Report",
                data=pdf_file,
                file_name="Interview_Report.pdf",
                mime="application/pdf"
            )

    with right_col:
        st.empty()