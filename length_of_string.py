# Function to calculate length of a string
def string_length(s):
    count = 0
    for _ in s: count += 1
    return count

# Input and output
print(string_length(input("Enter a string: ")))
