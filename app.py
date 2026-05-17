import streamlit as st
from parser import extract_text_from_pdf
from analyzer import analyze_resume

# Page Configuration
st.set_page_config(page_title="Resume Magic AI", page_icon="✨", layout="centered")

# Custom Professional Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1E293B;
    }

    .main-title {
        color: #4F46E5;
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 10px;
        text-align: center;
    }

    .section-header {
        color: #334155;
        font-size: 22px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 10px;
        border-left: 5px solid #6366F1;
        padding-left: 15px;
    }

    .stButton>button {
        background-color: #4F46E5;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
        width: 100%;
        border: none;
        transition: 0.3s;
    }
    
    .stButton>button:hover {
        background-color: #4338CA;
        box-shadow: 0 4px 12px rgba(79, 70, 229, 0.3);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<p class="main-title">Resume Intelligence AI ✨</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B;'>Optimize your career path with our advanced AI analyzer.</p>", unsafe_allow_html=True)
st.write("---")

# --- Step 1: Job Description ---
st.markdown('<p class="section-header">Target Job Description</p>', unsafe_allow_html=True)
jd = st.text_area("Paste the job requirements here", placeholder="Paste the job requirements here...", height=150, label_visibility="collapsed")

# --- Step 2: Resume Upload ---
st.markdown('<p class="section-header">Your Professional Resume</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload your resume in PDF format", type=["pdf"], label_visibility="collapsed", key="resume_uploader")

# --- Step 3: Analysis ---
st.write("<br>", unsafe_allow_html=True)
if st.button("Start AI Analysis 🚀"):
    if jd and uploaded_file:
        with st.spinner("AI is analyzing your resume... Please wait."):
            # Extract text from PDF
            resume_text = extract_text_from_pdf(uploaded_file)
            
            if "Error" in resume_text:
                st.error(resume_text)
            else:
                # Analyze using Gemini
                analysis_result = analyze_resume(resume_text, jd)
                
                st.write("---")
                st.markdown('<p class="section-header">Analysis Result</p>', unsafe_allow_html=True)
                st.markdown(analysis_result)
    else:
        st.warning("Please provide both the Job Description and your Resume.")
