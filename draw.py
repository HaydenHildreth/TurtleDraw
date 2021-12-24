import turtle

turtle.setup(600, 600)
player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
screen = turtle.Screen()
screen.title("Canvas example")
playerpos = []


def screenpos():
    global playerpos
    a, b = player.pos()
    a = int(a)
    b = int(b)
    p = (a, b)


def up():
    global player
    player.forward(10)
    screenpos()


def right():
    global player
    player.right(15)


def left():
    global player
    player.left(15)


def close():
    screen.bye()


screen.onkey(up, "w")
screen.onkey(right, "d")
screen.onkey(left, "a")
screen.onkey(close, "q")
screen.listen()
screen.mainloop()
