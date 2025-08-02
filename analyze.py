import PyPDF2
import docx2txt
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

nltk.download('stopwords')
stop_words = nltk.corpus.stopwords.words('english')

def extract_text_from_pdf(file):
    pdfReader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdfReader.pages:
        text += page.extract_text()
    return text

def extract_text_from_docx(file):
    return docx2txt.process(file)

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

def get_similarity(resume_text, jd_text):
    resume_text = preprocess_text(resume_text)
    jd_text = preprocess_text(jd_text)

    tfidf = TfidfVectorizer()
    tfidf_matrix = tfidf.fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]


    return round(score * 100, 2)