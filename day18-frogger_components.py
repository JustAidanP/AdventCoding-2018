from Vector import *
import turtle, math, time, random
#Defines an object that can be placed on the road
class Collider:
    #------Initialiser------
    #initialises the collider, takes a position, velocity and size
    def __init__(self, position=Vector.zero(), velocity=Vector.zero(), size=Vector.zero(), spawnThreshold=150):
        self.position = position
        self.velocity = velocity
        self.size = size
        self.spawnThreshold = spawnThreshold
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
        #Draws a rectangle at the collider's position
        self.colliderTurtle.penup()
        #Top Left
        self.colliderTurtle.setpos(self.position.x - (self.size.x / 2), self.position.y + (self.size.y / 2))
        self.colliderTurtle.pendown()
        #Top Right
        self.colliderTurtle.setpos(self.position.x + (self.size.x / 2), self.position.y + (self.size.y / 2))
        #Bottom Right
        self.colliderTurtle.setpos(self.position.x + (self.size.x / 2), self.position.y - (self.size.y / 2))
        #Bottom Left
        self.colliderTurtle.setpos(self.position.x - (self.size.x / 2), self.position.y - (self.size.y / 2))
        #Top Left
        self.colliderTurtle.setpos(self.position.x - (self.size.x / 2), self.position.y + (self.size.y / 2))
    #Detects if the collider has gone off of the screen
    def detectEdge(self):
        # if math.fabs(self.position.x) >= turtle.window_width() / 2:
        if self.position.x <= -turtle.window_width() / 2:
            self.isDead = True
            self.colliderTurtle.clear()
    #Detects if the collider has reached a boundary to spawn another
    def spawnBoundary(self):
        return self.position.x  <  turtle.window_width() - self.spawnThreshold
    #Detects a collision with the player's x position
    def detectPlayerCollision(self, x):
        return
    #Updates the collider, takes a y position
    def update(self, delta, yPos):
        self.position.y = yPos
        #Updates the position depending on the velocity
        self.position += self.velocity * delta
        #Clears the turtle's previous drawings
        self.colliderTurtle.clear()
        #Draws the turtle
        self.drawTurtle()
#Defines an instance that manages every collider
class Road:
    #------Initialiser-------
    #Initialises the road with a y position, roadHeight, collider movement direction as a bool (for right) and collider x seperation
    def __init__(self, yPos, roadHeight, collGoRight, collSeperation):
        self.yPos = yPos
        self.roadHeight = roadHeight
        self.collGoRight = collGoRight
        self.collSeperation = collSeperation
        #Keeps track of the elapsed time
        self.elapsedTime = 0
        #Creates the initial collider
        self.colliders = []
        self.createCollider(turtle.window_width() - 10)
    #------Methods/Functions------
    #Creates a collider
    def createCollider(self, xPos):
        self.colliders.append(Collider(position=Vector((-turtle.window_width() / 2) + xPos + random.randint(0, 100), 0), velocity=Vector(-350, 0), size=Vector(self.roadHeight, self.roadHeight), spawnThreshold=self.collSeperation))
    #Detects a collision with the player
    def detectPlayer(self, position, size):
        for collider in self.colliders:
            #Detects if the player and collider intersect
            #Detects x
            xIntersect = collider.position.x - (collider.size.x / 2) <= position.x - (size.x / 2) and collider.position.x + (collider.size.x / 2) >= position.x + (size.x / 2)
            #Detects y
            yIntersect = collider.position.y - (collider.size.y / 2) <= position.y - (size.y / 2) and collider.position.y + (collider.size.y / 2) >= position.y + (size.y / 2)
            if xIntersect and yIntersect: return True
        return False
    #Clears all colliders from the screen
    def clear(self): 
        for collider in self.colliders: collider.colliderTurtle.clear()
    #Updates all colliders
    def update(self, delta):
        #Holds the number of colliders that have been deleted
        collidersDeleted = 0
        self.elapsedTime += delta
        for index, collider in enumerate(self.colliders):
            #Passes the collider if it is dead
            if collider.isDead: continue
            #Updates the turtle
            collider.update(delta, self.yPos)
            #Detects an edge of the screen for the collider
            collider.detectEdge()
            #Delets the collider if it is now dead
            if collider.isDead:
                self.colliders.pop(index - collidersDeleted)
                collidersDeleted += 1

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
