import turtle
from Vector import *
#Defines a player object
class Player:
    #------Initialiser------
    #Creates the player, takes in a position, size, a turtle screen and a boolean to determine whether to take user input
    def __init__(self, position=Vector.zero(), size=Vector.zero(), stepRate=20, screen=None, takeInput=True):
        self.position = position
        self.size = size
        self.movementStepSize = stepRate
        #Creates the player's turtle
        self.createTurtle()
        #Draws the turtle at an initial position
        self.drawPlayer()
        if takeInput:
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
        #Draws a rectangle at the player's position
        self.playerTurtle.penup()
        #Top Left
        self.playerTurtle.setpos(self.position.x - (self.size.x / 2), self.position.y + (self.size.y / 2))
        self.playerTurtle.pendown()
        #Top Right
        self.playerTurtle.setpos(self.position.x + (self.size.x / 2), self.position.y + (self.size.y / 2))
        #Bottom Right
        self.playerTurtle.setpos(self.position.x + (self.size.x / 2), self.position.y - (self.size.y / 2))
        #Bottom Left
        self.playerTurtle.setpos(self.position.x - (self.size.x / 2), self.position.y - (self.size.y / 2))
        #Top Left
        self.playerTurtle.setpos(self.position.x - (self.size.x / 2), self.position.y + (self.size.y / 2))
    #------Player Movement------
    #Moves the player up
    def moveUp(self):
        self.position.y += self.movementStepSize
        self.drawPlayer()
    #Moves the player left
    def moveLeft(self):
        self.position.x -= self.movementStepSize
        self.drawPlayer()
    #Moves the player down
    def moveDown(self):
        self.position.y -= self.movementStepSize
        self.drawPlayer()
    #Moves the player right
    def moveRight(self):
        self.position.x += self.movementStepSize
        self.drawPlayer()
