import turtle
from Vector import Vector
#A button object that can be placed anywhere on a screen
class Button:
    #------Initialiser------
    #Creates the button, asks for a size and origin, origin being the top left corner
    #The onClick defines what function is called when the button is clicked
    def __init__(self, size, origin, onClick):
        self.size = size
        self.origin = origin
        self.onClick = onClick
        self.draw()

    #------Methods/Functions------
    #Draws the button
    def draw(self):
        buttonTurtle = turtle.Turtle()
        buttonTurtle.hideturtle()
        buttonTurtle.penup()
        #Sets the initial position
        buttonTurtle.setpos(self.origin.x, self.origin.y)
        buttonTurtle.pendown()
        #Draws the top side
        buttonTurtle.setx(self.origin.x + self.size.x)
        #Draws the right side
        buttonTurtle.sety(self.origin.y - self.size.y)
        #Draws the bottom side
        buttonTurtle.setx(self.origin.x)
        #Finishes the button
        buttonTurtle.setpos(self.origin.x, self.origin.y)

    #Checks if the click location is in bounds
    def checkClick(self, x, y):
        #Calculates whether the x position is in bounds
        isXInBounds = x >= self.origin.x and x <= self.origin.x + self.size.x
        isYInBounds = y <= self.origin.y and y >= self.origin.y - self.size.y
        if isXInBounds and isYInBounds:
            #Runs the defined function
            self.onClick()

#------Example Code------
#Stores every button
buttons = []

#This is where the buttons functionality goes
def buttonFunctionality():
    print("Button Clicked")

#Checks every button for input
def checkClick(x, y):
    for button in buttons:
        button.checkClick(x, y)

if __name__ == "__main__":
    #Creates the turtle screen and sets it up
    turtle.Screen()
    turtle.tracer(0, 0)
    #Creates a button
    button = Button(size=Vector(x=100, y=20), origin=Vector(x=20, y=20), onClick=buttonFunctionality)
    #Updates hte screen with the buttons
    turtle.update()
    #Adds the button to the list of buttons
    buttons.append(button)
    #Defines the method called on click
    turtle.onscreenclick(checkClick)
    input()
