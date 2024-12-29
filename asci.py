char = input("Enter a character: ")

if len(char) == 1:
    print(f"ASCII value: {ord(char)}")
    print(f"Uppercase: {char.upper()}" if char.islower() else f"Lowercase: {char.lower()}")
else:
    print("Invalid input. Please enter a single character.")
