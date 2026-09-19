from pypdf import PdfReader
from docx import Document


def extract_text_from_pdf(uploaded_file):
    """Extract text from a PDF resume."""
    reader = PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:
        extracted_text = page.extract_text()

        if extracted_text:
            text += extracted_text + "\n"

    return text


def extract_text_from_docx(uploaded_file):
    """Extract text from a DOCX resume."""
    document = Document(uploaded_file)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text


def extract_resume_text(uploaded_file):
    """Detect file type and extract resume text."""

    file_name = uploaded_file.name.lower()

    if file_name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)

    elif file_name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)

    else:
        return "Unsupported file format. Please upload PDF or DOCX."