#Defines an instance of hangman
class Hangman:
    #------Initialiser------
    def __init__(self, maxTries=11):
        self.maxTries = maxTries
        #Stores every incorrect guess
        self.incorrectGuesses = []
        #Generates a target word
        self.targetWord()
        self.run()
    #------Methods/Functions------
    #Runs the hangman game
    def run(self):
        #Runs while the game isn't in a game over state
        while len(self.incorrectGuesses) != self.maxTries and self.targetWord.isnumeric() == False:
            #Displays state info to the user
            print()
            print(self.wordProgress)
            print("Guesses: ", end='')
            #Prints all of the incorrect guesses to the user
            for guess in range(len(self.incorrectGuesses)):
                print(self.incorrectGuesses[guess], end='')
                if guess != len(self.incorrectGuesses) - 1: print(", ", end='')
            print()
            self.makeGuess()
        #------Game Ended Messages------
        print()
        print("You Achieved: " + self.wordProgress)
        print("The correct word is: " + self.correctWord)
        print("Your incorrect guesses were: ", end='')
        #Prints all of the incorrect guesses to the user
        for guess in range(len(self.incorrectGuesses)):
            print(self.incorrectGuesses[guess], end='')
            if guess != len(self.incorrectGuesses) - 1: print(", ", end='')
        print()
        #Prints the success Messages
        if len(self.incorrectGuesses) == self.maxTries: print("Good luck next time")
        elif self.targetWord.isnumeric(): print("Well done")

    #Asks for a target word from the user
    def targetWord(self):
        #Gets a target word and ensures that it is all letters
        while True:
            self.targetWord = input("Target Word: ").lower()
            #Validates the target word
            valid = True
            for i in range(len(self.targetWord)):
                if len(self.targetWord[i]) == 0 or self.targetWord[i].isnumeric(): valid = False
            if valid == True: break
        #Backs up the target word
        self.correctWord = self.targetWord
        #Stores the words progress with default values
        self.wordProgress = ""
        for i in range(len(self.targetWord)):
            if self.targetWord[i] == " ":
                self.wordProgress = self.wordProgress + " "
                #Replaces all spaces with a one
                if i == 0: self.targetWord = "1" + self.targetWord[i+1:]
                else: self.targetWord = self.targetWord[:i] + "1" + self.targetWord[i+1:]
                continue
            self.wordProgress = self.wordProgress + "_"
    #Asks for a guess by the user and keeps track of all guesses
    def makeGuess(self):
        #Recieves a guess from the user that is one letter long
        guess = input("What is your guess: ").lower()
        while len(guess) != 1 or guess.isnumeric() or guess == " ": guess = input("Guess has to be one letter: ").lower()
        #Adds the guess to incorrectGuesses if it is incorrect
        if self.checkGuess(guess) == False: self.incorrectGuesses.append(guess)
    #Checks if the guess is in the word
    #Returns a bollean to determine whether the guess was correct
    def checkGuess(self, guess):
        #A bollean to determine whether the guess was correct
        guessCorrect = False
        #Overwrites wordprogress with the progress if the guess is in the target word
        for i in range(len(self.targetWord)):
            if self.targetWord[i] == guess:
                #Places the correct guess in the correct index of word progress
                #Also removes the letter from the target word, replacing it with a character the user can't choose
                if i == 0:
                    self.wordProgress = guess + self.wordProgress[i+1:]
                    self.targetWord = "1" + self.targetWord[i+1:]
                else:
                    self.wordProgress = self.wordProgress[:i] + guess + self.wordProgress[i+1:]
                    self.targetWord = self.targetWord[:i] + "1" + self.targetWord[i+1:]
                guessCorrect = True
        return guessCorrect

if __name__=="__main__":
    Hangman(11)
