import turtle

isim1 = input("Lütfen 1. Oyuncunun Adını Giriniz : ")
isim2 = input("Lütfen 2. Oyuncunun Adını Giriniz : ")

pencere = turtle.Screen()
pencere.title("PinPong Oyunu")
pencere.bgcolor("black")
pencere.setup(width=1000, height=800)
pencere.tracer(0)

raket1 = turtle.Turtle()
raket1.speed(0)
raket1.shape("square")
raket1.color("white")
raket1.penup()
raket1.goto(-465, 0)
raket1.shapesize(5, 1)

raket2 = turtle.Turtle()
raket2.speed(0)
raket2.shape("square")
raket2.color("white")
raket2.penup()
raket2.goto(455, 0)
raket2.shapesize(5, 1)

top = turtle.Turtle()
top.speed(0)
top.shape('circle')
top.color("white")
top.penup()
top.x = 0.15
top.y = 0.15

puan_1 = 0
puan_2 = 0

Scoreboard = turtle.Turtle()
Scoreboard.speed(0)
Scoreboard.color("green")
Scoreboard.penup()
Scoreboard.goto(0,250)
Scoreboard.write("{} : {} {} : {}".format(isim1,puan_1,isim2,puan_2),align='center', font=('Courier', 20, 'bold'))
Scoreboard.hideturtle()

def raket1_up():
    y = raket1.ycor()
    y += 20
    if y < 350:
        raket1.sety(y)
def raket1_down():
    y = raket1.ycor()
    y -= 20
    if y > -350:
        raket1.sety(y)
def raket2_up():
    y = raket2.ycor()
    y += 20
    if y < 350:
        raket2.sety(y)
def raket2_down():
    y = raket2.ycor()
    y -= 20
    if y > -350:
        raket2.sety(y)

pencere.listen()
pencere.onkeypress(raket1_up, 'w')
pencere.onkeypress(raket1_down, 's')
pencere.onkeypress(raket2_up, 'Up')
pencere.onkeypress(raket2_down, 'Down')

while True:
    pencere.update()

    top.setx(top.xcor() + top.x)
    top.sety(top.ycor() + top.y)

    if top.ycor() > 390 or top.ycor() < -390:
        top.y *= -1

    if top.xcor() > 490:
        top.goto(0, 0)
        top.x *= -1
        puan_1 = puan_1 +1
        Scoreboard.clear(),
        Scoreboard.write("{} : {} {} : {}".format(isim1, puan_1, isim2, puan_2), align='center',font=('Courier', 20, 'bold'))

    if top.xcor() < -490:
        top.goto(0, 0)
        top.x *= -1
        puan_2 = puan_2 +1
        Scoreboard.clear()
        Scoreboard.write("{} : {} {} : {}".format(isim1, puan_1, isim2, puan_2), align='center',font=('Courier', 20, 'bold'))

    if (top.xcor() > 445 and top.xcor() < 455) and (top.ycor() < raket2.ycor() + 50 and top.ycor() > raket2.ycor() - 50):
        top.setx(445)
        top.x *= -1

    if (top.xcor() < -445 and top.xcor() > -455) and (top.ycor() < raket1.ycor() + 50 and top.ycor() > raket1.ycor() - 50):
        top.setx(-445)
        top.x *= -1