import numpy
#Deinfes a polygon that uses numpys vector attribute
class Polygon:
    #------Initialiser------
    def __init__(self, points):
        if len(points) != 3:
            print("Polygon doesn't have 3 points")
            return
        self.points = points
#Defines a mesh that stores a set of polygons
class Mesh:
    #------Initialiser------
    def __init__(self, polygons):
        self.polygons = polygons
