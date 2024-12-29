from datetime import datetime

# Input the current age of the user
current_age = int(input("Enter your current age: "))

# Get the current year
current_year = datetime.now().year

# Calculate the year when the user will turn 50
year_when_50 = current_year + (50 - current_age)

print(f"You will turn 50 years old in the year: {year_when_50}")
