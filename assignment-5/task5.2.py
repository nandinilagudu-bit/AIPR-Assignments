import re
from collections import defaultdict

# --- Simplified AI-generated loan approval code (for bias testing) ---
ai_generated_loan_code = """
def approve_loan(name, age, income, credit, loan, gender=None):
    if age < 18 or age > 65: return False, "Age limit"
    if credit < 600: return False, "Low credit"
    if income < loan * 0.1: return False, "Low income"
    if gender:
        if gender.lower() == "female":
            if credit < 650 or income < loan * 0.12: return False, "Stricter female check"
        elif gender.lower() == "male":
            if credit >= 600 and income >= loan * 0.08: return True, "Lenient male check"
    mnames = ["john","michael","david","james","robert"]
    fnames = ["mary","jennifer","sarah","emily","jessica"]
    name = name.lower()
    if any(n in name for n in mnames):
        if credit >= 620 and income >= loan * 0.09: return True, "Male pattern approval"
    if any(n in name for n in fnames):
        if credit >= 680 and income >= loan * 0.13: return True, "Female pattern approval"
    if credit >= 640 and income >= loan * 0.1: return True, "Standard approval"
    return False, "Not approved"
"""

# --- Bias detection (regex-based) ---
def detect_bias_in_code(code):
    checks = {
        "gender_bias": r"gender.*(male|female)",
        "name_bias": r"(male|female)_names",
        "stricter_for_female": r"female.*credit.*>|female.*income",
    }
    return {k: bool(re.search(v, code, re.I)) for k, v in checks.items()}

# --- Test loan logic with variations ---
def run_tests():
    exec_globals = {}
    exec(ai_generated_loan_code, exec_globals)
    approve_loan = exec_globals["approve_loan"]
    names = [
        ("John Smith","male"), ("Mary Johnson","female"),
        ("Michael Brown","male"), ("Sarah Miller","female"),
        ("Alex Taylor",None)
    ]
    profile = dict(age=35, income=50000, credit=630, loan=300000)
    results = [{**profile, "name": n, "gender": g, 
                "approved": approve_loan(n, **profile, gender=g)[0]} for n,g in names]
    return results

# --- Analyze bias by approval rate ---
def analyze(results):
    groups = defaultdict(list)
    for r in results:
        groups[r["gender"] or "unknown"].append(r)
    rates = {g: sum(c["approved"] for c in lst)/len(lst)*100 for g,lst in groups.items()}
    return rates

# --- Final report ---
def print_bias_report():
    print("=== Loan Bias Analysis ===\n")
    print("Detected Code Bias:", detect_bias_in_code(ai_generated_loan_code))
    results = run_tests()
    rates = analyze(results)
    print("\nApproval Rates by Gender:")
    for g, r in rates.items():
        print(f"  {g.capitalize():<8} -> {r:.1f}%")
    diff = abs(rates.get("male",0) - rates.get("female",0))
    print("\nVerdict:", "⚠️ Bias Detected" if diff > 10 else "✅ Fair (no major gap)")
    print("\nRecommendation: Remove gender/name conditions, use financial data only.")

if __name__ == "__main__":
    print_bias_report()
