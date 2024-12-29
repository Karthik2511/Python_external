# Function to count words and character frequencies in a file
def count_words_and_chars(file_name):
    # Open the file in read mode
    try:
        with open(file_name, 'r') as file:
            content = file.read()
            
            # Counting words
            words = content.split()
            num_words = len(words)
            
            # Counting character frequencies
            char_count = {}
            for char in content:
                if char.isalnum():  # Consider only alphanumeric characters
                    char_count[char] = char_count.get(char, 0) + 1
            
            return num_words, char_count
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return None, None

# Create and write sample content into a file
file_name = 'sample_file.txt'
sample_text = """Hello world! This is a test file.
It will be used to count words and character frequencies.
Python is fun!"""

with open(file_name, 'w') as file:
    file.write(sample_text)

# Calling the function to count words and character frequencies
num_words, char_count = count_words_and_chars(file_name)

# Displaying the results
if num_words is not None and char_count is not None:
    print(f"Number of words: {num_words}")
    print("Character frequencies:")
    for char, count in char_count.items():
        print(f"'{char}': {count}")
