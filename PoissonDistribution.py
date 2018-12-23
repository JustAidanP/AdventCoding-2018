import math
#Defines a Poisson Distribution Object
class PoissonDistribution:
    #------Initialiser------
    #Initialises the poisson distribution with the given lambda
    def __init__(self, pLambda):
        self.pLambda = pLambda
    #------Methods/Functions------
    #Returns the mean of the distribution
    def getMean(self):
        return self.pLambda
    #Returns the variance of the distribution
    def getVariance(self):
        return self.pLambda
    #Returns the standard deviation of the distribution
    def getStandardDistribution(self):
        return math.sqrt(self.pLambda)
    #Gets the probability that the distribution will be the discrete random variable
    def getProbability(self, x):
        if x >= 0: return (math.e ** -self.pLambda) * (self.pLambda ** x) / math.factorial(x)
        else: return 0
    #Gets the cumulative probability that the distribution will be less than or equal to a random variable
    def getCumulativeProbability(self, x):
        if x >= 0: 
            prob = 0
            for i in range(x + 1):
                prob += (math.e ** -self.pLambda) * (self.pLambda ** i) / math.factorial(i)
            return prob
        else: return 0

    #------Operators------
    #Overrides the add operator
    def __add__(self, other):
        return PoissonDistribution(self.pLambda + other.pLambda)
    def __iadd__(self, other):
        return self + other
    #Overrides the is equal to operator
    def __eq__(self, other):
        return self.pLambda == other.pLambda
    #Overrides the not equal to operator
    def __ne__(self, other):
        return self.pLambda != other.pLambda

    #Returns a string version of the Vector needed
    def __str__(self):
        return "Poisson Distribution with Lambda:%s"%self.pLambda

if __name__=="__main__":
    pd = PoissonDistribution(5) + PoissonDistribution(2)
    print(pd.getCumulativeProbability(3))