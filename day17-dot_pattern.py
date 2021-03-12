import turtle
#Defines a dot pattern
class DotPattern:
    #------Variables------
    #Defines the number of pattern occurences
    patternOccurences = 6
    #Defins the y step count
    stepCount = 5
    #------Initialiser------
    #Creates the dots
    def __init__(self):
        self.createTurtle()
        self.createDot()
    #------Methods/Functions------
    #Creates a turtle
    def createTurtle(self):
        self.dotTurtle = turtle.Turtle()
        self.dotTurtle.hideturtle()
        self.dotTurtle.penup()
    #Creates the dots
    def createDot(self):
        self.dotTurtle.setpos(-turtle.window_width()/2, -turtle.window_height() / 2)
        #Draws The initial dots
        self.dotTurtle.setpos(turtle.window_width()/2, -turtle.window_height() / 2)
        #Draws other dots
        outerIndex = 0
        while (DotPattern.stepCount * (outerIndex + 1)) <= turtle.window_height():
            self.dotTurtle.setpos(-turtle.window_width()/2, (-turtle.window_height() / 2) + (DotPattern.stepCount * (outerIndex + 1)))
            distanceMoved = 0
            #Places a dot for the turtle for as long as the turtle is on the screen
            while distanceMoved < 2 * turtle.window_width():
                self.dotTurtle.forward(turtle.window_width() / (DotPattern.patternOccurences * (outerIndex + 1)))
                self.dotTurtle.dot()
                #Breaks if the total distance moved by the turtle is out of the display
                distanceMoved += turtle.window_width() / (DotPattern.patternOccurences * (outerIndex + 1))
            turtle.update()
            outerIndex += 1


if __name__=="__main__":
    #Creates a turtle screen
    turtle.Screen()
    turtle.tracer(0, 0)
    #Draws the dots
    DotPattern()
    turtle.update()
    input()