import streamlit as st
from parser import extract_text_from_pdf
from analyzer import analyze_resume
import os

# Page Configuration
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

# Custom CSS for "New Gen" Aesthetic
st.markdown("""
    <style>
    .main {
        background-color: #020617;
        color: #f1f5f9;
    }
    .stButton>button {
        background: linear-gradient(45deg, #38bdf8, #818cf8);
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 24px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(56, 189, 248, 0.4);
    }
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 25px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🚀 New Gen Resume Analyzer")
    st.subheader("Evaluate your resume against any Job Description using AI")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        st.markdown("### 📝 Job Description")
        jd_text = st.text_area("Paste the job description here...", height=300)

    with col2:
        st.markdown("### 📂 Upload Resume")
        uploaded_file = st.file_uploader("Upload your resume (PDF format)", type=["pdf"])

    if st.button("Analyze Resume"):
        if uploaded_file is not None and jd_text != "":
            with st.spinner("Analyzing with AI..."):
                # 1. Extract Text
                resume_text = extract_text_from_pdf(uploaded_file)
                
                # 2. Analyze with Gemini
                analysis_results = analyze_resume(resume_text, jd_text)
                
                # 3. Display Results
                st.markdown("---")
                st.markdown("### 📊 Analysis Results")
                st.markdown(f'<div class="glass-card">{analysis_results}</div>', unsafe_allow_html=True)
        else:
            st.error("Please upload a resume and provide a job description.")

if __name__ == "__main__":
    main()
