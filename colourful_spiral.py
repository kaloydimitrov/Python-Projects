import turtle
import random

# Screen
screen = turtle.Screen()
screen.bgcolor("#abfeff")

# Turtle
turtle = turtle.Turtle()
turtle.shape("circle")
turtle.speed(0)
turtle.shapesize(0.2, 0.2, 0.2)
turtle.pensize(2)

turtle.screen.title("Colourful Spiral")

colors = ["blue", "green", "red", "purple", "cyan", "yellow", "darkred", "goldenrod", "violet"]

# Main
for i in range(240):
    turtle.forward(2 + i / 4)
    turtle.left(30 - i / 12)

    random_index = random.randint(0, len(colors) - 1)
    turtle.color(colors[random_index])

# Prevents it from closing
input()