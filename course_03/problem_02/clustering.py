#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Aug 26th 2020
#
#Implement max-spacing k-clustering using union-find

### HEADER ###
def readData(filename):
    '''
    '''
    parsedData = []
    
    with open(filename) as f:
        data = f.read().splitlines()
        
    info = list(map(int,data[0].split()))
    data = data[1:]
    
    for val in data:
        parsedData.append(list(map(int,val.split())))
    
    return parsedData, info


class Edge:
    def __init__(self,element):
        self.__source = element[0]
        self.__endpoint = element[1]
        self.cost = element[2]


class Node:
    def __init__(self,leader,rank):
        self._leader = leader
        self._rank = rank
        
    def set_leader(self,leader):
        self._leader = leader
    
    def increaseRank(self,leader):
        self._rank += 1
    
    def get_leader(self):
        return self._leader
    
    def get_rank(self):
        return self._rank
    
class Union:
    def __init__(self,size):
        for inx in range(size):
            pass

def createEdgeList(parsedData):
    edges = []
    for edge in parsedData:
        edges.append(Edge(edge))
    
    edges = sorted(edges, key = lambda x: x.cost)
    return edges

def clustering(edges,size,k):
        pass
### IMPLEMENTATION ###
            
(data, info) = readData('clustering1.txt')
edges = createEdgeList(data)