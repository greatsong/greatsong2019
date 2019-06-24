import turtle

t = turtle.Turtle()
t.shape('turtle');t.color('green')

def s(t, length, level) :
    t.speed(0)
    if level == 0 :
        return
    for i in range(3) :
        s(t, length / 2, level - 1)
        t.fd(length)
        t.rt(120)
        
s(t, 100, 5)
