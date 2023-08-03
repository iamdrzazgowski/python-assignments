from letter_counter_class import *

word = str(input("Enter a word: "))
char = str(input("Enter a char: "))
letterCounter = LetterCounter(word, char)
letterCounter.CreateDict()
letterCounter.RemoveUselessKeys()
print(letterCounter.ShowDict())
print(letterCounter.SingleLetterCounter())