import turtle
# Screen Setup

wn = turtle.Screen()
wn.title("Pong-Game @Noelle")
wn.bgcolor("black")
wn.setup(width=900, height=600)
wn.tracer(0)

# Score

player_1 = 0
player_2 = 0

# Start Screen

# Start Game
start = turtle.Turtle()
start.speed(0)
start.color('Magenta')
start.penup()
start.hideturtle()
start.goto(0,0)
start.write('PONG GAME', align='center', font=('Times New Roman', '60', 'bold'))

# Press Enter to Start
enter = turtle.Turtle()
enter.speed(0)
enter.color('Magenta')
enter.penup()
enter.hideturtle()
enter.goto(0, -50)
enter.write('Start Game: Press Enter ', align='center', font=('Times New Roman', '36', 'bold'))


# Paddle 1

pad_1 = turtle.Turtle()
pad_1.speed(0)
pad_1.shape("square")
pad_1.color("white")
pad_1.shapesize(stretch_wid=5,stretch_len=0.75)
pad_1.penup()
pad_1.goto(-400, 0)

# Paddle 2

pad_2 = turtle.Turtle()
pad_2.speed(0)
pad_2.shape("square")
pad_2.color("white")
pad_2.shapesize(stretch_wid=5, stretch_len=0.75)
pad_2.penup()
pad_2.goto(400, 0)

# Ball

ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("magenta")
ball.penup()
ball.goto(0, 0)
ball.dx = 1.65 # Ball moves by this many pixels
ball.dy = -1.65

# Pen - Sprint 5

pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal"))


# Functions
def btn_start_pressed():

  start.clear()
  enter.clear()

def pad_1_up():
    y = pad_1.ycor()
    y += 20
    pad_1.sety(y)

def pad_1_down():
    y = pad_1.ycor() # From Turtle Module
    y -= 20
    pad_1.sety(y)

def pad_2_up():
    y = pad_2.ycor() # From Turtle Module
    y += 20
    pad_2.sety(y)

def pad_2_down():
    y = pad_2.ycor()
    y -= 20
    pad_2.sety(y)

# Keyboard controls

wn.listen() # Listen for keyboard inputs
wn.onkeypress(btn_start_pressed, 'Return')
wn.onkeypress(pad_1_up, 'w')
wn.onkeypress(pad_1_down, 's')
wn.onkeypress(pad_2_up, 'k')
wn.onkeypress(pad_2_down, 'm')


# Main game loop

while True:
    wn.update()
    
    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border-Ball Collisions

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 # Reverses the direction
      
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 # Reverses the direction
        
        

    # Left and right
    if ball.xcor() > 470:
        player_1 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_1, player_2), align="center", font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -470:
        player_2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_1, player_2), align="center", font=("Arial", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1
        

    # Paddle-ball collisions
    if (ball.xcor() < -390 and ball.xcor() < -400) and ball.ycor() < pad_1.ycor() + 50 and ball.ycor() > pad_1.ycor() - 50:
        ball.setx(-390)
        ball.dx *= -1 
      
    elif (ball.xcor() > 390 and ball.xcor() < 400) and ball.ycor() < pad_2.ycor() + 50 and ball.ycor() > pad_2.ycor() - 50:
        ball.setx(390)
        ball.dx *= -1
    

# Features to add: 
# Start window needs work
# Show a Winner
# Exit Feature
# Change Background ?
