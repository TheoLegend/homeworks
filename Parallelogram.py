import turtle

t = turtle.Turtle()

for _ in range(2):
    t.forward(150)  # long side
    t.left(60)
    t.forward(80)   # short side
    t.left(120)

turtle.done()
