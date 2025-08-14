# Task 1: String Reversal Program

def reverse_string(text):
    """Function to reverse a given string."""
    return text[::-1]

# Ask the user for input
user_input = input("Enter a string: ")

# Process and output
reversed_text = reverse_string(user_input)

print("Reversed string:", reversed_text)
