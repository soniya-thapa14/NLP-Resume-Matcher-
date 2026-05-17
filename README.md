##Resume Matcher

A Python web application that compares your resume against a job description and gives you a match score using NLP techniques.

------
##What It Does

- Upload your resume as a PDF
- Paste any job description
- Get two scores:
  - **Skill Score** — how many required skills your resume has
  - **Document Score** — how similar your resume is to the job description overall

-----

How It Works

The app uses two methods to calculate how well your resume matches a job description:

**1. Skill Matching**
It scans both your resume and the job description for known skills across categories like Programming Languages, Frameworks, Databases, ML & Data Science, Cloud & DevOps, and Soft Skills. It then calculates what percentage of the job's required skills appear in your resume.

**2. TF-IDF Cosine Similarity**
It converts both documents into numerical vectors using TF-IDF (Term Frequency-Inverse Document Frequency) and measures the angle between them. The smaller the angle, the more similar the documents.

----

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/yourusername/resume-matcher.git
cd resume-matcher
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

---

## Requirements

```
streamlit
PyPDF2
nltk
scikit-learn
```

Or install all at once:
```bash
pip install streamlit PyPDF2 nltk scikit-learn
```

---

## Usage

1. Run the app with `streamlit run app.py`
2. Paste the job description in the text box
3. Upload your resume as a PDF file
4. Click **Calculate Match Score**
5. View your Skill Score and Document Score

----

## Tech Stack

- **Python** 
- **Streamlit** 
- **PyPDF2** 
- **NLTK** 
- **Scikit-learn** — TF-IDF vectorization and cosine similarity

