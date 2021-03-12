#An instance that will search a word for all the consonants
class ConsonantIdentifier:
    #------Initialiser------
    #Takes a string and takes out the consonants
    def __init__(self, text):
        self.text = text
        self.createDictionary()
        self.seperateConsonants()
        self.displayResult()

    #------Methods/Functions------
    #Identifies all of the possible consonants
    def createDictionary(self):
        self.consonants = {}
        #Iterates through every lower case letter and creates an entry into the consonants dictionary for it
        for letter in range(26):
            if letter + 97 in [ord('a'), ord('e'), ord('i'), ord('o'), ord('u')]: continue
            self.consonants[letter + 97] = 0
    #Seperates the consonants
    def seperateConsonants(self):
        #Seperates the consonants from the text
        self.seperatedText = ""
        for character in self.text:
            #Checks if the character is a consonant, if it is it adds it to seperatedText
            try:
                self.consonants[ord(character.lower())] += 1
                self.seperatedText = self.seperatedText + character
            except: continue
    #Displays the results
    def displayResult(self):
        print("Original: " + self.text)
        print("Consonants: " + self.seperatedText)
        for key in self.consonants:
            if key == 98:
                print(chr(key) + ": " + str(self.consonants[key]), end=''); continue
            print(", " + chr(key) + ": " + str(self.consonants[key]), end='')
        print()

if __name__=="__main__":
    ConsonantIdentifier("This is a test message that will get seperated in consonants")
