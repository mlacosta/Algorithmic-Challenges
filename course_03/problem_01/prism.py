#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Aug 9th 2020
#
#Implement Prim's minimum spanning tree algorithm.
#

### HEADER ###
import heapq as hp

class Edge:
    def __init__(self,endpoint,cost):
        self.endpoint = endpoint
        self.cost = cost
        
class Node:
    
    def __init__(self,idNum,edges):
        
        self.edges = []
        for edge in edges:
            self.edges.append(Edge(edge[0],edge[1]))    
        self.id = idNum
        self.key = 1e9
        
    def __lt__(self,other): #comparison function to use in the heap structure
        return self.key < other.key
    
    def __eq__(self, other):
        return self.key == other.key
    
     
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
    
    edges = sorted(edges, key = lambda a: a[0])
    X = set()
    frontier = []
    graph = []
    
    for inx in range(numOfNodes):
        graph.append(Node(inx + 1,[a[1:] for a in parsedData if a[0] == (inx+1)]))
    
    X.add(1)
    nextEdges = graph[0].edges.copy()
    
    for edge in nextEdges:
        if graph[edge.endpoint - 1].key > edge.cost:
            graph[edge.endpoint - 1].key = edge.cost
        
    

    
              
    return frontier


### IMPLEMENTATION ###
    
(parsedData, info) = readData('edges')
graph = prism(parsedData,info[0],info[1])