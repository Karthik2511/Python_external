def is_vowel(char):
    # Define a set of vowels
    vowels = 'A,E,I,O,U,a,e,i,o,u'
    return char in vowels

# Get user input
char = input("Enter an alphabet: ")

# Check if the input is a single alphabet
if len(char) == 1 and char.isalpha():
    if is_vowel(char):
        print(f"'{char}' is a vowel.")
    else:
        print(f"'{char}' is not a vowel.")
else:
    print("Please enter a single alphabet.")