import math
#A vector object containing an x and y and allowing simple maths
class Vector:
    #------Initialiser------
    def __init__(self, x, y):
        self.x = x
        self.y = y

    #------Methods/Functions------
    #Returns a new vector with default values of 0 or resets the values of the vector to 0
    def zero(self=None):
        if self == None: return Vector(0, 0)
        self.x = 0
        self.y = 0
    #Returns a new Vector with filled values
    def withFill(value=0):
        return Vector(value, value)
    #Fills every value of the Vector with a given value
    def fillValues(value=0):
        self.x = value
        self.y = value
    #Creates a new vector with a scale of 1 that is created from a given angle in RADIANS
    def fromAngle(angle, isRadians=True):
        if isRadians == False: angle=math.radians(angle)
        newX = math.sin(angle)
        newY = math.cos(angle)
        return Vector(newX, newY)
    #Rotates the vector by angle degress in RADIANS
    def rotate(self, angle, isRadians=True):
        if isRadians == False: angle=math.radians(angle)
        rotatedX = (self.x * math.cos(-angle)) - (self.y * math.sin(-angle))
        rotatedy = (self.x * math.sin(-angle)) + (self.y * math.cos(-angle))
        self.x = rotatedX
        self.y = rotatedy
    #Returns the magnitude of the vector
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    #Dupliactes the vector
    def copy(self):
        return Vector(self.x, self.y)

    #------Operators------
    #Overrides the add operator
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x + other, self.y + other)
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
    def __iadd__(self, other):
        return self + other
    #Overrides the sub operator
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x - other, self.y - other)
        if isinstance(other, Vector):
            return Vector(self.x - other.x, self.y - other.y)
    def __isub__(self, other):
        return self - other
    #Overrides the mult operator
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x * other, self.y * other)
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y)
    def __imul__(self, other):
        return self * other
    #Overrides the div operator
    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x / other, self.y / other)
        if isinstance(other, Vector):
            return Vector(self.x / other.x, self.y / other.y)
    def __itruediv__(self, other):
        return self / other
    #Overrides the is equal to operator
    def __eq__(self, other):
        if isinstance(other, (int, float)):
            return self.x == other and self.y == other
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
    #Overrides the not equal to operator
    def __ne__(self, other):
        if isinstance(other, (int, float)):
            return self.x != other and self.y != other
        if isinstance(other, Vector):
            return self.x != other.x and self.y != other.y
    #Overrides the pow operator
    def __pow__(self, other):
        if isinstance(other, (int, float)):
            return Vector(self.x ** other, self.y ** other)
        if isinstance(other, Vector):
            return Vector(self.x ** other.x, self.y ** other.y)

    #Returns a string version of the Vector needed
    def __str__(self):
        return "Vector with x:%s, y:%s"%(self.x, self.y)
    def __getitem__(self, index):
        if index == 0 or index == -2: return self.x
        elif index == 1 or index == -1: return self.y
        else:
            print("Index %s not in vector"&index)
            return None
    def __setitem__(self, index, value):
        if index == 0 or index == -2: self.x = value
        elif index == 1 or index == -1: self.y = value
        else:
            print("Index %s not in vector"&index)
            return None
