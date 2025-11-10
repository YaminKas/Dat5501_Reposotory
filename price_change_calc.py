#this calculator will calculate the change in a stocks price

arrray = [0,1,2,3,4,5,6,7,8,9,]

def calc(array):
    len_array = len(array)
    for x in range (0 , (len_array-1) ):
        return array[x] + array[x+1]