import re


def clean_text(text):
    """Clean extracted resume text."""

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9+#.\s]", " ", text)

    # Replace multiple spaces with a single space
    text = re.sub(r"\s+", " ", text)

    # Remove extra spaces
    text = text.strip()

    return text