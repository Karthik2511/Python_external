# Function to check if user can vote
def can_vote(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Main Program
try:
    age = int(input("Enter your age: "))
    if age < 0:
        print("Age cannot be negative. Please enter a valid age.")
    else:
        result = can_vote(age)
        print(result)
except ValueError:
    print("Invalid input. Please enter a valid integer for age.")
