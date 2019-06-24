import turtle

t = turtle.Turtle()
t.shape('turtle');t.color('green')
t.left(90)

def y(t, level) : 
    if level == 0 :
        return
    t.fd(100)
    t.rt(30)
    y(t, level - 1)
    t.left(60)
    y(t, level - 1)
    t.right(30)
    t.backward(100)

y(t, 5)
