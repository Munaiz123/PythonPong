#Raspbery Pi Branch
#Module for Simple Graphics

import turtle
import os

# Game Screen
window = turtle.Screen()
window.title('Pong by @amunaizing')
window.bgcolor('lightsteelblue')
window.setup(width=800, height=700)
window.tracer(0)

# Score
PlayerOneScore = 0
PlayerTwoScore = 0


# Paddle A
paddleA = turtle.Turtle()
paddleA.speed(0)#speed for animation not for on screen speed
paddleA.shape('square')
paddleA.color('pink')
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-365, 0)

# Paddle B
paddleB = turtle.Turtle()
paddleB.speed(0)#speed for animation not for on screen speed
paddleB.shape('square')
paddleB.color('pink')
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(365, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)#speed for animation not for on screen speed
ball.shape('circle')
ball.color('snow')
ball.penup()
ball.goto(0, 0)
ball.dx = 2 # d is for delta or 'change'. everytime the ball moves, it moves by 2 pixels
ball.dy = 2

# SCORE PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, -245)
pen.write('Player One: 0        Player Two: 0', align='center', font=('Garamond', 25, 'normal'))

# PAWS PEN
pawsPen = turtle.Turtle()
pawsPen.speed(0)
pawsPen.color('red')
pawsPen.penup
pawsPen.hideturtle()
pawsPen.goto(0,0)



# Paddle Functions

def paddleAUp():
    # Y increases as Y goes up / decreases as it goes down
    y = paddleA.ycor() #ycor method is from the turtle module. returns Y coordinates.
    y += 20
    paddleA.sety(y)

def paddleADown():
    # Y increases as Y goes up / decreases as it goes down
    y = paddleA.ycor() #ycor method is from the turtle module. returns Y coordinates.
    y -= 20
    paddleA.sety(y)

def paddleBUp():
    # Y increases as Y goes up / decreases as it goes down
    y = paddleB.ycor()  # ycor method is from the turtle module. returns Y coordinates.
    y += 20
    paddleB.sety(y)

def paddleBDown():
    # Y increases as Y goes up / decreases as it goes down
    y = paddleB.ycor()  # ycor method is from the turtle module. returns Y coordinates.
    y -= 20
    paddleB.sety(y)

pause = False

def gamePaws():
    if pause == False:
        print("PAAAAAAWWWSS", 'FALSE')
        pause = True
        pawsPen.write('Tri-ing 2 paws', align='center', font=('Garamond', 25, 'normal'))
        
    else:
        print('un-PAAWSS')
        pawsPen.clear()
        pause = False
        
    

    

# Keyboard Binding
window.listen()

window.onkey(paddleAUp, 'w')
window.onkey(paddleADown, 's')

window.onkey(paddleBUp, 'Up')
window.onkey(paddleBDown, 'Down')

window.onkey(gamePaws, 'p')



# MAIN GAME LOOP
while True:
    window.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border checking - once it gets to a certain point, we want it to bounce off.
    # we need to compare the ball's Y coordinate for the top border
    if ball.ycor() > 330:
        ball.sety(330)
        ball.dy *= -1
    if ball.ycor() < -330:
        ball.sety(-330)
        ball.dy *= -1

    # we need to compare the ball's x coordinate for the top border

    if ball.xcor() > 380:
        ball.setx(0)
        ball.dx *= -1
        os.system('aplay score.wav&')
        PlayerOneScore += 1
        pen.clear()
        pen.write('Player One: %s       Player Two: %s' %(PlayerOneScore, PlayerTwoScore), align='center', font=('Garamond', 25, 'normal'))
        #print 'PlayerOneScore', PlayerOneScore

    if ball.xcor() < -380:
        ball.goto(0, 0)
        ball.dx *= -1
        os.system('aplay score.wav&')
        PlayerTwoScore += 1
        pen.clear()
        pen.write('Player One: %s       Player Two: %s' %(PlayerOneScore, PlayerTwoScore), align='center', font=('Garamond', 25, 'normal'))
        #print 'PlayerTwoScore', PlayerTwoScore

    # Ball bouncing off the paddle
    if (ball.xcor() > 340 and ball.xcor() < 350 )and (ball.ycor() < paddleB.ycor() + 40 and ball.ycor() > paddleB.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system('aplay paddle.wav&')

    if (ball.xcor() < -340 and ball.xcor() > -350 )and (ball.ycor() < paddleA.ycor() + 40 and ball.ycor() > paddleA.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system('aplay paddle.wav&')
