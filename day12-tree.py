import turtle, math
#A class that will create a christmas tree
class ChristmasTree:
    #------Variables------
    #Defines the height of the triangle
    triangleHeight = 0
    #------Initialiser------
    #Initialises the turtle
    def __init__(self, anchor=(0,0), triangleSideSize=200, logSize=(25, 50)):
        #Debug.Log(msg="Christmas Tree Initalised", loc="ChristmasTree/init", name="Message")
        #------Sets instance properties------
        self.anchor = anchor
        self.triangleSideLength = triangleSideSize
        self.logSize = logSize
        ChristmasTree.triangleHeight = math.sqrt(self.triangleSideLength**2 - (self.triangleSideLength/2)**2)
        #Creates the first triangle
        self.createTriangle()
        #Creates the second triangle
        self.createTriangle(startingPos=(0, -ChristmasTree.triangleHeight))
        #Creates the third triangle
        self.createTriangle(startingPos=(0, -ChristmasTree.triangleHeight * 2))
        #Creates the log
        self.createLog(startingPos=(0, -ChristmasTree.triangleHeight * 2))

    #------Methods/Functions------
    def createTriangle(self, startingPos=(0, 0)):
        #Debug.Log(msg="Triangle Created", loc="ChristmasTree/createTriangle", name="Message")
        #Creates a turtle for the triangle
        triangleTurtle = turtle.Turtle()
        triangleTurtle.hideturtle()
        #Sets the turtle starting position and temporarily stops drawing
        triangleTurtle.penup()
        triangleTurtle.setx(self.anchor[0] + startingPos[0])
        triangleTurtle.sety(self.anchor[1] + startingPos[1])
        triangleTurtle.pendown()
        #Defines how far the turtle must turn
        turningAngle = 180-60
        #Creates the triangle
        for i in range(3):
            triangleTurtle.forward(self.triangleSideLength)
            triangleTurtle.left(turningAngle)
    def createLog(self, startingPos=(0, 0)):
        #Creates a turtle for the log
        logTurtle = turtle.Turtle()
        logTurtle.hideturtle()
        #Sets the turtle starting position and centres it to the tree and temporarily stops drawing
        logTurtle.penup()
        logTurtle.setx(self.anchor[0] + startingPos[0] + ((self.triangleSideLength // 2) - (self.logSize[0] // 2)))
        logTurtle.sety(self.anchor[1] + startingPos[1])
        logTurtle.pendown()
        #Creates the log
        for i in range(4):
            if i % 2 == 0:
                logTurtle.forward(self.logSize[0])
                logTurtle.right(90)
            elif i % 2 == 1:
                logTurtle.forward(self.logSize[1])
                logTurtle.right(90)

if __name__=="__main__":
    turtle.Screen()
    turtle.tracer(0, 0)
    for i in range(5):
       ChristmasTree(anchor=(-100* i, 200), triangleSideSize=75, logSize=(10, 20))
    turtle.update()
    input()
