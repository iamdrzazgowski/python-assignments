class LetterCounter:
    def __init__(self, word, char):
        self.dict = None
        self.word = word
        self.char = char

    def CreateDict(self):
        dict = {}
        for i in self.word:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        self.dict = dict

    def ShowDict(self):
        return self.dict

    def SingleLetterCounter(self):
        try:
            return self.dict[self.char]
        except:
            return "Char is not avaible"

    def RemoveUselessKeys(self):
        uselessKeys = [",", ".", " ", ":"]

        for j in uselessKeys:
            if j in self.dict:
                del self.dict[j]