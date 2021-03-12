import numpy, copy, random
from Vector import *
#Deinfes a polygon that uses numpys vector attribute
class Polygon:
    #------Initialiser------
    def __init__(self, verticies):
        # if len(verticies) != 3:
        #     print("Polygon doesn't have 3 verticies")
        #     return
        self.verticies = verticies
#Defines a mesh that stores a set of polygons
class Mesh:
    #------Initialiser------
    def __init__(self, polygons):
        self.polygons = polygons
#Defines a node that contains a mesh, handles all logic for a component
class Node:
    #------Initialiser------
    #Creates a node, requires a mesh, position, eulerRotation and scale
    def __init__(self, mesh, position=Vector3D.zero(), eulerRotation=Vector3D.zero(), scale=Vector3D(1, 1, 1)):
        #Sets up the initial variables
        self.mesh = mesh
        self.position = copy.copy(position)
        self.eulerRotation = copy.copy(eulerRotation)
        self.scale = copy.copy(scale)
    #------Methods/Functions------
    #Updates the node
    def update(self):
        return
    #Sets the euler rotation of the node
    def setEulerRotation(self, rotation=Vector3D.zero()):
        self.eulerRotation = rotation
    #Sets the position of the node
    def setPosition(self, position=Vector3D.zero()):
        self.position = position
    #Creates a cube mesh of size 0
    def createCube():
        #Creates a list of possible verticies
        corners = [#Front Face
            [0, 0, 0], [0, 1, 0], [1, 1, 0], [1, 0, 0],
            #Back Face
            [0, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 1]]
        return Mesh(polygons=[#Front Face
                    Polygon(verticies=numpy.array([corners[0], corners[1], corners[2]]).T),
                    Polygon(verticies=numpy.array([corners[0], corners[2], corners[3]]).T),
                    #Back Face
                    Polygon(verticies=numpy.array([corners[7], corners[6], corners[5]]).T),
                    Polygon(verticies=numpy.array([corners[7], corners[5], corners[4]]).T),
                    #Left Face
                    Polygon(verticies=numpy.array([corners[4], corners[5], corners[1]]).T),
                    Polygon(verticies=numpy.array([corners[4], corners[1], corners[0]]).T),
                    #Right Face
                    Polygon(verticies=numpy.array([corners[3], corners[2], corners[6]]).T),
                    Polygon(verticies=numpy.array([corners[3], corners[6], corners[7]]).T),
                    #Top Face
                    Polygon(verticies=numpy.array([corners[1], corners[5], corners[6]]).T),
                    Polygon(verticies=numpy.array([corners[1], corners[6], corners[2]]).T),
                    #Bottom Face
                    Polygon(verticies=numpy.array([corners[7], corners[4], corners[0]]).T),
                    Polygon(verticies=numpy.array([corners[7], corners[0], corners[3]]).T),
                    ])
        
    #------Render Specific Methods/Functions------
    #Returns the mesh with all transformation applied
    def getMesh(self):
        #Copies the mesh
        transformedMesh = copy.deepcopy(self.mesh)
        #Applies transformations to the mesh
        for polygon in transformedMesh.polygons:
            #Applies scale transform
            if self.scale != 1: polygon.verticies = (polygon.verticies.T * numpy.array([self.scale.x, self.scale.y, self.scale.z])).T
            #Applies rotational transformations
            polygon.verticies = Node.renderRotateX(polygon.verticies, self.eulerRotation.x)
            polygon.verticies = Node.renderRotateY(polygon.verticies, self.eulerRotation.y)
            polygon.verticies = Node.renderRotateZ(polygon.verticies, self.eulerRotation.z)
            for verticy in polygon.verticies.T:
                #Applies position transformation
                verticy[0] += self.position.x
                verticy[1] += self.position.y
                verticy[2] += self.position.z
        return transformedMesh
    #Rotates the vector about x by angle degress in RADIANS
    def renderRotateX(polygon, xRotation):
        rotationX = numpy.array([[1, 0, 0],
                            [0, math.cos(xRotation), -math.sin(xRotation)],
                            [0, math.sin(xRotation), math.cos(xRotation)]])
        return rotationX @ polygon
    #Rotates the vector about y by angle degress in RADIANS
    def renderRotateY(polygon, yRotation):
        rotationY = numpy.array([[math.cos(yRotation), 0, math.sin(yRotation)],
                            [0, 1, 0],
                            [-math.sin(yRotation), 0, math.cos(yRotation)]])
        return rotationY @ polygon
    #Rotates the vector about z by angle degress in RADIANS
    def renderRotateZ(polygon, zRotation):
        rotationZ = numpy.array([[math.cos(zRotation), -math.sin(zRotation), 0],
                            [math.sin(zRotation), math.cos(zRotation), 0],
                            [0, 0, 1]])
        return rotationZ @ polygon