#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: July 19th 2020
#
#Implement a "2-SUM" finder using a Hash Table 
#

### HEADER ###
import heapq as hp

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



class HashTable:
    
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
   

def twoSum(data,targetSum,hashTable):
        
    for val in data:
        search = targetSum - val 
    
        if search == val: #search only for distinc data
            continue
        if (hashTable.find(search)):
            return True
    
    return False

def computeTargetValues(data,lowerBound,upperBound):
    
    hashTable = HashTable(250007)
    hashTable.convertData(data)
    
    targetInterval = list(range(lowerBound,upperBound + 1))
    
    length = len(targetInterval)
    
    counter = 0;
    iteration = 1
    
    table = set(data)
    
    targets = set()
    
    #calculate all the targets
    
    for val in table:
        for target in targetInterval:
            targets.add(target - val)
    
    
        
    return targets
            
    

###Implementation ###

data = readData('2sum.txt')
print('\nsome statistics:\n')
print('* max value in data: %d'%(max(data)))
print('* min value in data: %d'%(min(data)))
print('* size of data: %d\n'%(len(data)))

counter = computeTargetValues(data,-10000,10000)
#print("Target values in interval: %d"%counter)




