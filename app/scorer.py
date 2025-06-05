from app.utils import check_skill_gaps

def generate_feedback(resume_data):
    required_skills = ["Python", "Machine Learning", "SQL", "NLP"]
    score = 50  # base score

    skills = resume_data.get("skills", [])
    experience = resume_data.get("experience", 0)

    matched_skills = [s for s in skills if s in required_skills]
    skill_gap = check_skill_gaps(skills, required_skills)

    if experience > 2:
        score += 20
    score += len(matched_skills) * 5

    feedback = {
        "Skill Gaps": skill_gap,
        "Experience Bonus": experience > 2,
        "Matched Skills": matched_skills
    }
    return score, feedback
