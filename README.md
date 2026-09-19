# 🤖 AI Resume Analyzer and Job Recommendation System

An NLP-based Streamlit application that analyzes resumes, extracts job-related skills, compares them with predefined job roles, calculates match scores, identifies skill gaps, recommends suitable roles, and generates a learning roadmap.

---

## 📌 Project Overview

The **AI Resume Analyzer and Job Recommendation System** is an educational and career guidance application developed using Python and Streamlit.

The system allows users to upload a resume in **PDF or DOCX format**. The uploaded resume is processed to extract and clean the resume text. Relevant technical and job-related skills are then identified using a controlled skill dictionary and keyword matching.

The extracted skills are compared with predefined job-role requirements. The system calculates a resume-to-role match score, displays matched and missing skills, recommends suitable job roles, and generates a basic learning roadmap based on the identified skill gaps.

The application also provides a **downloadable PDF resume analysis report**.

---

# 🎯 Project Objective

The main objectives of this project are to:

- Upload resumes in PDF and DOCX formats.
- Extract text from resumes.
- Clean and normalize unstructured resume text.
- Identify technical and job-related skills.
- Compare resume skills with job-role requirements.
- Calculate resume-to-job-role match scores.
- Recommend suitable job roles.
- Identify missing or weak skills.
- Generate a basic learning roadmap.
- Provide an interactive Streamlit interface.
- Generate and download a PDF analysis report.
- Provide educational and career guidance to students and job seekers.

---

# ✨ Features

## 1. Resume Upload

The application allows users to upload resumes in:

- PDF format
- DOCX format

The uploaded resume is processed directly by the application for analysis.

---

## 2. Resume Text Extraction

The system extracts text from the uploaded resume.

### PDF Resume Extraction

PDF files are processed using:

- PyPDF

### DOCX Resume Extraction

DOCX files are processed using:

- python-docx

The extracted text is then passed to the text-cleaning module.

---

## 3. Text Cleaning and Normalization

The extracted resume text is cleaned before skill analysis.

The cleaning process includes:

- Converting text to lowercase.
- Removing unnecessary symbols.
- Removing repeated spaces.
- Normalizing text for comparison.
- Preparing resume text for skill matching.

Important technical terms are preserved where possible.

---

## 4. Skill Extraction

The application identifies technical and job-related skills from the resume.

Skills are extracted using a controlled skill dictionary and keyword matching.

The project skill dictionary contains skills from areas such as:

### Programming

- Python
- Java
- C++
- JavaScript

### Web Development

- HTML
- CSS
- Flask
- FastAPI
- Streamlit
- Django

### Data Analysis

- SQL
- Pandas
- NumPy
- Excel
- Power BI
- Tableau
- Data Analysis
- Data Visualization
- Statistics

### Artificial Intelligence and Machine Learning

- Machine Learning
- Deep Learning
- Artificial Intelligence
- Scikit-learn
- TensorFlow
- PyTorch

### Specialized AI

- NLP
- Natural Language Processing
- Computer Vision
- OpenCV

### Software and Cloud Technologies

- Docker
- Kubernetes
- Git
- GitHub
- AWS
- Azure
- Linux

### Databases

- MongoDB
- MySQL
- PostgreSQL

### Computer Science Fundamentals

- Data Structures
- Algorithms

---

## 5. Job Role Dataset

The application uses a predefined CSV dataset containing job roles and their required skills.

Currently supported job roles include:

- Data Analyst
- Machine Learning Engineer
- AI Engineer
- NLP Engineer
- Computer Vision Engineer

The job-role dataset is stored in:

```text
data/job_roles.csv

---
6. Job Role Matching
The extracted resume skills are compared with the skills required for each predefined job role.
The system calculates how closely the resume skills match the requirements of each role.
The matching process considers the skills detected in the uploaded resume and the required skills listed for each job role.
7. Match Score Calculation
A match percentage is calculated for each job role based on the skills matched between the resume and the role requirements.
The application displays:
Job role
Match percentage
Matched skills
Missing skills
A higher percentage represents a greater overlap between the detected resume skills and the predefined role requirements.
The score is an estimate for educational and career guidance purposes.
8. Job Role Recommendation
The system compares the resume against multiple predefined job roles and displays the roles according to their calculated match scores.
The application can recommend suitable roles based on the skills detected in the resume.
Example roles include:
Data Analyst
Machine Learning Engineer
AI Engineer
NLP Engineer
Computer Vision Engineer
9. Skill Gap Analysis
The system compares the extracted resume skills with the required skills for each job role.
It displays two categories:
Skills Found
Skills that are detected in the uploaded resume and are relevant to the selected job role.
Missing Skills
Required skills that were not detected in the uploaded resume.
This helps users understand areas they may want to study or improve.
Note: Missing keywords do not necessarily mean that a person lacks the actual ability. A skill may be present but written using different terminology or not detected by the keyword-based extraction method.
10. Learning Roadmap
The application generates a basic learning roadmap based on the missing skills.
The roadmap provides:
Missing skill
Suggested learning topic
Learning sequence
Example:
Step 1: Learn NLP fundamentals
Step 2: Study natural language processing techniques
Step 3: Practice Machine Learning using Scikit-learn
Step 4: Learn data structures and algorithms
The roadmap is intended to provide basic educational guidance.