#Module for Simple Graphics

import turtle

# Game Screen
window = turtle.Screen()
window.title('Pong by @amunaizing')
window.bgcolor('lightsteelblue')
window.setup(width=800, height=700)
window.tracer(0)

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
ball.shape('square')
ball.color('snow')
ball.penup()
ball.goto(0, 0)


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

# Keyboard Binding
window.listen()

window.onkey(paddleAUp, 'w')
window.onkey(paddleADown, 's')

window.onkey(paddleBUp, 'Up')
window.onkey(paddleBDown, 'Down')


# MAIN GAME LOOP
while True:
    window.update()
