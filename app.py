import streamlit as st
from matcher import clean_text, extract_text_from_pdf, get_match_score,extract_skills,get_skill_score

st.title("Resume Matcher")

st.write('Upload your resume and paste the job description to see how well they match with each other')

job_description = st.text_area("Paste a job description here")
resume_file = st.file_uploader("Upload your resume PDF", type= ["pdf"])

if st.button('Calculate Match Score'):
    if not job_description:
        st.warning('Please paste a job description')
    elif resume_file is None:
        st.warning('Please uploade a Resume')
    else:
        resume_text = extract_text_from_pdf(resume_file)
        cleaned_resume = clean_text(resume_text)
        cleaned_job_description = clean_text(job_description)
        job_skills = extract_skills(cleaned_job_description)
        resume_skills = extract_skills(cleaned_resume)
        skill_score = get_skill_score(job_skills, resume_skills)
        score = get_match_score(cleaned_resume, cleaned_job_description)

        st.subheader(f"Skill Score: {skill_score}%")


        st.subheader(f"Document Score: {score}%")