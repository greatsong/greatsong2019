import turtle

t = turtle.Turtle()
t.shape('turtle');t.color('green')


def circle(t) : 
    for i in range(360) :
        t.forward(1);t.left(1)

circle(t)
