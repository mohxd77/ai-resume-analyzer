def load_skills(file_path="data/skill_dictionary.csv"):
    """Load skills from the skill dictionary CSV file."""

    skills = []

    with open(file_path, "r", encoding="utf-8") as file:
        next(file)  # Skip header

        for line in file:
            skill = line.strip().lower()

            if skill:
                skills.append(skill)

    return skills


def extract_skills(text, skills):
    """Extract skills found in the resume text."""

    text = text.lower()

    found_skills = []

    for skill in skills:
        if skill in text:
            found_skills.append(skill)

    return found_skills