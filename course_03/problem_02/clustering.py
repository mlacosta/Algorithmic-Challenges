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
        self.source = element[0]
        self.endpoint = element[1]
        self.cost = element[2]

class Node:
    def __init__(self,leader,rank):
        self.__leader = leader
        self.__rank = rank
        self.__id = leader
        
    def set_leader(self,leader):
        self.__leader = leader
    
    def increaseRank(self):
        self.__rank += 1
    
    def get_leader(self):
        return self.__leader
    
    def get_rank(self):
        return self.__rank
    
    def get_id(self):
        return self.__id
    
class Union:
    '''
    disjoint-set data structure
    '''
    def __init__(self,size):
        self.nodes = []
        self.__sets = size
        for inx in range(size):
            label =  inx + 1
            self.nodes.append(Node(label,0))
            
    def get_sets(self):
        return self.__sets
    
    def decreaseSets(self):
        self.__sets -= 1
    
    def findSet(self,label):
        leader =  self.nodes[label - 1].get_leader()
        if leader != label:
            self.nodes[label - 1].set_leader(self.findSet(leader))
        return self.nodes[label - 1].get_leader()
    
    def link(self,firstNodeLabel,secondNodeLabel):
        
        firstNode = self.nodes[firstNodeLabel - 1]
        secondNode = self.nodes[secondNodeLabel - 1]
        
        if firstNode.get_rank() > secondNode.get_rank():
            secondNode.set_leader(firstNodeLabel)
        else:
            firstNode.set_leader(secondNodeLabel)
            if firstNode.get_rank() == secondNode.get_rank():
                secondNode.increaseRank()
        #I assume that the first and second variable are aliasings...
        
    def union(self,firstNodeLabel,secondNodeLabel):
        self.link(self.findSet(firstNodeLabel),self.findSet(secondNodeLabel))
        self.decreaseSets()

def createEdgeList(parsedData):
    edges = []
    for edge in parsedData:
        edges.append(Edge(edge))
    
    edges = sorted(edges, key = lambda x: x.cost)
    return edges

def clustering(edges,size,k):
    lazySet = Union(size)
    
    while lazySet.get_sets() > k :
        
        edge = edges.pop(0)
        if not (lazySet.findSet(edge.source) == lazySet.findSet(edge.endpoint)):
            lazySet.union(edge.source,edge.endpoint)
    
    return lazySet
### IMPLEMENTATION ###

def calculateClusters(nodes):
    
    leaders = set()
    
    for node in nodes:
        if node.get_leader() == node.get_id():
            leaders.add(node.get_id())
    
    return leaders

def calculateDistance(source,endpoint,data,numOfNodes):
    index = int((source - 1)*(numOfNodes-source/2) + (endpoint - source) -1)
    return data[index][2]
    
def maxDistance(edges,lazySet):
    size = len(edges)
    for i in range(size):
        firstLeader = lazySet.findSet(edges[i].source)
        secondLeader = lazySet.findSet(edges[i].endpoint)
    
        if (firstLeader != secondLeader):
            return edges[i].cost
    
            
    
(data, info) = readData('question1\input_completeRandom_1_8.txt')

#small test case, uncomment to try it
#data = [
#        [1,2,3],
#        [1,3,12],
#        [1,4,2],
#        [2,3,11],
#        [2,4,7],
#        [3,4,3]
#        ]
#
#info = [4]
k = 4
edges = createEdgeList(data)
lazySet = clustering(edges,info[0],k)
nodes = lazySet.nodes
leaders = calculateClusters(nodes)
nodes = sorted(nodes, key = lambda x: x.get_rank(),reverse= True)
print(maxDistance(edges,lazySet))