from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.screen = Screen()
        self.color("white")
        self.shape("square")
        self.penup()
        self.goto(position)
        self.turtlesize(1, 5)
        self.setheading(90)

    def move_up(self):
        self.forward(30)


    def move_down(self):
        self.backward(30)

    def move_paddle(self,key1,key2):
        self.screen.listen()
        if self.ycor() < 225 or self.ycor() > -225:
            self.screen.onkeypress(self.move_up, key1)
            self.screen.onkeypress(self.move_down, key2)



