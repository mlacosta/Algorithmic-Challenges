#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: July 19th 2020
#
#Implement a "2-SUM" finder using a Hash Table (and binary search)
#

### HEADER ###
import heapq as hp
import bisect as bi

def readData(filename):
    '''
        parameters:
            filename (string): Name of the txt file you want to read 
        returns:
            parsedData (list): parsed data.
    '''
    parsedData = []
    
    with open(filename) as f:
        data = f.read().splitlines()
        
    for val in data:
        parsedData.append(int(val))
    
    return parsedData

class HashTable: #unused but functional
    
    def __init__(self,buckets):
        self.__buckets = buckets
        self.__hashTable = []
        
        for inx in range(self.__buckets):
            self.__hashTable.append([])
            
    def hashFunction(self,value):
        """
            implements the division method for hashing
        """
        
        return hash(value) % self.__buckets
    
    def add(self,value):
        
        key = self.hashFunction(value)
        self.__hashTable[key-1].append(value) 
    
    def convertData(self,data):
        """
            parameters:
                data(list): list of single values
        """
        for val in data:
            self.add(val)
    
    def find(self,value):
        
        key = self.hashFunction(value)
        chain = self.__hashTable[key-1]
        
        return value in chain
    
    def get_chain(self,key):
       
       return self.__hashTable[key-1]
   

def computeTargetValues(data,lowerBound,upperBound):
    """
        Given a list of integers, it computes if it exists
        two distinct values x and y in the list such that 
        x + y lies between a given input interval. It doesn't compute duplicates,
        for instance, if both 3 + 2 = 5 and 4 + 1 = 5 are between the input 
        interval, then it's counted as a single case.
        
        parameters:
            data (list): list of integers
            lowerBound (int): lowest value in the input interval
            upperBound (int): highest value in the input interval
        
        returns:
            (int): the number distinct sum values (x + y) between the input 
            interval
        
    """
    
    data = sorted(set(data)) #sort data in O(nlog(n)). Also it removes duplicates
    
    minVal = min(data)
    maxVal = max(data)

    targetSet = set() #here I'll store unique values (x + y) between lowerBound
                      #and upperBound such that x != y and both of them are in 'data'.
    
    for val in data:
        minRange = lowerBound - val #obtain the range of possible values
        maxRange = upperBound - val
        
        if (maxRange < minVal) or (minRange > maxVal):
            continue
        
        if (minRange < minVal):
            minRange = minVal

        if (maxRange > maxVal):
            maxRange = maxVal 

        i = bi.bisect_left(data,minRange)  #find index of closest match in O(log(n))
        j = bi.bisect_left(data,maxRange)  #find index of closest match in O(log(n))
        
        if (j - i) != 0: #if there exist values that sum a target value
            candidates = data[i:j]
            candidates = [x + val for x in candidates]
            targetSet.update(candidates)
            
    return len(targetSet) #cardinality of unique target values

###Implementation ###

data = readData('2sum.txt')
print('\nsome statistics:\n')
print('* max value in data: %d'%(max(data)))
print('* min value in data: %d'%(min(data)))
print('* size of data: %d\n'%(len(data)))

counter = computeTargetValues(data,-10000,10000)

print("Target values in interval: %d"%counter)




