def fibonacci_sequence(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

def main():
    print("=== Fibonacci Sequence Generator ===")
    try:
        n = int(input("Enter the number of terms to generate: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            seq = fibonacci_sequence(n)
            print(f"First {n} terms of the Fibonacci sequence:")
            print(seq)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
