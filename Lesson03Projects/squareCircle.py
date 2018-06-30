import turtle

window = turtle.Screen()
window.bgcolor("red")

david = turtle.Turtle()
david.color("green")
david.speed(300)

def drawSquare():
    david.forward(200)
    david.right(90)

for i in range(360):
    drawSquare()
    david.right(1)

window.exitonclick()