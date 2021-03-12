#Calculates eulers constnat
class EulerConstant:
    #------Initialiser------
    #Defines how many attempts should be taken to calculate eulars constant
    def __init__(self, attempts):
        self.attempts = attempts

    #------Methods/Functions------
    #Calculates the factorial of a number
    #Uses a loop to bypass recursive limit
    def factorial(self, n):
        #Defines the total factorial
        sum = 1
        for i in range(n, 0, -1):
            sum *= i
        return sum
    #Calculates the eulars constant
    def calculate(self):
        #Defies the eularsConstant
        eulersConstant = 0
        #Calculates eulers constant by finding the sum of the inverse of factorials
        for i in range(self.attempts):
            eulersConstant += 1 / self.factorial(i)
        return eulersConstant

if __name__=="__main__":
    eular = EulerConstant(100)
    print(eular.calculate())
