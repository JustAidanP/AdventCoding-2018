import turtle, random, time, math
from Vector import *

#Defines a Boid object
class Boid:
    #------Initialiser------
    #Initialises Boid, asking for a position, velocity and acceleration
    def __init__(self, position=Vector.zero(), velocity=Vector.zero(), acceleration=Vector.zero(), checkDist=1, checkAngle=270):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.checkDist = checkDist
        self.checkAngle = checkAngle
        #Creates the turtle
        self.boidTurtle = turtle.Turtle()
        self.boidTurtle.penup()

    #------Methods/Functions------
    #Updates the Boid
    def update(self):
        #Adds the velocity to the position and acceleration to velocity to emulate movement
        self.position += self.velocity
        if self.velocity.magnitude() < 10:
            self.velocity += self.acceleration
    #Checks if another boid is in the neighbourhood of this boid
    def checkNeighbourhood(self, flock):
        neighbourhood = []
        #Checks which boids are in the neighbourhood
        for boid in flock:
            if boid.position == self.position: continue
            if (boid.position - self.position).magnitudeSquared() <= self.checkDist ** 2: neighbourhood.append(boid)
        if len(neighbourhood) == 0: return
        #------Alignment------
        #Calculates the average velocity of the boids in the neighbourhood
        averageVelocity = Vector.zero()
        for boid in neighbourhood: averageVelocity += boid.velocity
        averageVelocity /= len(neighbourhood)
        #Steers the boid towards the average velocity
        angleVector = (averageVelocity - self.velocity)
        angleVector /= angleVector.magnitude()
        self.acceleration = angleVector / 100
        return
    #Sets the position turtle
    def show(self):
        self.boidTurtle.setpos(self.position.x, self.position.y)

#Defines a flock object
class Flock:
    #------Initialiser------
    #Initialises Flock, creating all of the boids
    def __init__(self, seedPoint=Vector(0, 0)):
        #Defines the area that the flock is created
        self.seedPoint = seedPoint
        #Creates a list of boids
        self.boids = [self.createBoid() for boid in range(10)]


    #------Methods/Functions------
    #Creates a boid
    def createBoid(self):
        boid = Boid(position=self.seedPoint, velocity=Vector(random.random(), random.random()) * 2)
        return boid
    #Updates all boids and followd boid behaviours
    def update(self):
        for boid in self.boids:
            boid.update()
            boid.checkNeighbourhood(self.boids)
            boid.show()

if __name__ == "__main__":
    turtle.Screen()
    turtle.tracer(0, 0)
    flock = Flock(Vector(0, 0))
    while True:
        flock.update()
        turtle.update()
        time.sleep(0.01)
