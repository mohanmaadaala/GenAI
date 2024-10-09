# Specify the path to the file (use the full path or relative path)
file_path = r"C:\Training\Testing.txt"  # For Windows
# Or
# file_path = "/Users/YourUsername/Documents/example.txt"   # For macOS/Linux

# Open the file in read mode
try:
    with open(file_path, "r") as file:
        # Read and print the file's contents
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
