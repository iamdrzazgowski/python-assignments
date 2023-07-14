from letter_counter_class import *

word = str(input("Enter a word: "))
char = str(input("Enter a char: "))
l = LetterCounter(word, char)
l.CreateDict()
l.RemoveUselessKeys()
print(l.ShowDict())
print(l.SingleLetterCounter())