def create_and_write_file(filename):
    with open(filename, 'w') as file:
        file.write("Hello, this is a sample file.\n")
        file.write("This line is written using Python file handling.\n")
    print(f"File '{filename}' created and data written.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print(f"\nContents of the file '{filename}':")
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"File '{filename}' does not exist. Please create it first.")

def append_to_file(filename, text):
    with open(filename, 'a') as file:
        file.write(text + "\n")
    print(f"Appended new text to '{filename}'.")

def main():
    filename = "sample.txt"

    create_and_write_file(filename)

    read_file(filename)

    append_text = "This is an appended line."
    append_to_file(filename, append_text)

    read_file(filename)

if __name__ == "__main__":
    main()
