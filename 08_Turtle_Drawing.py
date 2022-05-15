import turtle

arrow = turtle.Turtle()


# arrow.color('red')


# x = 100
# y = 0
# while True:
#     x -= 1
#     if y < 20:
#         arrow.forward(x)
#         arrow.left(90)
#         y += 1
#         continue
#     break

# arrow.penup()
# arrow.forward(250)
# arrow.right(90)
# arrow.forward(10)
# arrow.right(180)
# arrow.pendown()

# arrow.color('blue')
# x = 100
# y = 0
# while True:
#     x -= 1
#     if y < 20:
#         arrow.forward(x)
#         arrow.left(90)
#         y += 1
#         continue
#     break

# arrow.penup()
# arrow.forward(150)
# arrow.right(90)
# arrow.forward(10)
# arrow.right(180)
# arrow.pendown()

# # Right eyebrow -----
# arrow.color('orange')
# arrow.begin_fill()
# arrow.forward(100)
# arrow.left(90)
# arrow.forward(20)
# arrow.left(90)
# arrow.forward(100)
# arrow.left(90)
# arrow.forward(20)
# arrow.left(90)
# arrow.end_fill()

# arrow.penup()
# arrow.forward(200)
# arrow.pendown()

# # Left eyebrow -----
# arrow.color('pink')
# arrow.begin_fill()
# arrow.left(20)
# arrow.forward(100)
# arrow.left(90)
# arrow.forward(20)
# arrow.left(90)
# arrow.forward(100)
# arrow.left(90)
# arrow.forward(20)
# arrow.left(90)
# arrow.end_fill()

# arrow.penup()
# arrow.setheading(270)
# arrow.forward(100)
# arrow.setheading(90)
# arrow.pendown()

# # Left eye -----
# arrow.color('black')
# arrow.begin_fill()
# arrow.left(90)
# arrow.forward(30)
# arrow.left(90)
# arrow.forward(40)
# arrow.left(90)
# arrow.forward(30)
# arrow.left(90)
# arrow.forward(40)
# arrow.left(90)
# arrow.end_fill()


# # Eyeball shine LEFT ----
# arrow.penup()
# arrow.forward(25)
# arrow.left(90)
# arrow.forward(35)
# arrow.pendown()

# arrow.color('white')
# arrow.begin_fill()
# arrow.left(90)
# arrow.forward(10)
# arrow.left(90)
# arrow.forward(5)
# arrow.left(90)
# arrow.forward(10)
# arrow.left(90)
# arrow.forward(5)
# arrow.left(90)
# arrow.end_fill()

# # Right eyeball -----
# arrow.penup()
# arrow.forward(150)
# arrow.right(90)
# arrow.forward(5)
# arrow.pendown()

# arrow.color('black')
# arrow.begin_fill()
# arrow.left(90)
# arrow.forward(30)
# arrow.left(90)
# arrow.forward(40)
# arrow.left(90)
# arrow.forward(30)
# arrow.left(90)
# arrow.forward(40)
# arrow.left(90)
# arrow.end_fill()

# # Eyeball shine RIGHT ----
# arrow.penup()
# arrow.forward(15)
# arrow.left(90)
# arrow.forward(10)
# arrow.pendown()

# arrow.color('white')
# arrow.begin_fill()
# arrow.left(90)
# arrow.forward(10)
# arrow.left(90)
# arrow.forward(5)
# arrow.left(90)
# arrow.forward(10)
# arrow.left(90)
# arrow.forward(5)
# arrow.left(90)
# arrow.end_fill()

# # Mouth ----
# arrow.penup()
# arrow.left(90)
# arrow.forward(130)
# arrow.left(90)
# arrow.forward(20)
# arrow.pendown()

# arrow.color('black')
# arrow.begin_fill()
# arrow.left(90)
# arrow.forward(25)
# arrow.left(90)
# arrow.forward(20)
# arrow.left(90)
# arrow.forward(25)
# arrow.left(90)
# arrow.forward(20)
# arrow.left(90)
# arrow.end_fill()

# Head -----
arrow.penup()
arrow.right(90)
arrow.forward(100)
arrow.setheading(90)
arrow.forward(25)
arrow.setheading(0)
arrow.pendown()

arrow.color('black')
arrow.left(60)
arrow.forward(100)
arrow.left(30)
arrow.forward(100)
arrow.left(10)
arrow.forward(80)

# Hair -----
angle = 0
step = 0
z = 0
while True:
    arrow.left(angle)
    arrow.forward(step)
    if z < 12:
        angle += 2
        step += 10
        z += 1
        continue
    break

arrow.left(135)
arrow.forward(150)


# Face top -----

arrow.setheading(270)
arrow.right(45)

angle = 0
step = 0
z = 0
while True:
    arrow.left(angle)
    arrow.forward(step)
    if z < 7:
        angle += 3
        step += 5
        z += 1
        continue
    break

# Face middle -----
arrow.setheading(270)
arrow.right(10)

angle = 0
step = 0
z = 0
while True:
    arrow.left(angle)
    arrow.forward(step)
    if z < 6:
        angle += 2
        step += 10
        z += 1
        continue
    break







    











turtle.done()