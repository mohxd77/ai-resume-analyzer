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

**```text
data/job_roles.csv**

---

### 6. Job Role Matching
The extracted resume skills are compared with the skills required for each predefined job role.
The system calculates how closely the resume skills match the requirements of each role.
The matching process considers the skills detected in the uploaded resume and the required skills listed for each job role.

---

### 7. Match Score Calculation
A match percentage is calculated for each job role based on the skills matched between the resume and the role requirements.
The application displays:
Job role
Match percentage
Matched skills
Missing skills
A higher percentage represents a greater overlap between the detected resume skills and the predefined role requirements.
The score is an estimate for educational and career guidance purposes.

---

### 8. Job Role Recommendation
The system compares the resume against multiple predefined job roles and displays the roles according to their calculated match scores.
The application can recommend suitable roles based on the skills detected in the resume.
Example roles include:
Data Analyst
Machine Learning Engineer
AI Engineer
NLP Engineer
Computer Vision Engineer

---

### 9. Skill Gap Analysis
The system compares the extracted resume skills with the required skills for each job role.
It displays two categories:
Skills Found
Skills that are detected in the uploaded resume and are relevant to the selected job role.
Missing Skills
Required skills that were not detected in the uploaded resume.
This helps users understand areas they may want to study or improve.

Note: Missing keywords do not necessarily mean that a person lacks the actual ability. A skill may be present but written using different terminology or not detected by the keyword-based extraction method.

---

### 10. Learning Roadmap
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
---
### 11. Downloadable Resume Analysis Report
The application provides a Download Resume Analysis Report feature through Streamlit.
After a resume is uploaded and analyzed, the user can download the generated analysis as a PDF file.
The downloadable report contains:
Extracted skills
Job role analysis
Match percentage
Matched skills
Missing skills
Learning roadmap

The PDF report is generated automatically by the application.
Users can click:
📥 Download Resume Analysis Report
to download the report.

Example filename:
resume_analysis_report.pdf

The project also contains sample generated analysis reports inside:
reports/
---
### 🔄 Project Workflow
The overall workflow of the application is:
Upload PDF or DOCX Resume
          ↓
Extract Resume Text
          ↓
Clean and Normalize Text
          ↓
Identify Job-Related Skills
          ↓
Load Job-Role Requirements
          ↓
Compare Resume Skills with Job Roles
          ↓
Calculate Match Scores
          ↓
Recommend Suitable Job Roles
          ↓
Identify Missing Skills
          ↓
Generate Learning Roadmap
          ↓
Display Results in Streamlit
          ↓
Generate Downloadable PDF Report

---
### 🧩 Project Modules

Module 1: Resume Upload

Responsible for:
Accepting PDF and DOCX files.
Validating uploaded files.
Passing the uploaded file to the resume parser.
File:
app.py
---
Module 2: Resume Parsing

Responsible for extracting text from:
PDF resumes
DOCX resumes
File:
resume_parser.py

Module 3: Text Cleaning

Responsible for:
Lowercase conversion.
Removing unnecessary characters.
Removing repeated spaces.
Normalizing text.
File:
text_cleaner.py
---
Module 4: Skill Extraction
Responsible for:
Loading the skill dictionary.
Searching for relevant skills.
Extracting detected skills from the resume.
Files:
skill_extractor.py
data/skill_dictionary.csv
---
Module 5: Job Matching
Responsible for:
Loading job roles.
Comparing resume skills with required skills.
Calculating match percentages.
Identifying matched skills.
Identifying missing skills.
Producing job-role results.
Files:
job_matcher.py
data/job_roles.csv
---
Module 6: Learning Roadmap
Responsible for generating learning recommendations based on missing skills.
File:
roadmap_generator.py
---
Module 7: Streamlit Dashboard

The Streamlit application provides:
Resume upload interface.
Extracted skills display.
Job-role match results.
Match percentage.
Matched skills.
Missing skills.
Learning roadmap.
PDF report download option.
Main file:
app.py
---
### 📁 Project Structure
ai_resume_analyzer/
│
├── app.py
├── resume_parser.py
├── text_cleaner.py
├── skill_extractor.py
├── job_matcher.py
├── roadmap_generator.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── job_roles.csv
│   └── skill_dictionary.csv
│
├── sample_resumes/
│   ├── ALEX SHARMA.docx
│   ├── ARJUN REDDY.pdf
│   ├── PRIYA KUMAR.docx
│   ├── RAHUL VERMA.pdf
│   └── SNEHA PATEL.docx
│
├── reports/
│   ├── alex_analysis_report.pdf
│   ├── arjun_analysis_report.pdf
│   ├── priya_analysis_report.pdf
│   ├── rahul_analysis_report.pdf
│   └── sneha_analysis_report.pdf
│
└── tests/
    └── test_cases.csv
---
### ⚙️ Installation
1. Clone or download the project
Download the project source code and open the project folder in VS Code.
2. Create a virtual environment
On Windows:
python -m venv venv
3. Activate the virtual environment
venv\Scripts\activate
4. Install dependencies
Install all required Python packages using:
pip install -r requirements.txt
---
### ▶️ Running the Application
Make sure the virtual environment is activated.
Run:
streamlit run app.py
The Streamlit application will open in a web browser.
Upload a PDF or DOCX resume and the system will perform the analysis.

After the analysis is completed, the user can download the generated PDF report using:
📥 Download Resume Analysis Report
🧪 Testing and Evaluation
Five sample resumes were tested using the Streamlit application.

The sample resumes are stored in:
sample_resumes/
The generated analysis reports are stored in:
reports/
The test cases are documented in:
tests/test_cases.csv
---
### 📊 Sample Testing Results
The application was tested using resumes representing different technical skill profiles.
Sneha Patel
The analysis identified skills related to:
Python
Artificial Intelligence
Machine Learning
Deep Learning
TensorFlow
PyTorch
Computer Vision
OpenCV

The generated report showed:
AI Engineer: 100%
Computer Vision Engineer: 100%

Arjun Reddy
The analysis identified skills related to:
Python
SQL
Pandas
NumPy
Excel
Power BI
Tableau
Data Analysis
Data Visualization
Statistics

The generated report showed:
Data Analyst: 100%


Priya Kumar
The analysis identified skills related to:
Python
Pandas
NumPy
Machine Learning
Deep Learning
PyTorch
NLP
Natural Language Processing

The generated report showed:
NLP Engineer: 100%

Rahul Verma
The analysis identified skills related to:
Python
SQL
Pandas
NumPy
Machine Learning
Artificial Intelligence
Statistics
Data Structures
Algorithms
Git
GitHub

The generated report showed:
Machine Learning Engineer: 87.5%

Alex Sharma

The analysis identified skills related to:
Python
SQL
Pandas
NumPy
Excel
Power BI
Tableau
Data Analysis
Data Visualization
Statistics

The generated report showed:
Data Analyst: 100%
---
### 📄 Sample Reports
The generated PDF reports are included in the project under:
reports/

The reports demonstrate:
Extracted skills.
Job role analysis.
Match percentages.
Matched skills.
Missing skills.
Learning roadmaps.
---

### 🧪 Testing File

The test cases are stored in:
tests/test_cases.csv

The file contains:
test_id,resume,expected_top_role,expected_min_match_score
TC01,SNEHA PATEL.docx,AI Engineer,100
TC02,ARJUN REDDY.pdf,Data Analyst,100
TC03,PRIYA KUMAR.docx,NLP Engineer,100
TC04,RAHUL VERMA.pdf,Machine Learning Engineer,87.5
TC05,ALEX SHARMA.docx,Data Analyst,100
---
### 🔐 Responsible AI
This application is designed for educational and career guidance purposes.

The system follows these principles:
The tool should be used for guidance, not automatic hiring or rejection.
The system focuses on job-related skills and information.
Gender, age, religion, nationality, photograph, marital status, and disability should not be used for scoring.
Match scores are estimates and should not be treated as recruiter decisions.
Missing keywords do not necessarily mean missing ability.
Uploaded resumes should be handled responsibly.
Temporary uploaded resume data should not be stored permanently without user permission.
---

### ⚠️ Limitations
The current system has some limitations:

Skill extraction mainly uses keyword matching.
A skill may not be detected if it is written using different terminology.
Match scores depend on the predefined job-role requirements.
The system does not determine a person's actual ability solely from keywords.
The predefined job-role dataset contains a limited number of roles.
The learning roadmap provides basic educational guidance rather than a complete professional curriculum.
Match scores should not be interpreted as recruitment decisions.
---

### 🚀 Future Enhancements
Possible future improvements include:

Advanced NLP-based skill extraction.
spaCy-based entity and phrase extraction.
Sentence Transformer-based semantic matching.
Machine-learning-based classification when suitable labelled data is available.
Job-description upload and matching.
Resume improvement suggestions.
More job roles and industry-specific skills.
Downloadable advanced PDF reports.
Job-role dashboards with charts.
FastAPI backend.
Database integration.
Docker deployment.
Cloud deployment.
Feedback-based improvement of the skill dictionary.
AI-generated resume feedback.
---
### Possible Advanced Architecture
The current project can be extended using the following architecture:
                  ┌─────────────────────┐
                  │   User / Student    │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Streamlit Interface │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Resume Upload      │
                  │    PDF / DOCX       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Resume Parser      │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Text Cleaner       │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │  Skill Extractor    │
                  └──────────┬──────────┘
                             │
                 ┌───────────┴───────────┐
                 ▼                       ▼
       ┌──────────────────┐    ┌──────────────────┐
       │ Skill Dictionary │    │   Job Roles CSV  │
       └────────┬─────────┘    └────────┬─────────┘
                │                       │
                └───────────┬───────────┘
                            ▼
                  ┌─────────────────────┐
                  │    Job Matcher      │
                  └──────────┬──────────┘
                             │
                 ┌───────────┼───────────┐
                 ▼           ▼           ▼
          Match Score   Skill Gaps   Recommendations
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Roadmap Generator   │
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ PDF Report Generator│
                  └──────────┬──────────┘
                             │
                             ▼
                  ┌─────────────────────┐
                  │ Download PDF Report │
                  └─────────────────────┘
---
### 📦 Final Deliverables

The final project contains:
Working Streamlit application.
Complete Python source code.
Job-role dataset.
Skill dictionary.
Five sample resumes.
Five generated PDF analysis reports.
requirements.txt.
README.md.
.gitignore.
Testing CSV file.
Architecture/workflow documentation.
Downloadable resume analysis report feature.
GitHub repository.
Short project report.  
---
### 👨‍💻 Project Status

Status: Working Prototype / Educational Project

The current version supports:
Resume Upload
      ↓
Text Extraction
      ↓
Text Cleaning
      ↓
Skill Extraction
      ↓
Job Matching
      ↓
Match Score
      ↓
Skill Gap Analysis
      ↓
Learning Roadmap
      ↓
PDF Analysis Report
      ↓
Download Report
---

### 📜 License
This project is developed for educational and academic purposes.
---