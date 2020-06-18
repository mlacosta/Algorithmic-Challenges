#Author: Mariano L. Acosta
#17 June 2020

with open('kargerMinCut.txt') as f:
    nodes = f.read().splitlines()
    
#Preprocessing 
    
nodesArray = []

for node in nodes: #removes tabspace
    nodesArray.append(node.split('\t'))
    
for node in nodesArray: #removes empty element
    node.pop(-1)
    
#convert to integer


nodes = []    

for node in nodesArray:
    nodes.append(list(map(int,node)))

del node, nodesArray


#mincut Implementation
from random import seed, randint

class Node: #I define a Node class to make my life easier
    
    def __init__(self):
    
        self.__vertex = []
        self.__edges = []
    
    def set_vertex(self,vertex):
        
        """
        parameters:
            vertex (int): new node you want to add to your list of vertices (called vertex)
        
        """
        self.__vertex.append(vertex)
    
    def set_edges(self,edges):
    
        """
        parameters:
            edges (list): a list of adjacent vertices you want to add to your list of edges
        
        """
        self.__edges = self.__edges + edges
    
    def get_vertex(self):
        """ For testing purposes
        """
        return self.__vertex
    
    def get_edges(self):
        """ For testing purposes
        """
        return self.__edges
    
    
    def reduce(self):
        """ Removes self loops 
        """
        for val in self.__vertex:
            if val in self.__edges:
                while val in self.__edges:
                    self.__edges.remove(val)
    
    def merge(self, newNode):
        """ Combine step required in the Contraction Algorithm
        """
        self.__vertex += newNode.get_vertex()
        self.__edges += newNode.get_edges()
        self.reduce()
        

#seed(37) #for testing purposes
        
def findNode (graph,index):
    """ Find a node in a graph given their indices. This is not a trivial
        operation because of the combine step
    """

    nodesNumber = []
    
    for val in graph:
        nodesNumber.append(val.get_vertex())
    
    counter = 0
    
    for i in nodesNumber:
        if index in i:
            break
        else:
            counter+=1
    
    return counter
            

def randomContraction(listOfNodes):
    
    graph = [] # a list of nodes objects
    
    for val in listOfNodes: #I convert the list of nodes into a Graph (list of nodes objects)
        temp = Node()
        temp.set_vertex(val[0])
        temp.set_edges(val[1:])
        graph.append(temp)
    
    while (len(graph)>2):
        N = len(graph)
        randInx =  randint(0, N-1)
        
        randomNode =  graph[randInx]
        randomVertex = randomNode.get_edges()[randint(0,len(randomNode.get_edges())-1)]
        index = findNode(graph,randomVertex)
#        print('N:%d, rndinx:%d, adjinx:%d'%(N,randInx,index)) #debuging
        adjNode = graph[index]
        randomNode.merge(adjNode)
        graph[randInx] = randomNode
        graph.pop(index)
            
        
    return graph
    
    
#nodes =  [[1,3],[2,3,5],[3,1,2,4,5],[4,3,5],[5,2,3,4]]   #small test

mincut = 1e9
counter = 0

for i in range(1000): #I propose an adaptive search
    graph = randomContraction(nodes)
    cut =  len(graph[0].get_edges())
    
    if (cut < mincut):
        counter = 0
        mincut = cut
        print('new mincut found = %d'%mincut)
    else:
        counter+=1
        if counter == 30: #if after 30 consecutive search the mincut doesn't change then break
            break
        
print('finished!')


    



