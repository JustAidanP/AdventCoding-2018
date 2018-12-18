from Vector import *
import turtle, math, time
#Defines an object that can be placed on the road
class Collider:
    #------Initialiser------
    #initialises the collider, takes a position, velocity and size
    def __init__(self, position=Vector.zero(), velocity=Vector.zero(), size=Vector.zero()):
        self.position = position
        self.velocity = velocity
        self.size = size
        self.isDead = False
        #Creates the collider's turtle
        self.createTurtle()
        
    #------Methods/Functions------
    #Creates the collider's turtle
    def createTurtle(self):
        self.colliderTurtle = turtle.Turtle()
        #Sets up the turtle
        self.colliderTurtle.penup()
        self.colliderTurtle.hideturtle()

    #Draws the turtle at the current position
    def drawTurtle(self):
        self.colliderTurtle.setpos(self.position.x, self.position.y)
        self.colliderTurtle.dot(self.size.x)
    #Detects if the collider has gone off of the screen
    def detectEdge(self):
        if math.fabs(self.position.x) >= turtle.window_width() / 2:
            self.isDead = True
    #Detects if the collider has reached a boundary to spawn another
    def spawnBoundary(self):
        return math.fabs(self.position.x)  <  6 * (turtle.window_width() / 2) / 8
    #Detects a collision with the player's x position
    def detectPlayerCollision(self, x):
        return
    #Updates the collider
    def update(self, delta):
        #Updates the position depending on the velocity
        self.position += self.velocity * delta
        #Clears the turtle's previous drawings
        self.colliderTurtle.clear()
        #Draws the turtle
        self.drawTurtle()
#Defines an instance that manages every collider
class Road:
    #------Initialiser-------
    #Initialises the road with a y position, collider movement direction as a bool (for right) and collider x seperation
    def __init__(self, yPos, collGoRight, collSeperation):
        #Keeps track of the elapsed time
        self.elapsedTime = 0
        #Creates the initial collider
        self.colliders = []
        self.createCollider(turtle.window_width() - 10)
    #------Methods/Functions------
    #Creates a collider
    def createCollider(self, xPos):
        self.colliders.append(Collider(position=Vector((-turtle.window_width() / 2) + xPos, 0), velocity=Vector(-350, 0), size=Vector(40, 40)))
    #Updates all colliders
    def update(self, delta):
        self.elapsedTime += delta
        for collider in self.colliders:
            #Passes the collider if it is dead
            if collider.isDead: continue
            #Updates the turtle
            collider.update(delta)
            #Detects an edge of the screen for the collider
            collider.detectEdge()
        #Creates a new collider if the last collider is past the spawn boundary
        if self.colliders[-1].spawnBoundary():
            self.createCollider(turtle.window_width())

if __name__=="__main__":
    #Sets up the turtle screen
    turtle.Screen()
    turtle.tracer(0, 0)
    #Creates a road
    road = Road(0, 0, 150)
    #Creates the main loop, keeping tack of delta time
    prevTime = time.time()
    while True:
        #Works out the delta time
        curTime = time.time()
        deltaTime = curTime - prevTime
        prevTime = curTime
        #Updates the road
        road.update(deltaTime)
        #Sets the title of the window to the current frame rate
        if deltaTime != 0: turtle.title("Frame Rate: " + str(round(1 / deltaTime, 2)))
        #Updates the turtle screen
        turtle.update()
    input()
