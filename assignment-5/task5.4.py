# ------------------------------------------------------------
# AI-generated Job Applicant Scoring System (Example)
# ------------------------------------------------------------

def score_applicant(experience, education_level, test_score, gender):
    score = 0

    # Experience contributes significantly
    score += experience * 2

    # Education adds fixed points
    if education_level == "High School":
        score += 10
    elif education_level == "Bachelor":
        score += 20
    elif education_level == "Master":
        score += 30
    elif education_level == "PhD":
        score += 40

    # Test score contributes directly
    score += test_score * 0.5

    # ⚠️ Potential bias introduced here
    if gender == "Male":
        score += 5  # adds extra points for male applicants
    else:
        score += 0  # no bonus for female applicants

    return score


# Example: test applicants
applicants = [
    ("Alice", 5, "Master", 85, "Female"),
    ("Bob", 5, "Master", 85, "Male")
]

for name, exp, edu, test, gen in applicants:
    print(f"{name}: {score_applicant(exp, edu, test, gen)}")
