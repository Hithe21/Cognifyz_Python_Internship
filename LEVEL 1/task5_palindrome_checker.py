# Task 5: Palindrome Checker

def is_palindrome(text):
    """
    This function checks if the given text is a palindrome.
    It ignores spaces, capitalization, and punctuation.
    """
    # Remove spaces and make lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    
    # Check if it reads the same both ways
    return cleaned_text == cleaned_text[::-1]

def main():
    print("=== Palindrome Checker ===")
    user_input = input("Enter a word, sentence, or number: ")

    if is_palindrome(user_input):
        print(f"✅ '{user_input}' is a palindrome!")
    else:
        print(f"❌ '{user_input}' is NOT a palindrome.")

if __name__ == "__main__":
    main()
