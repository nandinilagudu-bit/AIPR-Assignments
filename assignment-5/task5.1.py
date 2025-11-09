import re
from typing import List, Tuple


# ------------------------------------------------------------
# "AI-generated" login system (intentionally naive for analysis)
# ------------------------------------------------------------
ai_generated_login_code = """
# AI-generated login system (example)
users = {
    "admin": "admin123",
    "user": "password"
}

def login(username, password):
    if username in users and users[username] == password:
        print("Login successful")
        return True
    else:
        print("Invalid credentials")
        return False

if __name__ == "__main__":
    u = input("Username: ")
    p = input("Password: ")  # Password collected in plain text
    if login(u, p):
        print("Welcome!")
"""


def analyze_code_security(code: str) -> List[Tuple[str, str]]:
    """Return list of (severity, finding) for insecure patterns commonly seen in AI-generated auth code."""
    findings: List[Tuple[str, str]] = []

    checks = [
        (r"users\s*=\s*\{[\s\S]*?\}",
         "HIGH",
         "Hardcoded credential store detected (in-memory dictionary)."),
        (r"(?i)(password|passwd|pwd)\s*[:=]\s*['\"]", 
         "HIGH", 
         "Hardcoded password literal detected."),
        (r"\binput\(\s*['\"]Password", 
         "MEDIUM", 
         "Reads password via input(); use getpass to avoid echoing."),
        (r"==\s*password\b|\bpassword\s*==", 
         "MEDIUM", 
         "Plain-text password equality comparison detected."),
        (r"\b(md5|sha1)\(", 
         "MEDIUM", 
         "Insecure hashing function (MD5/SHA1) detected for passwords."),
        (r"debug\s*=\s*True|app\.run\(.*debug\s*=\s*True", 
         "LOW", 
         "Debug mode enabled in production context."),
        (r"verify\s*=\s*False", 
         "HIGH", 
         "TLS certificate verification disabled in HTTP client."),
        (r"http://", 
         "MEDIUM", 
         "Plain HTTP URL detected; prefer HTTPS."),
        (r"(?i)(secret|api_key|token)\s*=\s*['\"]", 
         "MEDIUM", 
         "Hardcoded secret/token detected."),
    ]

    for pattern, severity, message in checks:
        if re.search(pattern, code):
            findings.append((severity, message))

    return findings


def print_report(code: str) -> None:
    print("Generated login system (from AI tool example):\n")
    print(code)
    print("\nSecurity analysis:\n-------------------")
    results = analyze_code_security(code)
    if not results:
        print("No obvious insecure patterns detected.")
        return
    for severity, message in results:
        print(f"[{severity}] {message}")

    high_count = sum(1 for sev, _ in results if sev == "HIGH")
    if high_count > 0:
        print("\nVerdict: INSECURE — hardcoded credentials or risky logic present.")
    else:
        print("\nVerdict: POTENTIALLY INSECURE — issues found; review and remediate.")

    print("\nRecommendations:")
    print("- Store user credentials in a database with strong password hashing (bcrypt/Argon2).")
    print("- Never hardcode usernames/passwords, secrets, or tokens in source code.")
    print("- Use getpass for password input in CLI tools to avoid echoing.")
    print("- Avoid plain equality checks of passwords; use a password hashing library.")
    print("- Disable debug mode and use HTTPS for transport.")


if __name__ == "__main__":
    print_report(ai_generated_login_code)


