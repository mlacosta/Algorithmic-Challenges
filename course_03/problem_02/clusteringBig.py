#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Aug 26th 2020
#
#Hamming distance clustering
#Calculate number of clusters such that max dist >= 3

### HEADER ###
import clustering as ctr

def bin2dec(num):
    size = len(num) - 1
    dec = 0        
    for bit in num:
        dec += (2 ** size) * bit
        size -= 1
    return dec

def xor(a,b):
    return (a & ~b) | (~a & b)

def decList(data,size):
    numbers =  []
    for word in data:
        numbers.append(bin2dec(word))
    
    return numbers

def createHashMap(data):
    size = len(data)
    hashMap = {}
    for inx in range(size):
        key = data[inx]
        if key in hashMap:
            hashMap[key].append(inx + 1)
        else:
            hashMap[key] = [inx + 1]
    
    return hashMap

def create_hamming_mask(size):
    #1-bit mask
    dist1 = [1 << i for i in range(size)]
    #2-bits mask
    dist2 = set()
    
    for value1 in dist1:
        for value2 in dist1:
            if value1 != value2:
                dist2.add(value1 | value2)
    
    dist2 = sorted(list(dist2))
    
    return [0] + dist1 + dist2

def clustering(data,masks,numOfNodes):
    
    lazySet = ctr.Union(numOfNodes)
    for mask in masks:    
        for key in data.keys():
            search = xor(key,mask)
#            print(search)
            if search in data:
                sources = data[key]   
                endpoints = data[search]     
                for source in sources:
                    for endpoint in endpoints:
                        if (lazySet.findSet(source) != lazySet.findSet(endpoint)):
#                            print('union!')
                            lazySet.union(source,endpoint)

    return lazySet
# IMPLEMENTATION 
    
(data, info) = ctr.readData('clustering_big.txt')
data = decList(data,info[1])
table  = createHashMap(data)
masks =  create_hamming_mask(info[1])
lazySet = clustering(table,masks,info[0])
nodes = lazySet.nodes
leaders = ctr.calculateClusters(nodes)
print(len(leaders))