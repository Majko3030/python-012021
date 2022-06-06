import turtle

wn = turtle.Screen()
"creating a window"
wn.title("Pong test")
wn.bgcolor("dark blue")
wn.setup(width=800, height=500)
wn.tracer(0)
# stops window from updating - allows to speed up the game'

# scores
score_a = 0
score_b = 0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
# speed of animation, sets to maximum possible - otherwise would be slow
paddle_a.shape("square")
paddle_a.color("light blue")
paddle_a.penup()
# withouth the penup - would make line from center!'
paddle_a.shapesize(stretch_wid=4.5, stretch_len=1.5)
# default size is 20x20 pixels, the above times the amount
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("light blue")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=4.5, stretch_len=1.5)
paddle_b.goto(350,0)
# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("turtle")
ball.color("pink")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1
# every time, it moves - it mvoes by 2 pixels
# main game loop - after creating- window stays (not just flash as before)

# pen
pen = turtle.Turtle()
pen.speed(1)
pen.color("yellow")
pen.penup()
pen.hideturtle()
# does not see it
pen.goto(0, 200)
pen.write("Player A: 0  Player B: 0", align = "center", font=("Courier", 20,"normal"))

# Functions
def paddle_a_up():
    y = paddle_a.ycor()
    # information about y coordintate- returns y cooadinate
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)
# keyboard binding
wn.listen()
# listens to keyboard input
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()
    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() >250:
        ball.sety(250)
        ball.dy *= -1
        # negative -1 reverses directions
    if ball.xcor() >400:
        ball.setx(400)
        ball.dx *= -1
    if ball.ycor() <-250:
        ball.sety(-250)
        ball.dy *= -1
    if ball.xcor() <-400:
        ball.setx(-400)
        ball.dx *= -1
    # ball outside of the field
    if ball.xcor() > 390 or ball.xcor() < -390:
        if ball.xcor() > 390:
            score_a +=1
        else:
            score_b +=1
        ball.goto(0,0)
        ball.dx *=-1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 20, "normal"))

    # paddle and ball collisions
    if (ball.xcor() > 330 and ball.xcor()<340) and (ball.ycor()< paddle_b.ycor() + 90 and ball.ycor() > paddle_b.ycor() - 90):
        ball.setx(320)
        ball.dx *= -1
    if (ball.xcor() < -330 and ball.xcor() >-340) and (ball.ycor() < paddle_a.ycor() + 90 and ball.ycor() > paddle_a.ycor() - 90):
        ball.setx(-320)
        ball.dx *= -1