import random

def guessing_game():
    print("=== Number Guessing Game ===")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    target = random.randint(lower, upper)

    max_attempts = input("Enter maximum number of attempts (default: 7): ")
    max_attempts = int(max_attempts) if max_attempts.strip() != '' else 7

    attempts = 0

    print(f"\nGuess the number between {lower} and {upper}!")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < target:
                print("Too low! Try a higher number.")
            elif guess > target:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Correct! The number was {target}. You guessed it in {attempts} attempts.\n")
                break

            print(f"Attempts left: {max_attempts - attempts}")

        except ValueError:
            print("Please enter a valid integer.")

    else:  # ran out of attempts
        print(f"\n🚫 Game Over! The number was {target}.\n")

def main():
    while True:
        guessing_game()
        play_again = input("Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
