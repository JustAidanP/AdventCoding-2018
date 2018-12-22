import numpy, math
#An instance that can be called to ask for and solve a simultaneous equation
class SimultaneousEquation:
    #------Initialiser------
    def __init__(self):
        #Gets the simultaneous equations
        self.getInput()
        #Solves the equations
        self.solve()
    #------Methods/Functions------
    #Gets the simultaneous equation from the user
    def getInput(self):
        #Asks for the number of unknowns from the user
        self.unknowns = input("Number of unknowns: ")
        while not self.unknowns.isnumeric():
            self.unknowns = input("Has to be a positive number: ")
        self.unknowns = int(self.unknowns)
        #Sets up the matricies
        self.setUpMatricies(self.unknowns)
        #Asks for an equation for every unknown
        for outer in range(self.unknowns):
            #Asks for coefficients for every unknown and what the equation is equal to
            for inner in range(self.unknowns + 1):
                #Asks for what the equation is equal to after all coefficients for unknown are gathered
                if inner == self.unknowns:
                    equalTo = input("Equation is equal to: ")
                    while not self.checkNumber(equalTo):
                        equalTo = input("Equation is equal to: ")
                    equalTo = float(equalTo)
                    self.equalToMatrix[outer][0] = equalTo
                else:
                    coefficient = input("Coefficient %s: "%(inner+1))
                    while not self.checkNumber(coefficient):
                        coefficient = input("Coefficient %s: "%(inner+1))
                    coefficient = float(coefficient)
                    self.coefficientsMatirx[outer][inner] = coefficient
    #Checks if the input is a number
    def checkNumber(self, number):
        try:
            foo = float(number)
            return True
        except: return False
    #Sets up the matricies
    def setUpMatricies(self, size):
        self.coefficientsMatirx = numpy.zeros(shape=(size, size))
        self.equalToMatrix = numpy.zeros(shape=(size, 1))
    #Solves the matricies
    def solve(self):
        #Checks if the equation is solvable
        if numpy.linalg.det(self.coefficientsMatirx) == 0: print("Simultaneous equation has no one solution"); return
        #Solves the simutaneous equations
        solutions = numpy.linalg.inv(self.coefficientsMatirx) @ self.equalToMatrix
        #Prints out the solutions
        for i in range(len(solutions)):
            print("Unknown %s = %s"%(i+1, round(solutions[i][0], 4)))
        return solutions
        
if __name__=="__main__":
    simul = SimultaneousEquation()