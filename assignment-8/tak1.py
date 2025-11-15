import re

def is_valid_email(email):
    # Rule 1: Must contain exactly one @
    if email.count("@") != 1:
        return False

    # Split local and domain parts
    local, domain = email.split("@")

    # Rule 2: Cannot start or end with special characters in local part
    if not local or not domain:
        return False
    
    if not local[0].isalnum() or not local[-1].isalnum():
        return False

    # Rule 3: Domain must contain dot
    if "." not in domain:
        return False

    # Cannot start or end with dot
    if domain[0] == "." or domain[-1] == ".":
        return False

    # No consecutive dots in domain
    if ".." in domain:
        return False

    # Basic regex for valid characters
    pattern = r'^[A-Za-z0-9._\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,}$'
    return bool(re.match(pattern, email))
test_emails = [
    "user@example.com",
    "john.doe@domain.co",
    "a_b-c@sub.domain.com",
    "name123@domain.org",
    "userexample.com",
    "user@domaincom",
    "us@er@domain.com",
    ".user@example.com",
    "user.@example.com",
    "@user.com",
    "user@domain.com.",
    "user@.com",
    "user@domain.",
    "user@domain..com"
]

for email in test_emails:
    print(f"{email:25} -> {is_valid_email(email)}")
