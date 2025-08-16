def number_guesser():
    print("=== Number Guesser (Computer tries to guess your number) ===")
    lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))

    print(f"Think of a number between {lower} and {upper}. I will try to guess it!")
    input("Press Enter when ready...")

    attempts = 0

    while lower <= upper:
        guess = (lower + upper) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        feedback = input("Is it correct (c), too high (h), or too low (l)? ").strip().lower()

        if feedback == 'c':
            print(f"🎉 Yay! I guessed your number {guess} in {attempts} attempts.")
            break
        elif feedback == 'h':
            upper = guess - 1
        elif feedback == 'l':
            lower = guess + 1
        else:
            print("Please enter 'c' for correct, 'h' for too high, or 'l' for too low.")

    else:
        print("\n💥 Something went wrong. Did you change your number?")

if __name__ == "__main__":
    number_guesser()
