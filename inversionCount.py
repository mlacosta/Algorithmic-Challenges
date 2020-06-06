file = open("IntegerArray.txt","r")
intList = []

for x in file:
    intList.append(int(float(x)))
    

def countSplit(listInput):
    length = len(listInput);
    counter = 0;
      
    B = listInput[:length//2]
    C = listInput[length//2:]
    

    B.sort()
    C.sort()
    

    lenB = len(B)
    lenC = len(C)
      
    i = 0
    j = 0
    
      
    while i < lenB and j < lenC:
        if B[i] <= C[j]:
            i+=1
        
        else:
            counter+= lenB - i
            j+=1
    
    return counter
      
  

def numOfinversions (integerList):
    
    length = len(integerList);
    
    if length == 1:
        return 0
    else:
        x = numOfinversions(integerList[:length//2])
        y = numOfinversions(integerList[length//2:])
        z = countSplit(integerList)
        return x + y + z
    


count = numOfinversions(intList)

print('Number of inversion in IntegerArray.txt: %d'%count)