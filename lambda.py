# Intro to lambda function

# lambda function can take any number of arguments with one expression
x = lambda a, b : a * b
print(x(3, 7)) 

# function that always doubles the number
def lambFunc(n):
    return lambda a : a * n

doublerFunc = lambFunc(2)
print(doublerFunc(7))