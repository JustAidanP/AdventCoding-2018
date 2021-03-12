#An instance that will search a word for all the vowels
class VowelIdentifier:
    #------Initialiser------
    #Takes a string and takes out the vowels
    def __init__(self, text):
        self.text = text
        self.vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        self.seperateVowels()
        self.displayResult()

    #------Methods/Functions------
    #Seperates the vowels
    def seperateVowels(self):
        #Seperates the vowels from the text
        self.seperatedText = ""
        for character in self.text:
            #Checks if the character is a vowel, if it is it adds it to seperatedText
            try:
                self.vowels[character.lower()] += 1
                self.seperatedText = self.seperatedText + character
            except: continue
    #Displays the results
    def displayResult(self):
        print("Original: " + self.text)
        print("Vowels: " + self.seperatedText)
        for key in self.vowels:
            print(key + ": " + str(self.vowels[key]))

if __name__=="__main__":
    VowelIdentifier("This is a test message that will get seperated into vowels")
