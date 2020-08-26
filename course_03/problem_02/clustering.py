#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Aug 26th 2020
#
#Implement max-spacing k-clustering using disjoint-sets

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
        self.__leader = leader
        self.__rank = rank
        
    def set_leader(self,leader):
        self.__leader = leader
    
    def increaseRank(self):
        self.__rank += 1
    
    def get_leader(self):
        return self.__leader
    
    def get_rank(self):
        return self.__rank
    
class Union:
    '''
    disjoint-set datastructure
    '''
    def __init__(self,size):
        self.nodes = []
        for inx in range(size):
            self.nodes = Node(inx + 1,0)

    def findSet(self,label):
        leader =  self.nodes[label - 1].get_leader()
        if leader != label:
            self.nodes[label - 1].set_leader(self.findSet(leader))
        return self.nodes[label - 1].get_leader()
    
    def link(self,firstNodeLabel,secondNodeLabel):
        
        firstNode = self.nodes(firstNodeLabel - 1)
        secondNode = self.nodes(secondNodeLabel - 1)
        
        if firstNode.get_rank() > secondNode.get_rank():
            secondNode.set_leader() = firstNodeLabel
        else:
            firstNode.set_leader() = secondNodeLabel
            if firstNode.get_rank() == secondNode.get_rank():
                secondNode.increaseRank()
    
    def Union(self,firstNodeLabel,secondNodeLabel):
        
        #I assume that the first and second variable are aliasing...
                
        

def createEdgeList(parsedData):
    edges = []
    for edge in parsedData:
        edges.append(Edge(edge))
    
    edges = sorted(edges, key = lambda x: x.cost)
    return edges

def clustering(edges,size,k):
        
### IMPLEMENTATION ###
            
(data, info) = readData('clustering1.txt')
edges = createEdgeList(data)