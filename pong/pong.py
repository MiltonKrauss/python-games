import turtle
import winsound
import time
import random

wn = turtle.Screen()
wn.title('Pong')
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.color('white')
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.color('white')
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('orange')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player L: 0    Player R: 0', align='center', font=('Courier', 24, 'bold'))

# Game Start
pencil = turtle.Turtle()
pencil.speed(0)
pencil.color('red')
pencil.penup()
pencil.hideturtle()
pencil.goto(0, -30)
pencil.write('Game Starts in 3', align='center', font=('Courier', 40, 'bold'))

# Function
def paddle_a_up():
    y = paddle_a.ycor()
    if y <= 240:
        y += 0.7
        paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    if y >= -240:
        y -= 0.7
        paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    if y <= 240:
        y += 0.7
        paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    if y >= -240:
        y -= 0.7
        paddle_b.sety(y)

# Keyboard binding
wn.listen()

# Define variables to keep track of pressed keys
keys_a = {'w': False, 's': False}
keys_b = {'Up': False, 'Down': False}

def set_key_a(key, state):
    keys_a[key] = state

def set_key_b(key, state):
    keys_b[key] = state

# Set up keypress and keyrelease events for paddle A
wn.onkeypress(lambda: set_key_a('w', True), 'w')
wn.onkeyrelease(lambda: set_key_a('w', False), 'w')
wn.onkeypress(lambda: set_key_a('s', True), 's')
wn.onkeyrelease(lambda: set_key_a('s', False), 's')

# Set up keypress and keyrelease events for paddle B
wn.onkeypress(lambda: set_key_b('Up', True), 'Up')
wn.onkeyrelease(lambda: set_key_b('Up', False), 'Up')
wn.onkeypress(lambda: set_key_b('Down', True), 'Down')
wn.onkeyrelease(lambda: set_key_b('Down', False), 'Down')

# Game start screen with countdown
ball.hideturtle()
wn.update()
time.sleep(1)
pencil.clear()
pencil.write('Game Starts in 2', align='center', font=('Courier', 40, 'bold'))
wn.update()
time.sleep(1)
pencil.clear()
pencil.write('Game Starts in 1', align='center', font=('Courier', 40, 'bold'))

# Random ball start position and velocity
ball.goto(0, random.randint(-200, 200))
ball.showturtle()
ball_start_direction = random.randint(1, 4)
if ball_start_direction == 1:
    ball.dx = 0.3
    ball.dy = 0.3
elif ball_start_direction == 2:
    ball.dx = -0.3
    ball.dy = 0.3
elif ball_start_direction == 3:
    ball.dx = 0.3
    ball.dy = -0.3
else:
    ball.dx = -0.3
    ball.dy = -0.3

wn.update()
time.sleep(1)
pencil.clear()

# Main game loop
while score_a < 10 and score_b < 10:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Move paddles based on pressed keys
    if keys_a['w']:
        paddle_a_up()
    if keys_a['s']:
        paddle_a_down()
    if keys_b['Up']:
        paddle_b_up()
    if keys_b['Down']:
        paddle_b_down()

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 410:
        score_a += 1
        pen.clear()
        pen.write('Player L: {}    Player R: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))
        ball.goto(0,0)
        ball.dx *= -1

    if ball.xcor() < -410:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write('Player L: {}    Player R: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'bold'))

    # Paddle and ball collisions
    if (ball.xcor() > 330 and ball.xcor() < 350) and ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60:
        ball.dx *= -1

    if (ball.xcor() < -330 and ball.xcor() > -350) and ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60:
        ball.dx *= -1

# Game end screen
if score_a == 10:
    ball.hideturtle()
    pencil.write('Player L Wins!', align='center', font=('Courier', 40, 'bold'))
    wn.update()
    time.sleep(5)
else:
    ball.hideturtle()
    pencil.write('Player R Wins!', align='center', font=('Courier', 40, 'bold'))
    wn.update()
    time.sleep(5)