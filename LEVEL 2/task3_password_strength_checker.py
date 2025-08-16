import re

def check_strength(password):
    length_check = len(password) >= 8
    uppercase_check = re.search(r"[A-Z]", password)
    lowercase_check = re.search(r"[a-z]", password)
    digit_check = re.search(r"[0-9]", password)
    special_check = re.search(r"[^A-Za-z0-9]", password)

    if all([length_check, uppercase_check, lowercase_check, digit_check, special_check]):
        return "Strong"
    elif length_check and (uppercase_check or lowercase_check) and (digit_check or special_check):
        return "Medium"
    else:
        return "Weak"

def main():
    print("=== Password Strength Checker ===")
    password = input("Enter your password: ")

    strength = check_strength(password)
    print(f"Password Strength: {strength}")

    # Show feedback
    print("\nFeedback:")
    if len(password) < 8:
        print("- It should be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        print("- Add uppercase letters.")
    if not re.search(r"[a-z]", password):
        print("- Add lowercase letters.")
    if not re.search(r"[0-9]", password):
        print("- Add digits.")
    if not re.search(r"[^A-Za-z0-9]", password):
        print("- Add special characters (@, #, $, %, etc.).")

if __name__ == "__main__":
    main()
