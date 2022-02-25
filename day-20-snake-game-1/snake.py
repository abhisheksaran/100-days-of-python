from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        # Add a new segment to the.segments
        t = Turtle()
        t.penup()
        t.color('white')
        t.shape('square')
        t.goto(position)
        self.segments.append(t)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def clear(self):
        for segment in self.segments:
            segment.clear()

    def move(self):
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(self.segments[i-1].position())

    def move_forwards(self):
        self.move()
        self.segments[0].forward(20)

    def turn_left(self):
        if self.segments[0].heading() == 90.0:
            self.move()
            self.segments[0].left(90)
        if self.segments[0].heading() == 270.0:
            self.move()
            self.segments[0].right(90)

    def turn_right(self):
        if self.segments[0].heading() == 90.0:
            self.move()
            self.segments[0].right(90)
        if self.segments[0].heading() == 270.0:
            self.move()
            self.segments[0].left(90)

    def turn_up(self):
        if self.segments[0].heading() == 0.0:
            self.move()
            self.segments[0].left(90)
        if self.segments[0].heading() == 180.0:
            self.move()
            self.segments[0].right(90)

    def turn_down(self):
        if self.segments[0].heading() == 0.0:
            self.move()
            self.segments[0].right(90)
        if self.segments[0].heading() == 180.0:
            self.move()
            self.segments[0].left(90)



