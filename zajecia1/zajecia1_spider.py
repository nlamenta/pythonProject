import turtle

turtle.speed(13)  # Painting speed control
turtle.bgcolor("#990000")
turtle.pensize(10)
turtle.penup()
turtle.goto(0, 50)
turtle.pendown()
turtle.circle(-120)
turtle.penup()
turtle.circle(-120, -60)
turtle.pendown()
turtle.pensize(5)
turtle.right(50)
turtle.circle(70, 55)
turtle.right(85)
turtle.circle(75, 58)
turtle.right(90)
turtle.circle(70, 55)
turtle.right(90)
turtle.circle(70, 58)

# body
turtle.penup()
turtle.pensize(10)
turtle.goto(80, 15)
turtle.pendown()
turtle.seth(92)
turtle.fd(135)
turtle.seth(125)
turtle.circle(30, 135)
turtle.seth(190)
turtle.fd(50)
turtle.seth(125)
turtle.circle(30, 135)
turtle.seth(275)
turtle.fd(90)

# Arm 1
turtle.penup()
turtle.pensize(10)
turtle.goto(92, -150)
turtle.seth(240)
turtle.pendown()
turtle.fd(80)
turtle.left(10)
turtle.circle(-28, 185)

# Arm 2
turtle.penup()
turtle.goto(0, 50)
turtle.seth(0)
turtle.pensize(10)
turtle.circle(-120, -60)
turtle.seth(200)
turtle.pendown()
turtle.fd(72)
turtle.left(20)
turtle.circle(30, 150)
turtle.left(20)
turtle.fd(20)
turtle.right(15)
turtle.fd(10)
turtle.pensize(5)
turtle.fillcolor("#3366cc")
turtle.begin_fill()
turtle.seth(92)
turtle.circle(-120, 31)
turtle.seth(200)
turtle.fd(45)
turtle.left(90)
turtle.fd(52)
turtle.end_fill()
turtle.fd(-12)
turtle.right(90)
turtle.fd(40)
turtle.penup()
turtle.right(90)
turtle.fd(18)
turtle.pendown()
turtle.right(86)
turtle.fd(40)
turtle.penup()
turtle.goto(-152, -86)
turtle.pendown()
turtle.left(40)
turtle.circle(35, 90)
# Body coloring
turtle.penup()
turtle.goto(-80, 116)
turtle.seth(10)
turtle.pensize(5)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("#3366cc")
turtle.fd(155)
turtle.seth(-88)
turtle.fd(37)
turtle.seth(195)
turtle.fd(156)
turtle.end_fill()
turtle.penup()
turtle.goto(-75, 38)
turtle.seth(15)
turtle.pendown()
turtle.begin_fill()
turtle.fd(158)
turtle.seth(-88)
turtle.fd(55)
turtle.seth(140)
turtle.circle(120, 78)
turtle.end_fill()
# Arm 1 To color
turtle.penup()
turtle.fillcolor("#3366cc")
turtle.pensize(5)
turtle.goto(75, -170)
turtle.pendown()
turtle.begin_fill()
turtle.seth(240)
turtle.fd(30)
turtle.right(90)
turtle.fd(17)
turtle.end_fill()
turtle.fd(10)
turtle.left(80)
turtle.fd(55)
turtle.penup()
turtle.left(90)
turtle.fd(15)
turtle.pendown()
turtle.left(85)
turtle.fd(55)
turtle.penup()
turtle.goto(43, -225)
turtle.left(84)
turtle.pendown()
turtle.circle(60, 51)
turtle.speed(0)

# Body vertical lines
for i in range(3):
    turtle.penup()
    turtle.goto(-70 + i * 15, 135)
    turtle.seth(-90)
    turtle.pendown()
    turtle.pensize(5)
    turtle.fd(15 - 2 * i)

for i in range(3):
    turtle.penup()
    turtle.goto(36 + i * 15, 156)
    turtle.seth(-90)
    turtle.pendown()
    turtle.pensize(5)
    turtle.fd(15 - 2 * i)
    a = -60
    b = 70

for i in range(4):
    turtle.penup()
    turtle.goto(a, b)
    a = a + 40
    b = b + 10
    turtle.seth(-90)
    turtle.pendown()
    turtle.pensize(5)
    turtle.fd(26)


def oo(li, jing):
    turtle.penup()
    turtle.turtle.goto(0, 50)
    turtle.seth(0)
    turtle.circle(-120, li)
    turtle.pendown()
    turtle.right(jing)
    turtle.turtle.pensize(5)
    oo(-60, 110)
    turtle.fd(130)
    oo(-28, 96)
    turtle.fd(140)
    oo(9, 89)
    turtle.fd(144)
    oo(42, 70)
    turtle.fd(160)
    oo(80, 60)
    turtle.fd(130)
    turtle.penup()
    turtle.turtle.goto(-80, -40)
    turtle.right(160)
    turtle.pendown()
    turtle.right(50)
    turtle.circle(70, 45)
    turtle.right(75)
    turtle.circle(70, 38)
    turtle.right(50)
    turtle.circle(70, 45)
    turtle.right(90)
    turtle.circle(70, 48)
    turtle.penup()
    turtle.turtle.goto(-53, -70)
    turtle.pendown()
    turtle.left(40)
    turtle.circle(70, 30)
    turtle.right(50)
    turtle.circle(70, 20)
    turtle.right(50)
    turtle.circle(70, 38)
    turtle.right(70)
    turtle.circle(70, 24)
    turtle.penup()
    turtle.turtle.goto(-19, -105)
    turtle.left(72)
    turtle.pendown()
    turtle.fd(22)
    turtle.right(60)
    turtle.fd(22)
    oo(-140, 80)
    turtle.circle(-90, 120)
    turtle.penup()
    oo(140, 100)
    turtle.circle(90, 13)
    turtle.pendown()


turtle.right(-50)
turtle.circle(70, 45)
turtle.right(75)
turtle.circle(70, 38)
turtle.right(50)
turtle.circle(70, 36)
turtle.penup()
turtle.goto(22, -185)
turtle.right(70)
turtle.pendown()
turtle.fd(72)
turtle.penup()
turtle.goto(-40, -182)
turtle.right(38)
turtle.pendown()
turtle.fd(70)
turtle.speed(10)
# The left eye
turtle.penup()
turtle.pensize(7)
turtle.goto(-15, -110)
turtle.seth(0)
turtle.pendown()
turtle.pensize(10)
turtle.begin_fill()
turtle.left(130)
turtle.fd(110)
turtle.right(250)
turtle.circle(90, 60)
turtle.circle(40, 120)
turtle.fillcolor("#F5FFFA")
turtle.end_fill()

# Right eye
turtle.penup()
turtle.goto(5, -110)
turtle.pendown()
turtle.begin_fill()
turtle.right(30)
turtle.fd(110)
turtle.right(-250)
turtle.circle(-90, 60)
turtle.circle(-40, 120)
turtle.end_fill()
turtle.done()
