# Tanner Hicks and Nicole Smith
# Recreation of Pong Game for CS4 short project

# turtle go brrr
# importing the turtle class for us to code project on screen
import turtle
# import Image

fin = 0
# Creating the base screen seen in pong
scanner = turtle.Screen()
# Rip yurtle can't make anything show up
scanner.title("PongGame")
scanner.bgcolor("black")
scanner.setup(width=800, height=600)

# Barrier 1
midpaddleone = turtle.Turtle()
midpaddleone.speed(0)
midpaddleone.shape("square")
midpaddleone.color("black")
midpaddleone.shapesize(stretch_wid=5, stretch_len=1)
midpaddleone.penup()
midpaddleone.goto(0, -150)

# Barrier 2
midpaddletwo = turtle.Turtle()
midpaddletwo.speed(0)
midpaddletwo.shape("square")
midpaddletwo.color("black")
midpaddletwo.shapesize(stretch_wid=5, stretch_len=1)
midpaddletwo.penup()
midpaddletwo.goto(0, 150)


# Line down the middle(adds to illusion of border)
midLine = turtle.Turtle()
midLine.speed(0)
midLine.shape("square")
midLine.color("white")
midLine.shapesize(stretch_wid=39, stretch_len=0.1)
midLine.penup()
midLine.goto(0, 0)

# Allows for animation
scanner.tracer(0)

# Left hand Paddle (Paddle A)
paddleA = turtle.Turtle()
paddleA.speed(0)
paddleA.shape("square")
paddleA.color("white")
paddleA.shapesize(stretch_wid=5, stretch_len=1)
paddleA.penup()
paddleA.goto(-350, 0)

# Right hand Paddle ( Paddle B)
paddleB = turtle.Turtle()
paddleB.speed(0)
paddleB.shape("square")
paddleB.color("white")
paddleB.shapesize(stretch_wid=5, stretch_len=1)
paddleB.penup()
paddleB.goto(350, 0)

# Making real ball
ball = turtle.Turtle()
# Will implement increase speed during rounds, this is base speed
ball.speed(5)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = .2
ball.dy = -.2

# Variables to keep track of score
scoreA = 0
scoreB = 0

# Scores shown(pen method)
score = turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 260)
score.write("A: 0  B: 0", align="center", font=("Comic Sans MS", 24, "normal"))

# Keyboard Functions(moving)
def paddleaup():
    y = paddleA.ycor()
    y += 20
    paddleA.sety(y)

def paddleadown():
    y = paddleA.ycor()
    y -= 20
    paddleA.sety(y)

def paddlebup():
    y = paddleB.ycor()
    y += 20
    paddleB.sety(y)

def paddlebdown():
    y = paddleB.ycor()
    y -= 20
    paddleB.sety(y)


# Keybinds for movement
scanner.listen()
# Left
scanner.onkeypress(paddleaup, "w")
scanner.onkeypress(paddleadown, "s")
# Right
scanner.onkeypress(paddlebup, "Up")
scanner.onkeypress(paddlebdown, "Down")

# Deuce Round Ball (it's attempting to hide)
balltwo = turtle.Turtle()
balltwo.speed(5)
balltwo.shape("circle")
balltwo.color("black")
balltwo.penup()
balltwo.goto(0, 0)
balltwo.dx = -.23
balltwo.dy = .23


# Main game code(what makes us run!!)(loop)
while True:
    scanner.update()

    if (scoreA > 4 and scoreB > 4) or scoreA > 4 > scoreB or scoreA < 4 < scoreB:
        # Second ball moving
        balltwo.color("blue")
        balltwo.setx(balltwo.xcor() + balltwo.dx)
        balltwo.sety(balltwo.ycor() + balltwo.dy)

    # Update new ball position(animation)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Keep in the frame

    # Too high
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # Too low
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Deuce only too high
    if balltwo.ycor() > 290:
        balltwo.sety(290)
        balltwo.dy *= -1
    # Too low
    elif balltwo.ycor() < -290:
        balltwo.sety(-290)
        balltwo.dy *= -1

    # Left of frame
    if ball.xcor() < -350:
        # speed of ball
        ball.dx = .2
        # GOALLL
        scoreB += 1
        # Change score
        score.clear()
        score.write("A: {}   B: {}".format(scoreA, scoreB), align="center", font=("Comic Sans MS", 24, "normal"))
        # Back to round one ladies and gents
        ball.goto(0, 0)

    # Right of frame
    elif ball.xcor() > 350:
        # Reset speed of ball
        ball.dx = -.2
        # GOALL
        scoreA += 1
        # Change score
        score.clear()
        score.write("A: {}   B: {}".format(scoreA, scoreB), align="center", font=("Comic Sans MS", 24, "normal"))
        # Back to round one ladies and gents
        ball.goto(0, 0)

    # Left of frame(blue)
    if balltwo.xcor() < -350:
        # speed of ball
        balltwo.dx = .23
        # GOALLL
        scoreB += 1
        # Change score
        score.clear()
        score.write("A: {}   B: {}".format(scoreA, scoreB), align="center", font=("Comic Sans MS", 24, "normal"))
        # Back to round one ladies and gents
        balltwo.goto(0, 0)
    # Right of frame(blue)
    elif balltwo.xcor() > 350:
        # Reset speed of ball
        balltwo.dx = -.23
        # GOALL
        scoreA += 1
        # Change score
        score.clear()
        score.write("A: {}   B: {}".format(scoreA, scoreB), align="center", font=("Comic Sans MS", 24, "normal"))
        # Back to round one ladies and gents
        balltwo.goto(0, 0)

        # The person hit the ball!!
        # No score(collisions)
        # Paddle A hits
    if ball.xcor() < -340 and paddleA.ycor() + 50 > ball.ycor() > paddleA.ycor() - 50:
        # Increase speed
        ball.dx -= .05
        # Slide to the right
        ball.dx *= -1

    # Paddle B hits
    elif ball.xcor() > 340 and paddleB.ycor() + 50 > ball.ycor() > paddleB.ycor() - 50:
        # Increase speed
        ball.dx += .05
        # Slide to the left
        ball.dx *= -1

        # Paddle A hits blue ball
    if balltwo.xcor() < -340 and paddleA.ycor() + 50 > balltwo.ycor() > paddleA.ycor() - 50:
        # Increase speed
        balltwo.dx -= .05
        # Slide to the right
        balltwo.dx *= -1

    # Paddle B hits blue ball
    elif balltwo.xcor() > 340 and paddleB.ycor() + 50 > balltwo.ycor() > paddleB.ycor() - 50:
        # Increase speed
        balltwo.dx += .05
        # Slide to the left
        balltwo.dx *= -1

    # Sudden death
    if scoreA == 9 and scoreB == 9:
        break

    if scoreA == 10:
        fin = 'Player A'
        break
    if scoreB == 10:
        fin = 'Player B'
        break


while scoreA == scoreB == 9:
    scanner.update()
    score.clear()
    score.write("Showdown", align="center", font=("Comic Sans MS", 24, "normal"))
    midpaddleone.color("red")
    midpaddletwo.color("red")

    balltwo.color("blue")
    balltwo.setx(balltwo.xcor() + balltwo.dx)
    balltwo.sety(balltwo.ycor() + balltwo.dy)

    # Update new ball position(animation)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Keep in the frame

    # Too high
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # Too low
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Deuce only too high
    if balltwo.ycor() > 290:
        balltwo.sety(290)
        balltwo.dy *= -1
    # Too low
    elif balltwo.ycor() < -290:
        balltwo.sety(-290)
        balltwo.dy *= -1

    # The person hit the ball!!
    # No score(collisions)
    # Paddle A hits
    if ball.xcor() < -340 and paddleA.ycor() + 50 > ball.ycor() > paddleA.ycor() - 50:
        # Increase speed
        ball.dx -= .05
        # Slide to the right
        ball.dx *= -1

    # Paddle B hits
    elif ball.xcor() > 340 and paddleB.ycor() + 50 > ball.ycor() > paddleB.ycor() - 50:
        # Increase speed
        ball.dx += .05
        # Slide to the left
        ball.dx *= -1

    # Paddle A hits blue ball
    if balltwo.xcor() < -340 and paddleA.ycor() + 50 > balltwo.ycor() > paddleA.ycor() - 50:
        # Increase speed
        balltwo.dx -= .05
        # Slide to the right
        balltwo.dx *= -1

    # Paddle B hits blue ball
    elif balltwo.xcor() > 340 and paddleB.ycor() + 50 > balltwo.ycor() > paddleB.ycor() - 50:
        # Increase speed
        balltwo.dx += .05
        # Slide to the left
        balltwo.dx *= -1

    # Middle Barriers for Ball
    if -10 < ball.xcor() < 10 and 200 > ball.ycor() > 100:
        # Slide to the right
        ball.dx *= -1
    elif -10 < ball.xcor() < 10 and -200 < ball.ycor() < -100:
        # Slide to the left
        ball.dx *= -1
    # Middle Barriers for Blue Ball
    if -10 < balltwo.xcor() < 10 and 200 > balltwo.ycor() > 100:
        # Slide to the right
        balltwo.dx *= -1
    elif -10 < balltwo.xcor() < 10 and -200 < balltwo.ycor() < -100:
        # Slide to the left
        balltwo.dx *= -1

    if ball.xcor() < -350:
        fin = 'Player B'
        break

    # Right of frame
    elif ball.xcor() > 350:
        fin = 'Player A'
        break

    # Left of frame(blue)
    if balltwo.xcor() < -350:
        fin = 'Player B'
        break
    # Right of frame(blue)
    elif balltwo.xcor() > 350:
        fin = 'Player A'
        break

scanner.clear()
scanner.bgcolor("white")
while True:
    scanner.update()
    score.color("black")
    score.goto(0, -50)
    score.write("{} wins!".format(fin), align="center", font=("Comic Sans MS", 65, "normal"))
