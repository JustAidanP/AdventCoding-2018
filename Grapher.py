import turtle
#A class that defines what a graph is and creates it
class Graph:
        #------Initialiser------
        #Defines a graph, takes an x and y scale and an x and y div size
        def __init__(self, scale=(1, 1), div=(0.2, 0.2)):
            self.scale = scale
            self.div = div
            #Sets up the turtle screen
            turtle.Screen()
            turtle.tracer(0, 0)
            #Creates a turtle
            self.graphTurtle = turtle.Turtle()
            self.graphTurtle.hideturtle()
            #Creates a up the grid
            self.setUpGrid()
            turtle.update()

        #------Methods/Functions------
        #Plots a point on the grid
        #Takes an x and y
        def plot(self, x, y):
            self.graphTurtle.penup()
            self.graphTurtle.setpos((turtle.window_width() * x) / (2 * self.scale[0]), (turtle.window_height() * y) / (2 * self.scale[1]))
            self.graphTurtle.dot()
        #Plots a given plotter
        def plotPlotter(self, plotter):
            for point in plotter.createPoints():
                self.plot(point.x, point.y)
            turtle.update()

        #Sets up the grid
        def setUpGrid(self):
            #Draws the x and y axis
            self.drawAxis()
            #Creates all divs
            self.drawDivs()

        #Draws the x,y axis
        def drawAxis(self):
            #Sets the stroke of the turtle to 2
            self.graphTurtle.pensize(2)
            #Draws x axis
            self.graphTurtle.penup()
            self.graphTurtle.setpos(-turtle.window_width() / 2, 0)
            self.graphTurtle.pendown()
            self.graphTurtle.setpos(turtle.window_width() / 2, 0)
            #Draws y axis
            self.graphTurtle.penup()
            self.graphTurtle.setpos(0, turtle.window_height() / 2)
            self.graphTurtle.pendown()
            self.graphTurtle.setpos(0, -turtle.window_height() / 2)

        #Draws the divs
        def drawDivs(self):
            #Sets the stroke of the turtle to 0.5 and resets the position
            self.graphTurtle.pensize(0.5)
            self.graphTurtle.sety(0)
            self.graphTurtle.penup()
            #Loops through every x div position and draws a line
            xPosition = 0
            while xPosition <= turtle.window_width() / 2:
                #Draws a div line at a negative and position x position
                self.graphTurtle.setpos(xPosition, turtle.window_height() / 2)
                self.graphTurtle.pendown()
                self.graphTurtle.sety(-turtle.window_height() / 2)
                self.graphTurtle.penup()
                self.graphTurtle.sety(0)
                self.graphTurtle.write(round((xPosition * 2 * self.scale[0]) / turtle.window_width(), 3), font=("Arial", 12, "normal"))

                self.graphTurtle.setpos(-xPosition, turtle.window_height() / 2)
                self.graphTurtle.pendown()
                self.graphTurtle.sety(-turtle.window_height() / 2)
                self.graphTurtle.penup()
                self.graphTurtle.sety(0)
                if xPosition > 0: self.graphTurtle.write(round((-xPosition * 2 * self.scale[0]) / turtle.window_width(), 3), font=("Arial", 12, "normal"))
                #Sets the next positive and negative x position
                xPosition += (turtle.window_width() * self.div[0]) / (2 * self.scale[0])
            #Loops through every y div position and draws a line
            yPosition = 0
            while yPosition <= turtle.window_height() / 2:
                #Draws a div line at a negative and position x position
                self.graphTurtle.setpos(turtle.window_width() / 2, yPosition)
                self.graphTurtle.pendown()
                self.graphTurtle.setx(-turtle.window_width() / 2)
                self.graphTurtle.penup()
                self.graphTurtle.setx(0)
                self.graphTurtle.write(round((yPosition * 2 * self.scale[1]) / turtle.window_height(), 3), font=("Arial", 12, "normal"))

                self.graphTurtle.setpos(turtle.window_width() / 2, -yPosition)
                self.graphTurtle.pendown()
                self.graphTurtle.setx(-turtle.window_width() / 2)
                self.graphTurtle.penup()
                self.graphTurtle.setx(0)
                if yPosition > 0: self.graphTurtle.write(round((-yPosition * 2 * self.scale[1]) / turtle.window_height(), 3), font=("Arial", 12, "normal"))

                #Sets the next positive and negative x position
                yPosition += (turtle.window_height() * self.div[1]) / (2 * self.scale[1])

if __name__ == "__main__":
    graph = Graph(scale=(10, 100), div=(1, 10))
    for i in range(-100, 100):
        graph.plot(i / 10, ((i / 10) ** 3) + ((i / 10) ** 2) + (i / 10) + 10)
    turtle.update()
    input()
