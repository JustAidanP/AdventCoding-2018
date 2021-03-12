import turtle, time
#Defines an object which will trace the mouse as it moves
class MouseTracer:
    #------Initialiser------
    #Creates the mouse tracer object
    def __init__(self):
        self.createTurtle()
        self.mousePos = (0, 0)
        #Tells turtle to keep track of the mouse
        turtle.getcanvas().bind('<Motion>', self.getMousePosition)
        #Loops through to keep track of the mouse position
        while True:
            self.traceMouse(1, 1)
            time.sleep(0.01)

    #------Methods/Functions------
    #Creates a turtle
    def createTurtle(self):
        turtle.Screen()
        turtle.tracer(0, 0)
        self.tracerTurtle = turtle.Turtle()
        self.tracerTurtle.penup()

    #Recieves the mouse position
    def getMousePosition(self, motion):
        self.mousePos = (motion.x - (turtle.window_width() / 2), (turtle.window_height() / 2) - motion.y)

    #Sets the position of the turtle to the mouse position and draws a dot
    def traceMouse(self, x, y):
        self.tracerTurtle.setpos(self.mousePos[0], self.mousePos[1])
        self.tracerTurtle.dot()
        turtle.update()

if __name__=="__main__":
    #RUns the mouse tracer
    MouseTracer()
    input()
