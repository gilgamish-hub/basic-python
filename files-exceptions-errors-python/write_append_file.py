# Task 2: Write and Append Data to a File

def write_and_append_file(filename):
    """Writes user input to a file, appends more data, then reads and displays final content."""
    
    # Step 1: Write to file
    data = input("Enter some text to write into the file: ")
    with open(filename, 'w') as file:
        file.write(data + '\n')
    print(f"Data written to {filename}")

    # Step 2: Append data
    more_data = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(more_data + '\n')
    print("Additional data appended successfully.")

    # Step 3: Read and display content
    print("\n--- Final File Content ---")
    with open(filename, 'r') as file:
        print(file.read())


# Calling the function
write_and_append_file('output.txt')
