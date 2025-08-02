**📄 Smart Resume Analyzer**

An intelligent web application that helps job seekers and recruiters quickly determine how well a resume matches a job description. The application uses Natural Language Processing (NLP) and Machine Learning (ML) to provide a similarity score and actionable feedback.

---

**✨ Features**

- **Resume Upload:** Supports uploading resumes in both PDF and DOCX formats.
- **Job Description Input:** A dedicated text area for pasting the job description.
- **Similarity Score:** Calculates a percentage-based match score using TF-IDF and Cosine Similarity.
- **Visual Feedback:** Provides clear, color-coded feedback and a fun "balloons" animation for high-scoring matches.
- **User-Friendly Interface:** Built with Streamlit to be simple, clean, and intuitive.

---

**💻 Technology Stack**

- **Frontend:** Streamlit
- **Backend:** Python
- **NLP/ML:** scikit-learn for TF-IDF and Cosine Similarity
- **Text Extraction:** PyPDF2 (for PDF) and docx2txt (for DOCX)
- **Text Preprocessing:** nltk for stop word removal

---

**📌 How It Works**

1. Upload your resume (PDF or DOCX)
2. Paste the job description
3. App cleans and preprocesses both texts
4. Applies TF-IDF vectorization
5. Uses cosine similarity to score the match
6. Shows you the match score + feedback

---

**🚀 Setup and Installation**
Follow these steps to get the project up and running on your local machine.

```bash

# 1. Clone the Repository
git clone https://github.com/piyush-dhote/Smart-Resume-Analyzer.git
cd Smart-Resume-Analyzer

# 2. Create a Virtual Environment
It is highly recommended to use a virtual environment to manage dependencies.
# For macOS / Linux
python3 -m venv venv
source venv/bin/activate

# For Windows
python -m venv venv
.\venv\Scripts\activate

# 3. Install Dependencies
Install the required Python libraries using the requirements.txt file.
pip install -r requirements.txt

# 4. Download NLTK Stopwords
# Your application requires the stopwords corpus from NLTK. Run this command once to download it:
python -c "import nltk; nltk.download('stopwords')"

# 5. Run the Application
# Now you can start the Streamlit application.
streamlit run app.py
# Your default web browser will open to http://localhost:8501, where you can access the application.

```

---

**📖 Usage**
Upload your resume using the file uploader.

1. Paste the job description into the text area.
2. Click the "Analyze" button.
3. The application will display a match score and a message indicating how well your resume aligns with the job description.

---

**👨‍💻 Connect with the Author**

**Piyush Dhote**
🔗[GitHub](https://github.com/piyush-dhote/Smart-Resume-Analyzer)
🔗[LinkedIn](https://www.linkedin.com/in/piyush-dhote/)
📧 piyussh.dhote@gmail.com
🎓 Fresher Engineer (CS)

---

**📜 License**

This project is licensed under the MIT License.
You are free to use, modify, and distribute it with attribution.