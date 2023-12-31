import turtle

t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('lightyellow')



t.penup()
t.goto(-150, -100)
t.pendown()
t.pensize(2)
t.color('black', 'pink')
t.begin_fill()


for i in range(3):
    t.forward(300)
    t.left(90)
    t.forward(125)
    t.left(90)


t.end_fill()
t.forward(300)
t.left(90)


# lingkaran
t.color('black', 'yellow')
t.begin_fill()
t.circle(50, 180)
for i in range(2):
    t.left(180)
    t.circle(50, 180)
t.end_fill()


t.left(90)
t.forward(70)
t.right(90)


t.color('black', 'pink')
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(90)
    t.forward(160)
    t.left(90)
t.end_fill() 


# lingkaran
t.color('black', 'yellow')
t.begin_fill()
for i in range(2):
    t.circle(40, 180)
    t.left(180)
t.end_fill()


t.right(90)
t.forward(160)
t.left(90)
t.forward(100)
t.right(90)
t.forward(70)


# Happy Birthday
t.color('black')
t.penup()
t.goto(0, -175)
t.write('HAPPY BIRTHDAY NCIN', align='center', font="Times 35 normal")

turtle.done()

