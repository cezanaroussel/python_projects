# Pong in Python 3
# By Cezana Roussel
# CS 3750.02 with E. Sander
# Cal Poly Pomona, Fall 2020

import turtle

win = turtle.Screen()
win.title("Pong by Cezana Roussel")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

#Score
score_a = 0
score_b = 0

    # Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)   # Place Paddle A on left of x-axis 

    # Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("blue")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)  
paddle_b.penup()
paddle_b.goto(350, 0)     #Place Paddle B on right of x-axis

    # Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)       # We want the ball to be centered, i.e. (0,0)
ball.dx = 1.5         # Every time our ball moves, it moves 1.5 px/sec
ball.dy = 1.5


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Functions 
# Each function is defined first, then called upon in the program
# We must define a function for each movement that takes place in the game

def paddle_a_up():
    y = paddle_a.ycor() 
    y += 20                    # Move up 20px on the y-axis 
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20                    # Move down 20px on the y-axis
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor() 
    y += 20                    
    paddle_b.sety(y)
    
def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard Binding
win.listen() # listen for keyboard input, how the user moves the paddles 
win.onkeypress(paddle_a_up, "w") # when key w is hit, move upwards on y- axis 20 px
win.onkeypress(paddle_a_down, "s") # when s is hit, move downards on y- axis 20 px
win.onkeypress(paddle_b_up, "Up")  #when arrow is pressed, move upwards on y-axis 
win.onkeypress(paddle_b_down, "Down") #when arrow is pressed, move downwards on y-axis


# Main game loop
while True:
    win.update()

 # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
       

    # Left and right score keeping
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
    
