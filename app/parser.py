import re
import spacy
from pyresparser import ResumeParser
import tempfile

nlp = spacy.load("en_core_web_sm")

def parse_resume(file_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(file_bytes)
        tmp_path = tmp.name

    parsed = ResumeParser(tmp_path).get_extracted_data()
    return {
        "name": parsed.get("name", ""),
        "email": parsed.get("email", ""),
        "skills": parsed.get("skills", []),
        "education": parsed.get("degree", []),
        "experience": parsed.get("total_experience", 0)
    }
