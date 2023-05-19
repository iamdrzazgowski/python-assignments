
x = 123
def isPalindrom(x):
    if x < 0 or (x > 0 and x % 10 == 0):
        return False
    elif x == 0 or (x > 0 and x < 10):
        return True
    else:
        
        result = 0
        num_lenght = len(str(x)) - 1
        n = 0
        temp = x
        
        while x > 0:
            result += x % 10 * pow(10,num_lenght - n)
            x = x // 10
            n += 1
        
        if result == temp:
            return True
        else:
            return False


print(isPalindrom(1221))