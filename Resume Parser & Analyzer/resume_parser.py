"""
Resume Parser & Analyzer
-----------------------------
Extracts structured information (email, phone number, skills, years of
experience mentions) from raw resume text using regex pattern matching
and a built-in skills keyword list — no external downloads needed.

"""

import re

SKILLS_LIST = [
    "python", "java", "javascript", "typescript", "c++", "c#", "sql",
    "html", "css", "react", "angular", "vue", "node.js", "django",
    "flask", "machine learning", "deep learning", "nlp", "tensorflow",
    "pytorch", "pandas", "numpy", "scikit-learn", "aws", "azure", "gcp",
    "docker", "kubernetes", "git", "linux", "excel", "power bi", "tableau",
    "communication", "leadership", "project management", "agile", "scrum",
]

EMAIL_PATTERN = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_PATTERN = re.compile(r"(?:\+?\d{1,3}[-.\s]?)?\(?\d{2,4}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}")
EXPERIENCE_PATTERN = re.compile(r"(\d+)\+?\s*(?:years?|yrs?)\s+(?:of\s+)?experience", re.IGNORECASE)


def extract_email(text):
    match = EMAIL_PATTERN.search(text)
    return match.group() if match else None


def extract_phone(text):
    match = PHONE_PATTERN.search(text)
    return match.group() if match else None


def extract_skills(text):
    text_lower = text.lower()
    return [skill for skill in SKILLS_LIST if skill in text_lower]


def extract_experience(text):
    matches = EXPERIENCE_PATTERN.findall(text)
    return matches[0] + " years" if matches else "Not mentioned"


def parse_resume(text):
    return {
        "Email": extract_email(text) or "Not found",
        "Phone": extract_phone(text) or "Not found",
        "Experience": extract_experience(text),
        "Skills": extract_skills(text) or ["None detected"],
    }


def main():
    print("Resume Parser & Analyzer")
    print("Paste resume text (single line works best for this demo), then press Enter.")
    print("Type 'quit' to exit.\n")

    while True:
        text = input("> ").strip()
        if text.lower() == "quit":
            break
        if not text:
            continue

        result = parse_resume(text)
        print()
        for field, value in result.items():
            if isinstance(value, list):
                print(f"  {field}: {', '.join(value)}")
            else:
                print(f"  {field}: {value}")
        print()


if __name__ == "__main__":
    main()
