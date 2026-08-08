# Resume Parser & Analyzer

Extracts structured information — email, phone number, mentioned years of experience, and matched skills — from raw resume text using regex pattern matching and a built-in skills keyword list.

## How It Works
1. **Email** is found using a regex pattern matching standard email address formats.
2. **Phone number** is found using a flexible regex pattern covering common formats (with/without country code, dashes, spaces, or parentheses).
3. **Years of experience** is extracted from phrases like "5 years of experience" or "5+ yrs experience" using a targeted regex.
4. **Skills** are detected by checking the resume text against a built-in list of ~35 common technical and soft skills.

## Requirements
- Python 3.x (standard library only — no installs needed)

Paste resume text (works best as a single line for this demo) and press Enter. Type `quit` to exit.

## Notes & Limitations
- This is a regex/keyword-based parser — it won't understand resumes with unconventional formatting, and the skills list is a fixed set (~35 skills) rather than an exhaustive taxonomy.
- Multi-line resume text (e.g. pasted directly from a PDF) may need to be flattened to a single line first for best results in this simple CLI demo.

## Possible Extensions
- Add support for reading directly from PDF/DOCX resume files.
- Expand the skills list or load it from an external, categorized file (technical vs. soft skills).
- Extract additional fields: education, job titles, certifications.
