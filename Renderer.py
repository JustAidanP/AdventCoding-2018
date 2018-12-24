import turtle, math, time, numpy, copy
from Vector import Vector, Vector3D
from Object import Polygon, Mesh, Node
#Defines a scene object
class Scene:
    #------Initialiser------
    def __init__(self):
        self.children = []
    #------Methods/Functions------
    #Adds a child node to the scene
    def addChild(self, node):
        self.children.append(node)
#An object that can be used to render pixels onto a window
class Renderer:
    #------Initialiser------
    def __init__(self):
        #Defines the camera position
        self.cameraPosition = numpy.array([0, 0, 0]).T
        #Creates the projection matrix
        self.createProjMatrix()
        #Sets up turtle for the renderer
        self.setuUpTurtle()
        self.theta = 0

    #------Methods/Functions------
    #Defines projection values and
    #Creates the projection matrix
    def createProjMatrix(self):
        #Defines camera variables
        self.zNear = 0.1
        self.zFar = 1000
        self.fov = 1 / math.atan(math.pi / 2)
        #Calculates the aspect ratio
        self.aspectRatio = turtle.window_height() / turtle.window_width()
        #Creates the projection matrix
        self.projectionMatrix = numpy.array([[self.aspectRatio * self.fov, 0, 0, 0],
                                             [0, self.fov, 0, 0],
                                             [0, 0, self.zFar / (self.zFar - self.zNear), (-self.zFar * self.zNear) / (self.zFar - self.zNear)],
                                             [0, 0, 1, 0]])
    #Creates a turtle for the renderer
    def setuUpTurtle(self):
        turtle.Screen()
        turtle.tracer(0, 0)
        turtle.onscreenclick(self.handleInput)
        self.renderTurtle = turtle.Turtle()
        # self.renderTurtle.penup()
        self.renderTurtle.hideturtle()
        
	#Handles input
    def handleInput(self, x, y):
        if x < 0: self.cameraPosition[0] -= 1
        elif x > 0: self.cameraPosition[0] += 1
    #Renders a mesh
    def renderMesh(self, delta, mesh):
        #Renders every polygon in the mesh
        for polygon in mesh.polygons:
            #Backface Culling
            # polyNormal = numpy.cross(polygon.verticies[1] - polygon.verticies[0], polygon.verticies[2] - polygon.verticies[0])
            self.renderPolygon(polygon=(polygon.verticies))
    #Renders a polygon to the screen
    def renderPolygon(self, polygon):
        #Translates the triangle onto the screen
        for pointIndex in range(len(polygon[2])):
            polygon[2][pointIndex] += 20
        #Adds the camera position to the polygon
        for verticy in polygon.T:
            verticy -= self.cameraPosition.T
        #Adds a fourth element to every verticy that is used for division later
        intermediatePolygon = numpy.insert(polygon.T, 3, 1, axis=1).T
        #Applies the projection matrix to every point
        projectedVerticies = (self.projectionMatrix @ intermediatePolygon).T
        #Divides every projectedVerticies by the fourth element
        for verticy in projectedVerticies:
            if verticy[3] != 0:verticy /= verticy[3]
        #Defines how much each verticy will be scaled by
        scaleFactor = 200
        #Draws the projectedVerticies
        self.renderTurtle.penup()
        self.renderTurtle.setpos(projectedVerticies[0][0] * scaleFactor, projectedVerticies[0][1] * scaleFactor)
        self.renderTurtle.pendown()
        self.renderTurtle.setpos(projectedVerticies[1][0] * scaleFactor, projectedVerticies[1][1] * scaleFactor)
        self.renderTurtle.setpos(projectedVerticies[2][0] * scaleFactor, projectedVerticies[2][1] * scaleFactor)
        self.renderTurtle.setpos(projectedVerticies[0][0] * scaleFactor, projectedVerticies[0][1] * scaleFactor)

#Creates the main game
class GameManager:
    #------Initialiser------
    def __init__(self):
        #Creates a list of nodes in the game, stores it in a scene
        self.scene = Scene()
        # #Creates a cube mesh
        self.scene.addChild(Node(Node.createCube()))
        self.scene.children[0].scale *= 10
        #Creates the scene's renderer
        self.renderer = Renderer()
        #Renders the mesh, keeping tack of detla time
        prevTime = time.time()
        while True:
            #Works out the delta time
            curTime = time.time()
            deltaTime = curTime - prevTime
            prevTime = curTime
            #Sets the title of the window to the current frame rate
            if deltaTime != 0: turtle.title("Frame Rate: " + str(round(1 / deltaTime, 2)))
            #Renders the scene
            self.render(deltaTime)
            #Uodates the turtle screen
            turtle.update()
    #Renders the scene
    def render(self, deltaTime):
        #Clears the render turtles drawing
        self.renderer.renderTurtle.clear()
        #Renders every mesh in the scene
        for node in self.scene.children:
            node.eulerRotation.x += math.pi * 0.5 * deltaTime
            node.eulerRotation.y += math.pi * 0.5 * deltaTime
            node.eulerRotation.z += math.pi * 0.5 * deltaTime
            self.renderer.renderMesh(delta=deltaTime, mesh=node.getMesh())

if __name__ == "__main__":
    GameManager()
    input()
