import csv


def load_job_roles(file_path="data/job_roles.csv"):
    """Load job roles and their required skills."""

    jobs = []

    with open(file_path, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            jobs.append({
                "job_role": row["job_role"],
                "required_skills": [
                    skill.strip().lower()
                    for skill in row["required_skills"].split(",")
                ]
            })

    return jobs


def calculate_match(resume_skills, required_skills):
    """Calculate the percentage match."""

    matched_skills = []

    for skill in required_skills:
        if skill in resume_skills:
            matched_skills.append(skill)

    if len(required_skills) == 0:
        return 0, matched_skills

    match_percentage = (
        len(matched_skills) / len(required_skills)
    ) * 100

    return round(match_percentage, 2), matched_skills


def match_jobs(resume_skills, jobs):
    """Match resume skills with available job roles."""

    results = []

    for job in jobs:

        percentage, matched_skills = calculate_match(
            resume_skills,
            job["required_skills"]
        )

        missing_skills = [
            skill for skill in job["required_skills"]
            if skill not in resume_skills
        ]

        results.append({
            "job_role": job["job_role"],
            "match_percentage": percentage,
            "matched_skills": matched_skills,
            "missing_skills": missing_skills
        })

    results.sort(
        key=lambda x: x["match_percentage"],
        reverse=True
    )

    return results