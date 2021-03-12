from Vector import *
import time, turtle, random
#An object that is in a physical world, abiding by simplistic 2 dimensional physics
class Entity:
    #------Initialiser------
    #Defines the Entities attributes
    def __init__(self, radius=1, position=Vector.zero(), velocity=Vector.zero(), acceleration=Vector.zero()):
        self.radius = radius
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        #Tells the physics engine whether the entity is dead
        self.isDead = False
        self.colour = (random.random(), random.random(), random.random())

        #Sets up the entities turtle
        self.particle = turtle.Turtle()
        self.particle.hideturtle()
        self.particle.penup()

    #------Methods/Functions------
    #Defines the update method that is called by the renderer
    def update(self):
        #Adjusts the position and velocity depending on the acceleration
        self.velocity += self.acceleration
        self.position += self.velocity
        self.detectEdge()
        self.detectCollision()
        self.draw()
    #Detects if the entity has left the screen
    def detectEdge(self):
        if math.fabs(self.position.x) >= Main.canvasSize.x / 2:
            self.velocity.x *= -1
            self.acceleration.x *= -1
        if self.position.y >= Main.canvasSize.y / 2:
            self.velocity.y *= -1
        if self.position.y <= -Main.canvasSize.y / 2:
            self.velocity.y *= -1
    #Detects whether there has been a collision with the entity
    def detectCollision(self):
        #Loops through every entity to detect a collision
        for entity in Main.entities:
            if entity.position == self.position: continue
            if (self.position.x - entity.position.x) ** 2 + (self.position.y - entity.position.y) ** 2 <= (self.radius + entity.radius) ** 2:
                #Responds to the collision
                self.velocity.x *= -1
                self.velocity.y *= -1
                self.acceleration.x *= -1
    #Draws a position on the screen of the entity
    def draw(self):
        self.particle.clear()
        self.particle.setpos((self.position.x, self.position.y))
        self.particle.dot(2*self.radius, self.colour)

class Main:
    #------Variables------
    #Stores all of the entities
    entities = []
    #Defines the canvas size
    canvasSize = Vector(2000, 2000)

    #------Initialiser------
    def __init__(self):
        #Creates the turtle screen and sets it up
        turtle.Screen()
        turtle.tracer(0, 0)
        turtle.setworldcoordinates(-Main.canvasSize.x/2, -Main.canvasSize.y/2, Main.canvasSize.x/2, Main.canvasSize.y/2)
        #Defines the method called on click
        turtle.onscreenclick(Main.createEntity)
        #Creates an initial starting entity
        Main.entities.append(Entity(radius=10, position=Vector.zero(), velocity=Vector(0, 5), acceleration=Vector(0, -0.098)))
        while True:
            #Loops through every entity and updates it, if it is alive
            for entity in Main.entities:
                if entity.isDead == False:
                    entity.update()
            #Updates the screen
            turtle.update()
            #Waits until the next frame
            time.sleep(0.005)
    #------Methods/Functions------
    #Creates a new entity at the position
    def createEntity(x, y):
        Main.entities.append(Entity(radius=10, position=Vector(x, y), velocity=Vector(random.random() * 2 - 1, random.random()) * 10, acceleration=Vector(0, -0.098)))

if __name__ == "__main__":
    Main()
    input()
