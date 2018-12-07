#A class that can be called to calculate a sum from sigma notation
class Sum:
    #------Initialisers------
    #Calcutes the sum of all natural numbers defines by the user
    def __init__(self, startingNo, upTo, formula):
        self.startingNo = startingNo
        self.upTo = upTo
        self.formula = formula
        print(self.calculateSum())

    #------Methods/Functions------
    #Calculates the sum
    def calculateSum(self):
        #Define sthe variables that holds the total sum calculated
        totalSum = 0
        for i in range(self.startingNo, self.upTo + 1):
            totalSum += self.formula(i)
        return totalSum

if __name__ == "__main__":
    #Calculates the sum of odd numbers between 0 and 40
    Sum(0, 20, lambda x: 2 * x - 1)
