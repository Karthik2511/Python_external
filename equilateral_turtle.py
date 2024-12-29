import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle object
t = turtle.Turtle()

# Set the turtle speed
t.speed(2)

# Draw an equilateral triangle
for _ in range(3):
    t.forward(100)  # Move turtle forward by 100 units
    t.left(120)     # Turn turtle by 120 degrees

# Hide the turtle
t.hideturtle()

# Finish
turtle.done()
