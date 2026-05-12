import streamlit as st

# Custom Professional Styling
st.markdown("""
    <style>
    /* 1. Pure App ka Font change */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #1E293B; /* Soft Dark Slate */
    }

    /* 2. Main Title Styling */
    .main-title {
        color: #4F46E5; /* Premium Indigo */
        font-size: 42px;
        font-weight: 800;
        letter-spacing: -1px;
        margin-bottom: 10px;
    }

    /* 3. Subheadings (Neutral & Clean) */
    .section-header {
        color: #334155; /* Slate Grey */
        font-size: 22px;
        font-weight: 600;
        margin-top: 30px;
        margin-bottom: 10px;
        border-left: 5px solid #6366F1; /* Accent Line */
        padding-left: 15px;
    }

    /* 4. Text Area aur Buttons ko thoda round karna */
    .stTextArea textarea {
        border-radius: 12px;
        border: 1px solid #E2E8F0;
    }
    
    .stButton>button {
        background-color: #4F46E5;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-weight: 600;
            

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
st.markdown('<p class="main-title">Resume Intelligence AI</p>', unsafe_allow_html=True)
st.write("Optimize your career path with our advanced analyzer.")

st.write("---") # Thin Divider line

# --- Job Description Section ---
st.markdown('<p class="section-header">Target Job Description</p>', unsafe_allow_html=True)
job_description = st.text_area("", placeholder="Paste the job requirements here...", height=150)

# --- Resume Upload Section ---
st.markdown('<p class="section-header">Your Professional Resume</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload PDF version only", type=["pdf"])

# --- Buttons ---
st.write("") # Thodi space ke liye
submit_button = st.button("Analyze Resume")

import streamlit as st

# Custom Styling with Cursive Font
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Inter:wght@400;700&display=swap');

    /* Cursive Font for Headings */
    .cursive-head {
        font-family: 'Dancing Script', cursive;
        color: #4F46E5;
        font-size: 45px; /* Size increased */
        margin-bottom: 5px;
    }

    /* Normal Clean Font for other text */
    .normal-text {
        font-family: 'Inter', sans-serif;
        font-size: 18px;
            
        color: #475569;
    }
    
    /* Image Container */
    .step-img {
        border-radius: 15px;
        margin-bottom: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header ---
st.markdown('<p class="cursive-head">Resume Intelligence AI</p>', unsafe_allow_html=True)
st.markdown('<p class="normal-text">Let\'s refine your career path step by step.</p>', unsafe_allow_html=True)
st.write("---")

# --- STEP 1: Job Description ---
st.markdown('<p class="cursive-head">Step 1: The Target</p>', unsafe_allow_html=True)
# Yahan image add karein (Target/Goal related)
st.image("https://img.icons8.com/illustrations/external-tulpahn-outline-color-tulpahn/100/external-target-business-management-tulpahn-outline-color-tulpahn.png", width=100)
st.markdown('<p class="normal-text">Paste the job description you are aiming for:</p>', unsafe_allow_html=True)
jd = st.text_area("", height=150, key="jd_input")

# --- STEP 2: Resume Upload ---
st.markdown('<p class="cursive-head">Step 2: Your Journey</p>', unsafe_allow_html=True)
# Yahan image add karein (Document/Profile related)
st.image("https://img.icons8.com/illustrations/external-tulpahn-outline-color-tulpahn/100/external-document-business-management-tulpahn-outline-color-tulpahn.png", width=100)
st.markdown('<p class="normal-text">Upload your current resume in PDF format:</p>', unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"])

# --- STEP 3: Analysis ---
st.markdown('<p class="cursive-head">Step 3: The Result</p>', unsafe_allow_html=True)
# Yahan image add karein (Analysis/Success related)
st.image("https://img.icons8.com/illustrations/external-tulpahn-outline-color-tulpahn/100/external-analysis-business-management-tulpahn-outline-color-tulpahn.png", width=100)
submit_button = st.button("Start Analysis ✨")
import streamlit as st

# Professional yet Cool Gen Z Styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Caveat:wght@400;700&display=swap');

    /* Pura App Cursive Font mein */
    html, body, [class*="css"], .stMarkdown, p, h1, h2, h3 {
        font-family: 'Caveat', cursive !important;
        font-size: 24px; /* Default font size increased */
    }

    /* Titles with Neon Glow (Works on Dark & Light) */
    .genz-title {
        color: #8B5CF6; /* Electric Violet */
        font-size: 60px;
        font-weight: 700;
        text-shadow: 2px 2px 10px rgba(139, 92, 246, 0.4);
        text-align: center;
        margin-bottom: 0px;
    }

    .genz-header {
        color: #EC4899; /* Hot Pink */
        font-size: 40px;
        margin-top: 40px;
        display: flex;
        align-items: center;
    }

    /* Input boxes ko round aur stylish banana */
    .stTextArea textarea, .stFileUploader {
        border-radius: 20px !important;
        border: 2px solid #6366F1 !important;
        background: rgba(255, 255, 255, 0.05);
    }

    /* Button Style: Pop-out effect */
    .stButton>button {
        background: linear-gradient(90deg, #8B5CF6 0%, #EC4899 100%);
        color: white;
        border-radius: 50px;
        padding: 15px 40px;
        font-size: 30px;
        border: none;
        box-shadow: 0 4px 15px rgba(236, 72, 153, 0.4);
        transition: 0.3s;
        width: 100%;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 6px 20px rgba(139, 92, 246, 0.6);
    }
    </style>
    """, unsafe_allow_html=True)

# --- Header Section ---
st.markdown('<p class="genz-title">Resume Magic AI ✨</p>', unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #64748B;'>Level up your career game with AI energy! 💅</p>", unsafe_allow_html=True)

# --- Step 1: Job Description ---
st.markdown('<div class="genz-header">🎯 Step 1: The Vibe Check (JD)</div>', unsafe_allow_html=True)
st.markdown("<i>Paste the Job Description to see if you match the energy!</i>", unsafe_allow_html=True)
jd = st.text_area("", placeholder="What's the job role?...", height=150)

# --- Step 2: Resume Upload ---
st.markdown('<div class="genz-header">📄 Step 2: Drop Your Resume</div>', unsafe_allow_html=True)
st.markdown("<i>Upload your PDF and let the AI do the heavy lifting!</i>", unsafe_allow_html=True)
uploaded_file = st.file_uploader("", type=["pdf"])

# --- Step 3: Analysis Button ---
st.write("<br>", unsafe_allow_html=True)
submit_button = st.button("Analyze My Vibe 🚀")
uploaded_file = st.file_uploader("", type=["pdf"])
uploaded_file = st.file_uploader("", type=["pdf"], key="resume_upload_unique")