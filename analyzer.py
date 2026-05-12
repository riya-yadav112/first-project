import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def analyze_resume(resume_text, job_description):
    """
    Analyzes the resume against the job description using Gemini AI.
    """
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    prompt = f"""
    As an expert Technical Recruiter and Career Coach, analyze the following Resume against the provided Job Description.
    
    Resume Content: {resume_text}
    Job Description: {job_description}
    
    Please provide the following in a structured format:
    1. Match Percentage: A percentage score indicating how well the resume matches the JD.
    2. Key Skills Found: List of technical and soft skills identified in the resume.
    3. Missing Skills: Critical skills or keywords from the JD that are missing in the resume.
    4. Improvement Suggestions: Specific advice to tailor the resume for this role.
    5. Final Verdict: A brief summary of whether the candidate is a good fit.
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error during analysis: {str(e)}"
    
