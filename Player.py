import turtle
from Vector import *
#Defines a player object
class Player:
    #------Variables-------
    movementStepSize = 20
    #------Initialiser------
    #Creates the player, takes in a position, size and a turtle screen
    def __init__(self, position=Vector.zero(), size=Vector.zero(), screen=None):
        self.position = position
        self.size = size
        #Creates the player's turtle
        self.createTurtle()
        #Draws the turtle at an initial position
        self.drawPlayer()
        #Sets up character detection
        screen.onkey(self.moveUp, "w")
        screen.onkey(self.moveLeft, "a")
        screen.onkey(self.moveDown, "s")
        screen.onkey(self.moveRight, "d")
        screen.listen()
    #------Methods/Functions------
    #Creates the player turtle
    def createTurtle(self):
        self.playerTurtle = turtle.Turtle()
        #Sets up the turtle
        self.playerTurtle.penup()
        self.playerTurtle.hideturtle()
    #Draws the player
    def drawPlayer(self):
        self.playerTurtle.clear()
        self.playerTurtle.setpos(self.position.x, self.position.y)
        self.playerTurtle.dot(self.size.x)
    #------Player Movement------
    #Moves the player up
    def moveUp(self):
        self.position.y += Player.movementStepSize
        self.drawPlayer()
    #Moves the player left
    def moveLeft(self):
        self.position.x -= Player.movementStepSize
        self.drawPlayer()
    #Moves the player down
    def moveDown(self):
        self.position.y -= Player.movementStepSize
        self.drawPlayer()
    #Moves the player right
    def moveRight(self):
        self.position.x += Player.movementStepSize
        self.drawPlayer()