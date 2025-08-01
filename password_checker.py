import re
import math

print("Password Strength Checker")

weak_passwords = [
    "password", "123456", "123456789", "admin", "qwerty",
    "abc123", "iloveyou", "letmein", "monkey", "football"
]

def check_password(password):
    score = 0
    feedback = []

    length = len(password)

    if length >= 12:
        score += 2
    elif length >= 8:
        score += 1
    else:
        feedback.append("Password too short (use at least 8 characters)")

    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("No lowercase letters")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("No uppercase letters")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("No numbers")

    if re.search(r'[^a-zA-Z0-9]', password):
        score += 1
    else:
        feedback.append("No special characters (!, @, #, etc.)")

    if password.lower() in weak_passwords:
        feedback.append("This password is very common — avoid it!")
        score = 0

    charset = 0
    if re.search(r'[a-z]', password): charset += 26
    if re.search(r'[A-Z]', password): charset += 26
    if re.search(r'[0-9]', password): charset += 10
    if re.search(r'[^a-zA-Z0-9]', password): charset += 32

    entropy = round(math.log2(charset ** len(password))) if charset > 0 else 0

    return score, entropy, feedback

# Run the main program directly
print("Ready to check password strength!")
password = input("Enter a password to check: ")
score, entropy, feedback = check_password(password)

print("\nPassword Analysis:")
print("Strength Score: {}/6".format(score))
print("Estimated Entropy: {} bits".format(entropy))

if score >= 5:
    print("Strong password!")
elif score >= 3:
    print("Moderate password. Could be improved.")
else:
    print("Weak password!")

if feedback:
    print("\nSuggestions:")
    for tip in feedback:
        print(" - " + tip)
