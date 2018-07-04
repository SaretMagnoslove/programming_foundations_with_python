import turtle


def drawShapes():
    window = turtle.Screen()
    window.bgcolor("red")

    brad = turtle.Turtle()
    brad.shape('turtle')
    brad.color('green')
    brad.speed(2)

    for i in range(4):
        brad.forward(100)
        brad.right(90)

    angie = turtle.Turtle()
    angie.shape('arrow')
    angie.color('blue')
    angie.circle(100)

    pete = turtle.Turtle()
    pete.shape("classic")
    pete.color("black")

    for i in range(3):
        pete.forward(100)
        pete.left(120)

    window.exitonclick()


drawShapes()
