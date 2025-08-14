import re

def validate_email(email):
    """
    Validates an email address using regex.
    
    The regex used checks for:
    - A local part containing word characters, dots, or hyphens
    - An '@' symbol
    - A domain name containing letters, digits, or hyphens
    - A dot followed by a domain extension with at least 2 letters
    """
    pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(pattern, email):
        return True
    else:
        return False

def main():
    email = input("Enter an email address to validate: ")
    if validate_email(email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is not a valid email address.")

if __name__ == "__main__":
    main()
