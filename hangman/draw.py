from turtle import Turtle, Screen
def szu_1(x):
    x.color("black")
    x.pensize(10)
    x.right(90)
    return x.forward(200)


def szu_2(x):
    x.color("black")
    x.pensize(10)
    x.right(90)
    x.forward(50)
    return x.backward(100)

def szu_3(x):
    x.color("black")
    x.pensize(10)
    x.forward(50)
    x.right(90)
    x.forward(200)
    x.right(90)
    return x.forward(100)

def head(x):
    x.color("pink")
    x.pensize(10)
    x.left(180)
    return x.circle(25)


def body(hangman):
    hangman.circle(25, 180)
    hangman.pensize(10)
    hangman.color("yellow")
    hangman.right(90)
    return hangman.forward(50)

def right_arm(hangman):
    # hangman.pensize(10)
    # hangman.color("yellow")
    hangman.backward(50)
    hangman.right(90)
    hangman.color("red")
    return hangman.forward(50)


def left_arm(hangman):
    hangman.pensize(10)
    hangman.color("red")
    hangman.backward(50)
    hangman.right(180)
    return hangman.forward(50)


def left_leg(hangman):
    hangman.pensize(10)
    hangman.color("red")
    hangman.backward(50)
    hangman.color("yellow")
    hangman.setx(100)
    hangman.sety(-100)
    hangman.color("red")
    hangman.right(25)
    return hangman.forward(50)


def right_leg(hangman):
    hangman.pensize(10)
    hangman.color("red")
    hangman.backward(50)
    hangman.right(130)
    return hangman.forward(50)
# t1 = Turtle()
# t1.showturtle()
# szu_1(t1)
# szu_2(t1)
# szu_3(t1)
# t1.speed(5)
# head(t1)
# body(t1)
# right_arm(t1)
# left_arm(t1)
# left_leg(t1)
# right_leg(t1)


