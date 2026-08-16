filename = input("Enter the file name or path: ")

try:
    with open(filename, 'r') as file:
        content = file.read()
        words = content.split()
        word_count = len(words)
        
    print(f"Total word count in '{filename}': {word_count}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")