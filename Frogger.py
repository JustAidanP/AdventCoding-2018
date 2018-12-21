from Vector import *
from Player import *
from FroggerComponents import *
import turtle, math, time

#Defines an instance of a game that handles it
class GameManager:
    #------Initialiser------
    def __init__(self):
        self.roads = []
        #Stores the number of empty and full roads the player has passed
        self.roadsPassed = 0
        #Determines whether the game is running
        self.playing = True
        #Defines the height of the roads
        #Influences the collider sizes, road intervals and player size
        self.roadHeight = 50
        #Defines whether the player is currently on an active road
        self.onRoad = False
        #Sets up the game
        self.setUp()
        self.createPlayer()
        self.createRoad(-150 + self.roadHeight)
        for i in range(4):
            self.createRoad(self.roads[-1].yPos + self.roadHeight * 2)
        self.run()
    #------Methods/Functions------
    #Sets up the screen
    def setUp(self):
        #Sets up the turtle screen
        self.screen = turtle.Screen()
        turtle.tracer(0, 0)
        #Sets up the score turtle
        self.scoreTurtle = turtle.Turtle()
        self.scoreTurtle.penup()
        self.scoreTurtle.hideturtle()
        self.scoreTurtle.setpos(-turtle.window_width() / 2 + 80, turtle.window_height() / 2 - 80)
        #Writes inital score to screen
        self.displayScore()
        #Sets up user input
        self.screen.onkey(self.moveUp, "w")
        self.screen.onkey(self.moveLeft, "a")
        self.screen.onkey(self.moveRight, "d")
        self.screen.listen()
    #Creates the game's player
    def createPlayer(self):
        self.player = Player(position=Vector(0, -150), size=Vector(self.roadHeight * 0.75, self.roadHeight * 0.75), stepRate=50, screen=self.screen, takeInput=False)
    #Creates a new road
    def createRoad(self, yPos):
        self.roads.append(Road(yPos, self.roadHeight, 0, 650))
    #Displays the player's score
    def displayScore(self):
        self.scoreTurtle.clear()
        self.scoreTurtle.write("Score: %s"%(self.roadsPassed), font=("Arial", 40, "bold"))
    #Runs the game
    def run(self):
        #Creates the main loop, keeping tack of delta time
        prevTime = time.time()
        while self.playing:
            #Works out the delta time
            curTime = time.time()
            deltaTime = curTime - prevTime
            prevTime = curTime
            #Updates components
            self.updateComponents(deltaTime)
            #Sets the title of the window to the current frame rate
            if deltaTime != 0: turtle.title("Frame Rate: " + str(round(1 / deltaTime, 2)))
            #Updates the turtle screen
            turtle.update()
    def updateComponents(self, delta):
        for index, road in enumerate(self.roads):
            if index >= (self.roadsPassed - 1) // 2: 
                road.update(delta)
            #Detects a collision with the player, expects a bool
            if self.roads[self.roadsPassed // 2].detectPlayer(self.player.position, self.player.size): self.playing = False
    #------User Input------
    #Moves the game up
    def moveUp(self):
        self.onRoad = not self.onRoad
        if self.onRoad: self.createRoad(self.roads[-1].yPos + self.roadHeight * 2)
        for road in self.roads:
            road.yPos -= self.roadHeight
        #Detects if the player is on a road and clears the passed road
        if self.onRoad:
            self.roads[(self.roadsPassed - 1) // 2].clear()
        self.roadsPassed += 1
        #Displays the score
        self.displayScore()
    #Moves the game left
    def moveLeft(self):
        self.player.moveLeft()
    #Moves the game right
    def moveRight(self):
        self.player.moveRight()

if __name__=="__main__":
    GameManager()
    input()