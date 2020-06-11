#Author: Mariano Leonel Acosta

import random
from statistics import median

file = open("quicksort.txt", "r")
intList = []

for x in file:
    intList.append(int(float(x)))

a = []

for i in range(9):
    a.append(random.randint(0, 100) - 50) #for testing purposes

counter = 0

def quicksort(array, option=1):
# USAGE: option: choose 1,2 or 3 to implement each quiz respectively
#
#
    global counter

    n = len(array)

    if (n == 1) or (n == 0):
        return array
    
    # partition step
    if option == 1:
        pivot = array[0]

    if (option == 2):
        pivot = array[-1]
        temp = array[0]
        array[0] = pivot
        array[-1] = temp
    
    if (option == 3):
        first = array[0]
        last = array[-1]
        
        if (n%2 == 1):
            inx = n//2    
        else:
            inx = (n-1)//2
        
        candidates = [first,array[inx],last]
        pivot = median(candidates)
        inx2 = candidates.index(pivot)
        
        if inx2 == 0:
            inx = 0
        elif inx2 == 2:
            inx = -1

        array[inx] = array[0]
        array[0] = pivot
        
    counter = counter + n - 1
    i = 1
    j = 1

    while j < n:

        if (array[j] >= pivot):
            j = j + 1
        else:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            j = j + 1
            i = i + 1

    temp = array[i - 1]
    array[i - 1] = pivot
    array[0] = temp

    # recursive call 1
    array[:(i - 1)] = quicksort(array[:(i - 1)],option)

    # recursive call 2
    array[i:] = quicksort(array[i:],option)

    return array

quicksort(intList,option = 3)

print(counter)
