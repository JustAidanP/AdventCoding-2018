from Grapher import Graph
from Vector import Vector
import turtle

#Defines a Plotter object, defines how an equation should be plotted on a graph
class Plotter:
    #------Initialiser------
    #Requires a range (this defines the range of values that the plotter is for), step (the rate at which the range is stepped through)
    #And requires a function which creates every point
    def __init__(self, range=(-1, 1), step=0.1, equation=lambda x:x):
        self.range = range
        self.step = step
        self.equation = equation

    #------Methods/Functions------
    #Returns a list of vectors of points to plot
    def createPoints(self):
        points = []
        #Creates a reference position
        xPosition = self.range[0]
        #Creates all points in range with the step rate, with the x and y position
        while xPosition <= self.range[1]:
            points.append(Vector(xPosition, self.equation(xPosition)))
            xPosition += self.step
        return points

if __name__ == "__main__":
    graph = Graph(scale=(100, 100), div=(10, 10))
    plotter = Plotter(range=(-100, 100), equation=lambda x: 2 * x)
    graph.plotPlotter(plotter)
    turtle.update()
    input()
