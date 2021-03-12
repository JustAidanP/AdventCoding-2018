# AdventCoding
Every day for December 2018, a new piece of code is aimed to be uploade.  
All code is written in python and is purely a chance to try out some ideas that I've never had the time for before.  

## Note (from the future)
I'd never recommend anyone use any of this code, it was just an exercise to try out some ideas. 
This was never about code quality (which is fairly clear, e.g. lack of PEP8 styling) but it was a fun project to partake in,
I hope to be able to do another project similar to this in the future.  

# Day 1, Vector:  
    -A vector class  
    -Operates in 2D  
    -Allows for basic vector creation and manipulation  
    
# Day 2, Entity:  
    -An object that implements simplistic physics  
    -Uses the turtle module to display entities in the module  
    -Just click anywhere on the produced screen and a dot will appear with physics  
    -Implements the Vector class from Day 1  
    
# Day 3, Object:  
    -This file contains both a polygon type and mesh type  
    -Will be used and extended on a later day for use in another project  
    
# Day 4, Button:  
    -An object that defines a button  
    -It requires a top left corner origin, a size and an outlet function in order to work  
    -Uses turtle and the Vector class from Day 1  
    
# Day 5, Fractals (Sierpinski Triangle):  
    -Creates a sierpinski triangle  
    -It randomly chosses between 3 seed points, moves halfway there, places a dot and repeats  
    -Uses python's turtle module 
    
# Day 6, PiEstimator:  
    -Estimates pi using randomly generated positions  
    -Uses an Updated Vector class from Day 1 that returns a sqaured magnitude  
    
# Day 7, SumOf (Series):  
    -An object that can calculate the sum of a formula with a start point and end point  
    -The formula is defined as a lambda in python  
    -Emulates sigma notation as arguments in a class instance  
    
# Day 8, Grapher:  
    -An object that create a graph with a defined x and y scale using python's turtle  
    -Grid lines(dividers) can be defined with a seperate x and y value  
    -Allows plotting of a plot on the axis  
    
# Day 9, Plotter:  
    -Used in conjunction with Grapher.py from day 8  
    -Creates a list of points between an x range, stepping through this range with a step rate  
    -It returns a list of vectors (Day 1) that contain an x and y to plot  
    -Updated Grapher.py from day 8 to take a Plotter and plot all points from it  
    
# Day 10, MouseTracer:  
    -A program that traces the mouse with dots on a turtle window  
    -Uses the turtle module to trace the mouse  
    
# Day 11 - Boid:  
    -An object that emulates flocking  
    -A flock of boids use the boid algorithm's alignment to emulate flocking  
    -Depends on turtle and Vector from Day 1  
    
# Day 12, Tree:  
    -An object that will place a tree on a turtle window  
    -Has a customisable component size and position  
    -Uses python's turtle  
    
# Eldrad Must Live! :)  
 
# Day 13, EulersConstant:  
    -Calculates eulers constant using no external library  
    -Uses a custom non recursive factorial function to bypass recursive limit  
    
# Day 14, Hangman:  
    -Runs a text based hangman game  
    -Asks for a target word and accepts input for approach to the target word  
    
# Day 15, VowelIdentifier:  
    -Seperates a given piece of text into the vowels  
    -Gives a new string that just contains the vowels  
    -Also gives the number of times each vowel appeared in the text  
    
# Day 16, ConsonantIdentifier:  
    -Updated Day 15 VowelIdentifier to work for lowercase  
    -Seperates a given piece of text in the consonants  
    -Gives a new string that just contains the vowels and their appearance count  
    -Uses ASCII values to identify consonants  
    
# Day 17, DotPattern:  
    -Creates a fractal pattern of dots with python's turtle  
    -Creates a pattern that will fill the turtle screen  

# Day 18, FroggerComponents:  
    -The beginnings of the components required for a frogger game  
    -Uses python's turtle  
    -Includes collider and road objects for frogger, uses Vector from Day 1  
    
# Day 19, Ellipse:  
    -Defines an object that creates an ellipse of a defined size and position  
    -Can be placed on a screen with a varying level of detail (how many sides to draw)  
    -Uses python's turtle and Vector from Day 1  
    
# Day 20, Player:  
    -An object that can be created for the user to control  
    -Allows text based input to move the player on the screen  
    -Uses python's turtle and Vector from Day 1  
    
# Day 21, Frogger:  
    -A quick and abstracted version of the game Frogger  
    -Updated FroggerComponents from Day 18 and Player from Day 20 to work with the game  
    -Control a moveable character in a frogger instance with colliders getting in the way  
    -Uses python's turtle, FroggerComponents from Day 18, Player from Day 20 and Vector from Day 1  
    
# Day 22, SimultaneousEquation:    
    -Solves a system of equations using matricies  
    -Gets an input from the user of the number of unknowns, coefficients and equal to for each equation  
    -Returns the solutions for each unknown  
    
# Day 23, PoissonDistribution:  
    -An object that deinfes a poisson distribution  
    -Can be created for statistical distribution when a lambda is given  
    -Can get probability, cumulative probability, mean, variance, s.d and allows addition of distributions  
    
# Final Day 24, Renderer:  
    -Updated Vector from Day 1 to include 3d vectors with included support for dot product and cross product  
    -Updated Object from Day 3 to have a Node class that defines a node in a renderer  
    -Renderer is a 3D perspective renderer that can project 3D points into 2D space  
    -Currently has limited functionality and lacks culling however support will be introduced over the months  
    -Includes a basic way to show nodes in 3D space, nodes are attached to a scene which then renders these every frame  
    -Includes GameManager, Renderer, Scene, Polygon, Mesh and Node  
