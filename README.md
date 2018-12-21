# AdventCoding
Every day a new piece of code is aimed to be uploaded
The code will most often be in python
The aim is to use previous days projects later on in the month to produce something better

Day 1 - 'Vector.py':<br>
    -A vector class<br>
    -Operates in 2D<br>
    -Allows for basic vector creation and manipulation<br>
Day 2 - 'Entity.py':<br>
    -An object that implements simplistic physics<br>
    -Uses the turtle module to display entities in the module<br>
    -Just click anywhere on the produced screen and a dot will appear with physics<br>
    -Implements the Vector class from Day 1<br>
Day 3 - 'Object.py':<br>
    -This file contains both a polygon type and mesh type<br>
    -Will be used and extended on a later day for use in another project<br>
Day 4 - 'Button.py':<br>
    -An object that defines a button<br>
    -It requires a top left corner origin, a size and an outlet function in order to work<br>
    -Uses turtle and the Vector class from Day 1<br>
Day 5 - 'Fractals.py':<br>
    -Creates a sierpinski triangle<br>
    -It randomly chosses between 3 seed points, moves halfway there, places a dot and repeats<br>
    -Uses python's turtle module<br>
Day 6 - 'PiEstimator.py':<br>
    -Estimates pi using randomly generated positions<br>
    -Uses an Updated Vector class from Day 1 that returns a sqaured magnitude<br>
Day 7 - 'SumOf.py':<br>
    -An object that can calculate the sum of a formula with a start point and end point<br>
    -The formula is defined as a lambda in python<br>
    -Emulates sigma notation as arguments in a class instance<br>
Day 8 - 'Grapher.py':<br>
    -An object that create a graph with a defined x and y scale using python's turtle<br>
    -Grid lines(dividers) can be defined with a seperate x and y value<br>
    -Allows plotting of a plot on the axis<br>
Day 9 - 'Plotter.py':<br>
    -Used in conjunction with Grapher.py from day 8<br>
    -Creates a list of points between an x range, stepping through this range with a step rate<br>
    -It returns a list of vectors (Day 1) that contain an x and y to plot<br>
    -Updated Grapher.py from day 8 to take a Plotter and plot all points from it<br>
Day 10 - 'MouseTracer.py':<br>
    -A program that traces the mouse with dots on a turtle window<br>
    -Uses the turtle module to trace the mouse<br>
Day 11 - 'Boid.py':<br>
    -An object that emulates flocking<br>
    -Project will extend multiple days. On day 12, steering behaviours began to be implemented<br>
    -Depends on turtle and Vector from Day 1<br>
Day 12 - 'Tree.py':<br>
    -An object that will place a tree on a turtle window<br>
    -Has a customisable component size and position<br>
    -Uses python's turtle<br>
Eldrad Must Live!<br>
Day 13 - 'EulersConstant.py':<br>
    -Calculates eulers constant using no external library<br>
    -Uses a custom non recursive factorial function to bypass recursive limit<br>
Day 14 - 'Hangman.py':<br>
    -Runs a text based hangman game<br>
    -Asks for a target word and accepts input for approach to the target word<br>
Day 15 - 'VowelIdentifier.py':<br>
    -Seperates a given piece of text into the vowels<br>
    -Gives a new string that just contains the vowels<br>
    -Also gives the number of times each vowel appeared in the text<br>
Day 16 - 'ConsonantIdentifier.py':<br>
    -Updated Day 15 VowelIdentifier to work for lowercase<br>
    -Seperates a given piece of text in the consonants<br>
    -Gives a new string that just contains the vowels and their appearance count<br>
    -Uses ASCII values to identify consonants<br>
Day 17 - 'DotPattern.py':<br>
    -Creates a fractal pattern of dots with python's turtle<br>
    -Creates a pattern that will fill the turtle screen<br>
Day 18 - 'FroggerComponents.py':<br>
    -The beginnings of the components required for a frogger game<br>
    -Uses python's turtle<br>
    -Includes collider and road objects for frogger, uses Vector from Day 1<br>
Day 19 - 'Ellipse.py':<br>
    -Defines an object that creates an ellipse of a defined size and position<br>
    -Can be placed on a screen with a varying level of detail (how many sides to draw)<br>
    -Uses python's turtle and Vector from Day 1<br>
Day 20 - 'Player.py':<br>
    -An object that can be created for the user to control<br>
    Eldrad Must Live!
    -Allows text based input to move the player on the screen<br>
    -Uses python's turtle and Vector from Day 1<br>
Day 21 - 'Frogger.py':<br>
    -A quick and abstracted version of the game Frogger<br>
    -Updated FroggerComponents from Day 18 and Player from Day 20 to work with the game<br>
    -Control a moveable character in a frogger instance with colliders getting in the way<br>
    -Uses python's turtle, FroggerComponents from Day 18, Player from Day 20 and Vector from Day 1<br>
