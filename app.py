import streamlit as st
from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)
from reportlab.lib.styles import getSampleStyleSheet

from resume_parser import extract_resume_text
from text_cleaner import clean_text
from skill_extractor import load_skills, extract_skills
from job_matcher import load_job_roles, match_jobs
from roadmap_generator import generate_roadmap


# =====================================
# Generate PDF Resume Analysis Report
# =====================================
def generate_pdf_report(resume_skills, results):

    buffer = BytesIO()

    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(
        Paragraph(
            "AI Resume Analysis Report",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 20))


    # Extracted Skills
    story.append(
        Paragraph(
            "Extracted Skills",
            styles["Heading2"]
        )
    )

    if resume_skills:
        story.append(
            Paragraph(
                ", ".join(resume_skills),
                styles["Normal"]
            )
        )
    else:
        story.append(
            Paragraph(
                "No skills detected.",
                styles["Normal"]
            )
        )

    story.append(Spacer(1, 20))


    # Job Analysis
    story.append(
        Paragraph(
            "Job Role Analysis",
            styles["Heading2"]
        )
    )

    for result in results:

        # Job Role
        story.append(
            Paragraph(
                f"<b>{result['job_role']}</b>",
                styles["Heading3"]
            )
        )

        # Match Percentage
        story.append(
            Paragraph(
                f"<b>Match Percentage:</b> "
                f"{result['match_percentage']}%",
                styles["Normal"]
            )
        )

        # Matched Skills
        matched_skills = result["matched_skills"]

        story.append(
            Paragraph(
                "<b>Matched Skills:</b> "
                + (
                    ", ".join(matched_skills)
                    if matched_skills
                    else "None"
                ),
                styles["Normal"]
            )
        )

        # Missing Skills
        missing_skills = result["missing_skills"]

        story.append(
            Paragraph(
                "<b>Missing Skills:</b> "
                + (
                    ", ".join(missing_skills)
                    if missing_skills
                    else "None"
                ),
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 10))


        # Learning Roadmap
        roadmap = generate_roadmap(missing_skills)

        story.append(
            Paragraph(
                "<b>Learning Roadmap:</b>",
                styles["Heading3"]
            )
        )

        if roadmap:

            for index, step in enumerate(
                roadmap,
                start=1
            ):

                story.append(
                    Paragraph(
                        f"<b>Step {index}: "
                        f"{step['skill']}</b>",
                        styles["Normal"]
                    )
                )

                story.append(
                    Paragraph(
                        step["topic"],
                        styles["Normal"]
                    )
                )

        else:

            story.append(
                Paragraph(
                    "You already have all the required skills "
                    "for this role.",
                    styles["Normal"]
                )
            )

        story.append(Spacer(1, 20))


    # Disclaimer
    story.append(
        Paragraph(
            "This report is generated for educational and "
            "career guidance purposes.",
            styles["Italic"]
        )
    )


    # Build PDF
    doc.build(story)

    buffer.seek(0)

    return buffer


# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)


# -----------------------------
# Title
# -----------------------------
st.title("📄 AI Resume Analyzer")

st.write(
    "Upload your resume and discover matching job roles, "
    "skills, and a personalized learning roadmap."
)


# -----------------------------
# Load Skills and Job Roles
# -----------------------------
skills = load_skills()
jobs = load_job_roles()


# -----------------------------
# Resume Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume",
    type=["pdf", "docx"]
)


# -----------------------------
# Process Resume
# -----------------------------
if uploaded_file is not None:

    # Extract text from resume
    resume_text = extract_resume_text(uploaded_file)

    # Clean extracted text
    cleaned_text = clean_text(resume_text)

    # Extract skills from resume
    resume_skills = extract_skills(cleaned_text, skills)

    # Match resume skills with job roles
    results = match_jobs(resume_skills, jobs)


    # =============================
    # Extracted Skills
    # =============================
    st.subheader("🔍 Extracted Skills")

    if resume_skills:
        st.write(", ".join(resume_skills))
    else:
        st.warning("No skills were detected from the resume.")


    # =============================
    # Job Role Matches
    # =============================
    st.subheader("💼 Job Role Matches")

    if results:

        # Loop through every job role
        for result in results:

            # Job role name
            st.write(f"## 💼 {result['job_role']}")

            # Match percentage
            st.progress(int(result["match_percentage"]))

            st.write(
                f"**Match Percentage: {result['match_percentage']}%**"
            )

            # Matched skills
            matched_skills = result["matched_skills"]

            if matched_skills:
                st.write(
                    "**Matched Skills:** "
                    + ", ".join(matched_skills)
                )
            else:
                st.write("**Matched Skills:** None")


            # Missing skills
            missing_skills = result["missing_skills"]

            if missing_skills:
                st.write(
                    "**Missing Skills:** "
                    + ", ".join(missing_skills)
                )
            else:
                st.write("**Missing Skills:** None")


            st.divider()


            # =============================
            # Learning Roadmap
            # =============================
            roadmap = generate_roadmap(missing_skills)

            st.subheader(
                f"🗺️ Learning Roadmap for {result['job_role']}"
            )


            if roadmap:

                for index, step in enumerate(roadmap, start=1):

                    st.write(
                        f"### Step {index}: {step['skill']}"
                    )

                    st.write(step["topic"])

                    st.divider()

            else:

                st.success(
                    "🎉 You already have all the required skills "
                    "for this role!"
                )


            # Separate next job role
            st.markdown("---")


        # =============================
        # Download PDF Report
        # =============================
        st.subheader("📥 Download Your Analysis")

        pdf_report = generate_pdf_report(
            resume_skills,
            results
        )

        st.download_button(
            label="📄 Download Resume Analysis Report",
            data=pdf_report,
            file_name="resume_analysis_report.pdf",
            mime="application/pdf"
        )


    else:
        st.warning("No matching job roles were found.")