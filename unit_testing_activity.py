#function that adds two numbers

#what would the requirements be?
#only take numbers as an input i.e. it would always be a float


def addition(x,y):
    sum = int(x) + int(y)
    print(sum)
    return sum

def run():
    addition(input('enter number 1 to add: '), input('enter number 2 to add: '))