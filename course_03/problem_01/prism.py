#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Aug 9th 2020
#
#Implement Prim's minimum spanning tree algorithm.
#

### HEADER ###
import heapq as hp
     
def readData(filename):
    '''
        parameters:
            filename (string): Name of the txt file you want to read (without the file extension)
        returns:
            parsedData (list): parsed data.
    '''
    parsedData = []
    
    with open(filename + '.txt') as f:
        data = f.read().splitlines()
        
    info = list(map(int,data[0].split()))
    data = data[1:]
    
    for val in data:
        parsedData.append(list(map(int,val.split())))
    
    return parsedData, info

def prism(edges,numOfNodes,numOfEdges):
    
    explored = hp.heapify([])

    
    edges = sorted(edges, key = lambda a: a[0])
    
    
    return graphSize


### IMPLEMENTATION ###
    
(parsedData, info) = readData('edges')
prism(parsedData,info[0],info[1])