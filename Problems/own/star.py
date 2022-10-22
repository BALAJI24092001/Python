import turtle as t
t.bgcolor("black")
color = ("pink", "orange", "white")
s = t.Turtle()
n = t.Screen()
n.setup(width=800, height=650)
t.tracer(2)
c = 0

for i in range(300):
    s.forward(2*i)
    s.right(150)
    s.color(color[c])
    if c == 2:
        c = 0
    else:
        c += 1

s.hideturtle()
t.done()
