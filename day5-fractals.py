import turtle, random

#Creates a fractal object that draws onto the screen
class Fractal():
    #------Variables------
    lastSeed = (0, 0)
    #Defines how many times a point has been placed
    currentIter = 0
    #------Initialiser------
    #Initialises the fractal object with target parameters
    #Takes in the number of start points
    def __init__(self, pointCount=3):
        #Sets up the turtle instance
        turtle.Screen()
        #Tells turtle to draw instantly
        turtle.tracer(0, 0)
        #Sets up a turtle instance
        self.fractalTurtle = turtle.Turtle()
        #Starts the fractal
        self.createRandomPoint()
        self.seedPoints = [(-300, -300), (0, 300), (300, -300)]
        self.percentageToSeed()
        while True:
            self.percentageToSeed()

    #------Methods/Functions------
    #Draws a spiral recursively
    def drawSpiral(self, segmentLength, turningPoint):
        self.fractalTurtle.forward(segmentLength)
        self.fractalTurtle.left(turningPoint)
        if segmentLength <= 200: self.drawSpiral(segmentLength + 0.01, turningPoint)
    #Creates a random starting point for the turtle
    def createRandomPoint(self):
        #Randomly chooses a starting point for the turtle
        #And sets the turtle to it
        randomStart = (random.randint(-300, 300), random.randint(0, 300))
        self.fractalTurtle.penup()
        self.fractalTurtle.setx(randomStart[0])
        self.fractalTurtle.sety(randomStart[1])
    def percentageToSeed(self):
        #Randomly chooses a seed point and moves halfway to it
        targetSeed = self.seedPoints[random.randint(0, 2)]
        #Ensures that the seed position is different every time
        if Fractal.lastSeed == targetSeed: self.percentageToSeed()
        Fractal.lastSeed = targetSeed

        #Changes the colour of the turtle depending on the target seed
        if targetSeed[0] == -300: self.fractalTurtle.color("red")
        if targetSeed[1] == 300: self.fractalTurtle.color("green")
        if targetSeed[0] == 300: self.fractalTurtle.color("blue")

        #Defines the new position of the turtle
        newPosition = (float(targetSeed[0] - self.fractalTurtle.xcor()) / 2 + self.fractalTurtle.xcor(),
                       float(targetSeed[1] - self.fractalTurtle.ycor()) / 2 + self.fractalTurtle.ycor())
        #Draws to the newly defined position
        self.fractalTurtle.setposition(newPosition)
        self.fractalTurtle.dot(4)
        #Updates the turtle screen every 100 frames
        Fractal.currentIter += 1
        if Fractal.currentIter % 25 == 0:turtle.update()

Fractal()
