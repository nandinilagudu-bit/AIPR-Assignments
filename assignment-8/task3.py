import string

def is_sentence_palindrome(sentence):
    if not isinstance(sentence, str):
        return "Invalid input"
    
    cleaned = "".join(
        ch.lower() for ch in sentence
        if ch.isalnum()
    )
    return cleaned == cleaned[::-1]


# Test the function
tests = [
    "A man a plan a canal Panama",
    "No lemon, no melon",
    "Hello world",
    "Was it a car or a cat I saw?",
    "Madam In Eden, I'm Adam",
    12321,
    "",
    "@#$%^",
]

for t in tests:
    print(f"{t} -> {is_sentence_palindrome(t)}")
