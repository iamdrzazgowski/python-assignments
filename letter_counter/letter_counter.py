word = str(input("Enter a word: "))
char = str(input("Enter a char: "))
word = word.lower()

def create_dict(word):
    dict = {}
    for i in word:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    return dict

def remove_useless_keys(dict):
    uselessKeys = [",","."," ",":"]

    for j in uselessKeys:
        if j in dict:
            del dict[j]
    return dict

def single_letter_counter(dict, char):
    return dict[char]

# dict = create_dict(word)
print(remove_useless_keys(create_dict(word)))
print(single_letter_counter(create_dict(word), char))
