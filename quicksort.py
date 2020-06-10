file = open("quicksort.txt","r")
intList = []

for x in file:
    intList.append(int(float(x)))
    
a=[12,5,7,9,91,2,45,4,6,9,11,32,77] 

def quicksort(array,option = 1):
    
    n = len(array)
    
    if n == 1:
        return array
    
    choosePivot = [0,-1]
    i = choosePivot[option - 1]
    pivot = array[i]

    #partition step
    
    if (option == 1) :
        i = 1
        j = 1
    
        while j<n:
    
            if (array[j] >= pivot):
                j = j + 1
            else:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
                j = j + 1
                i = i + 1
                
        temp = array[i-1]
        array[i-1] = pivot
        array[0] = temp
    
    print("i: %d, j: %d"%(i,j))
            
    return array

    #recursive call 1
    
    #recursive call 2
    

    

    
    
    