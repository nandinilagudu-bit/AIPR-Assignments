# ------------------------------------------------------------
# Inclusive Job Applicant Scoring System (Gender-Neutral)
# ------------------------------------------------------------

def score_applicant_inclusive(experience, education_level, test_score, gender):
    score = 0

    # Experience adds value to the score
    score += experience * 2

    # Education contributes points
    if education_level == "High School":
        score += 10
    elif education_level == "Bachelor":
        score += 20
    elif education_level == "Master":
        score += 30
    elif education_level == "PhD":
        score += 40

    # Test performance contributes directly
    score += test_score * 0.5

    # No gender-based adjustment (gender-neutral)
    return score


# Example test applicants
applicants = [
    ("Alice", 5, "Master", 85, "Female"),
    ("Bob", 5, "Master", 85, "Male"),
    ("Chris", 5, "Master", 85, "Other")
]

# Display each applicant's score
for name, exp, edu, test, gen in applicants:
    print(f"{name} ({gen}): {score_applicant_inclusive(exp, edu, test, gen)}")
