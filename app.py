import streamlit as st
from analyze import extract_text_from_pdf, extract_text_from_docx, get_similarity

# styling
st.markdown("""
    <style>
    .main-header {
        font-size: 3.5 rem;
        font-weight: bold;
        color: #2c3e50;
        text-align: center;
        text-shadow: 2px 2px 4px #bdc3c7
        margin-bottom: 0;        
    }
    .sub-header {
        font-size: 1.5 rem;  
        color: #7f8c8d;
        text-align: center;
        margin-top: 0;    
    }
    .stButton > button {
        background-color: #2980b9;
        color: white;
        border-radius: 8px;
        padding: 10px 24px;
        font-size: 1 rem;
        border: none;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
    }
    .stButton > button:hover {
        background-color: #3498db;
        color: white;
    }
    .stFileUploader {
        border: 2px dashed #95a5a6;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# Title and Subtitle
st.markdown("<h1 class='main-header'>📄 Smart Resume Analyzer</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-header'>Powered by NLP and Machine Learning</p.", unsafe_allow_html=True)

st.write("---")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Upload your Resume")
    st.info("Supported Formats: PDF and DOCX")
    resume_file = st.file_uploader("", type=["pdf", "docx"], key="resume_uploader")

with col2:
    st.subheader("Paste Job Description")
    st.warning("Ensure the job description is complete and accurate.")
    jd_input = st.text_area("", height=200, placeholder="PAste the full job description here...", key="jd_text_area")

# Analyzer
st.write("---")
if st.button("Analyze"):
    if resume_file and jd_input:
        if resume_file.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(resume_file)
        else:
            resume_text = extract_text_from_docx(resume_file)

        score = get_similarity(resume_text, jd_input)

        # expander
        with st.expander("Analysis Results", expanded=True):
            st.subheader("Resume Match Score")
            st.metric(label="Match Percentage", value=f"{score}%")

        if score > 75:
            st.success("🎉 Awesome! Your resume matches the job well.")
            st.balloons()
        elif score > 50:
            st.info("👍 Good job! Your resume has a solid match. Consider adding more keywords.")
        else:
            st.warning("Your resume could use more relevant keywords to match the job description.")
    else:
        st.error("⚠️ Please upload a resume and enter the job description.")

