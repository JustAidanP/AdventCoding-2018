import random
from Vector import Vector
#A simple class to estimate pi
class PiEstimator:
    #------Initialiser------
    def __init__(self):
        #Defines how many points are in the circle and in total
        self.pointsInCircle = 0
        self.totalPoints = 0
        #Calculates pi
        for i in range(100000000):
            self.createPoint()
            #Prints the current value of pi every 100000 iterations
            if self.totalPoints % 100000 == 0:
                print(self.calculatePi())
        print(self.calculatePi())

    #------Methods/Functions------
    #Creates a point and checks if it is in the circle
    def createPoint(self):
        #Randomly creates a point between -1 and 1 for both x and y
        point = Vector(random.random()*2-1, random.random()*2-1)
        #Checks if the point is contained within the circle
        if point.magnitudeSquared() <= 1:
            #Iterates the pointsInCircle value
            self.pointsInCircle += 1
        #Iterates the totalPoints value
        self.totalPoints += 1
    #Calculates pi with the current information
    def calculatePi(self):
        #Calcuates pi and returns it
        return 4 * (self.pointsInCircle / self.totalPoints)
if __name__ == "__main__":
    PiEstimator()
