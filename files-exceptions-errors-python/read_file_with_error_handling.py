# Task 1: Read a File and Handle Errors

def read_file(filename):
    """Reads and prints content of a text file, handling file not found error."""
    try:
        with open(filename, 'r') as file:
            print("\n--- File Content ---")
            for line in file:
                print(line.strip())  # strip() removes newline characters
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Calling the function
read_file('sample.txt')
