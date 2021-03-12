import turtle, math
from Vector import *
#Defines an elipse
class Ellipse:
    #------Initialiser------
    #Creates an ellipse, takes a size and position
    #Detail defines how many points on the ellipse must be created
    def __init__(self, size=Vector.zero(), position=Vector.zero(), detail=360):
        self.size = size
        self.position = position
        self.detail = detail
        #Creates a turtle
        self.createTurtle()
        #Draws the ellipse
        self.draw()
    #------Methods/Functions------
    #Creatse a turtle
    def createTurtle(self):
        self.ellipseTurtle = turtle.Turtle()
        self.ellipseTurtle.penup()
    #Draws the ellipse
    def draw(self):
        #Sets the initial position of the turtle
        self.ellipseTurtle.setpos(self.position.x + (self.size.x / 2), self.position.y)
        self.ellipseTurtle.pendown()
        for i in range(self.detail + 1):
            #Calculates the x position of the point, using the detail and size
            xPos = math.cos((2 * i * math.pi) / self.detail) * self.size.x / 2
            #Calculates the x position of the point
            yPos = math.sin((2 * i * math.pi) / self.detail) * self.size.y / 2
            #Sets the turtle's position to the ellipse point
            self.ellipseTurtle.setpos(self.position.x + xPos, self.position.y + yPos)
        self.ellipseTurtle.penup()

if __name__=="__main__":
    turtle.Screen()
    turtle.tracer(0, 0)
    Ellipse(size=Vector(500, 250), position=Vector(100, 50), detail=15)
    input()