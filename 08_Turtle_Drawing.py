import turtle

arrow = turtle.Turtle()


arrow.color('red')
arrow.begin_fill()
arrow.end_fill()


x = 100
y = 0
while True:
    x -= 1
    if y < 20:
        arrow.forward(x)
        arrow.left(90)
        y += 1
        continue
    break

arrow.penup()
arrow.forward(250)
arrow.right(90)
arrow.forward(10)
arrow.right(180)
arrow.pendown()

arrow.color('blue')
x = 100
y = 0
while True:
    x -= 1
    if y < 20:
        arrow.forward(x)
        arrow.left(90)
        y += 1
        continue
    break

arrow.penup()
arrow.forward(150)
arrow.right(90)
arrow.forward(10)
arrow.right(180)
arrow.pendown()


arrow.color('orange')
arrow.begin_fill()
arrow.forward(100)
arrow.left(90)
arrow.forward(20)
arrow.left(90)
arrow.forward(100)
arrow.left(90)
arrow.forward(20)
arrow.left(90)
arrow.end_fill()

arrow.penup()
arrow.forward(200)
arrow.pendown()

arrow.color('pink')
arrow.begin_fill()
arrow.left(20)
arrow.forward(100)
arrow.left(90)
arrow.forward(20)
arrow.left(90)
arrow.forward(100)
arrow.left(90)
arrow.forward(20)
arrow.left(90)
arrow.end_fill()

arrow.penup()
arrow.left(40)
arrow.forward(200)
arrow.pendown()

arrow.color('black')
arrow.begin_fill()
arrow.left(20)
arrow.forward(100)
arrow.left(90)
arrow.forward(20)
arrow.left(90)
arrow.forward(100)
arrow.left(90)
arrow.forward(20)
arrow.left(90)
arrow.end_fill()

    











turtle.done()