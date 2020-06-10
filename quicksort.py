file = open("quicksort.txt","r")
intList = []

for x in file:
    intList.append(int(float(x)))
    
    

def quicksort(array,option = 1):
    
    choosePivot = [0,-1]
    
    n = len(array)
    
    if n == 1:
        return array
    
    pivot = choosePivot[option]
    
    left = []
    right = []
    
    #partition step
    
    left = quicksort(left,1)
    right = quicksort(right,1)