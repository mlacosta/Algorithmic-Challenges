# Your task is to compute the number of inversions in the file given, where the 
# i^{th}ith row of the file indicates the i^{th}ithentry of an array.
# Because of the large size of this array, you should implement the fast 
# divide-and-conquer algorithm covered in the video lectures.
# The numeric answer for the given input file should be typed in the space below.
# So if your answer is 1198233847, then just type 1198233847 in the space 
# provided without any space / commas / any other punctuation marks. 
# You can make up to 5 attempts, and we'll use the best one for grading.

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