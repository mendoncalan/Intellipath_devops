# 1. CREATE and write to the file
# The 'w' mode opens a file for writing. It creates the file if it does not exist.
with open(file_name, "w") as file:
    file.write("Hello! This file was created using Python.\n")
    file.write("This is the second line of text.")

print(f"'{file_name}' has been created and populated.\n")


# 2. OPEN and read the file
# The 'r' mode opens an existing file for reading.
with open(file_name, "r") as file:
    # Read the entire content of the file
    content = file.read()
    
    # Display the content in the console
    print("--- File Contents ---")
    print(content)
