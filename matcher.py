import nltk
import PyPDF2
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re
nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)

from nltk.corpus import stopwords
stop_words = set(stopwords.words('english'))

SKILL_LIST = {
    "Programming Languages": [
        "python", "java", "javascript", "typescript", "c", "cpp", "csharp",
        "ruby", "swift", "kotlin", "golang", "rust", "php", "scala", "sql",
        "bash", "html", "css", "xml", "json"
    ],
    "Frameworks": [
        "django", "flask", "fastapi", "react", "angular", "vue", "nodejs",
        "express", "spring", "laravel", "rails", "nextjs", "nuxtjs",
        "bootstrap", "tailwind", "jquery"
    ],
    "Databases": [
        "postgresql", "mysql", "mongodb", "sqlite", "firebase", "redis",
        "oracle", "cassandra", "dynamodb", "mariadb", "elasticsearch"
    ],
    "ML & Data Science": [
        "pandas", "numpy", "scikit", "tensorflow", "pytorch", "keras",
        "matplotlib", "seaborn", "opencv", "nltk", "spacy", "huggingface",
        "xgboost", "lightgbm", "scipy", "jupyter"
    ],
    "Cloud & DevOps": [
        "aws", "azure", "gcp", "docker", "kubernetes", "jenkins", "terraform",
        "ansible", "linux", "git", "github", "gitlab", "bitbucket", "cicd",
        "nginx", "apache"
    ],
    "Soft Skills": [
        "communication", "teamwork", "leadership", "management", "problem",
        "analytical", "collaborative", "creative", "organized", "motivated",
        "adaptable", "responsible", "detail"
    ]
}


def extract_text_from_pdf(pdf_file):
    text =""

    try:
        reader = PyPDF2.PdfReader(pdf_file)
        for page in reader.pages:
            text += page.extract_text()
    except Exception as e:
        return f"Error Reading PDF: {str(e)}"
    
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'\S+@\S+', '', text)
    text = re.sub(r'http\S+|www\S+', '', text)
    text = re.sub(r'\S*(github|linkedin|http|www|\.com)\S*', '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = word_tokenize(text)
    words = [word for word in tokens if word not in stop_words]
    cleaned_text = " ".join(words)
    return cleaned_text

def extract_skills(cleaned_text):
    words = set(cleaned_text.split())
    found_skills = {}
    for category, skills in SKILL_LIST.items():
        matched = [skill for skill in skills if skill in words]
        if matched:
            found_skills[category] = matched
    return found_skills

def get_skill_score(job_skills, resume_skills):
    if not job_skills or not resume_skills:
        return 0.0
    job_skills_list = set([skill for skills in job_skills.values() for skill in skills])
    resume_skills_list = set([skill for skills in resume_skills.values() for skill in skills])
    matched = job_skills_list & resume_skills_list
    skill_score = round((len(matched) / len(job_skills_list)) * 100, 2)
    return skill_score

def get_match_score(job_text, resume_text):
    if not job_text or not resume_text:
        return 0.0
    processed_job = clean_text(job_text)
    processed_resume = clean_text(resume_text)
    vectorize = TfidfVectorizer(stop_words="english",
        ngram_range=(1,2),
        max_features=50)
    vectors = vectorize.fit_transform([processed_job, processed_resume])
    score = cosine_similarity(vectors[0], vectors[1])
    return round(float(score[0][0]) * 100, 2)



