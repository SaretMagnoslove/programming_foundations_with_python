import turtle

window = turtle.Screen()
window.bgcolor("red")

david = turtle.Turtle()
david.color("green")
david.speed(300)


def drawSquare():
    for i in range(4):
        david.forward(100)
        david.right(90)


def drawCircle():
    david.circle(100)


def drawTriange():
    for i in range(3):
        david.forward(100)
        david.left(120)


for i in range(36):
    drawSquare()
    drawTriange()
    drawCircle()
    david.right(10)

window.exitonclick()
