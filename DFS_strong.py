#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: July 2nd 2020

from collections import deque

## Header ###
class Node:
    
    def __init__(self,nodeNumber):
        self.__nodeNumber = nodeNumber;
        self.__edges = [];
        self.__explored = False;
        self.__fTime = 0;
        self.__leader = 0;
    
    def set_nodeNumber(self,number):
        self.__nodeNumber = number;
    
    def add_edge(self,edge):
        self.__edges.append(edge);
    
    def get_edges(self):
        return self.__edges
    
    def get_vertex(self):
        return self.__nodeNumber
    
    def set_fTime(self,value):
        self.__fTime =  value
        
    def get_fTime(self):
        return self.__fTime
    
    def isExplored(self):
        return self.__explored
    
    def set_explored(self):
        self.__explored = True;
    
    def set_leader(self,value):
        self.__leader = value
        
    def get_leader(self):
        return self.__leader

    def __str__(self):
        return "Node: %d, edges: "%self.get_vertex() + str(self.get_edges())
        
#  Uncomment the code below if you want to check the leaders and finishing times (debug)
#
#        
#        return ("Node: %d, edges: "%self.get_vertex() + str(self.get_edges()) 
#                + " (leader: %d)"%self.get_leader() + " (fTime: %d)"%self.get_fTime())

class Stack:
    """ requires deque from collection
    """
    def __init__(self):
        self.__stack = deque()
    
    def push(self,item):
        self.__stack.append(item)
    
    def pull(self):
        return self.__stack.pop()

def createNodes(vertices):
    """
    parameters:
        vertices(list): list of [vertex,edges]
        
    returns:
        a list of Node objects
    """
    nodesObj = []
    index = 1;
    nodeSet = set()
    
    for vertex in vertices:
        
        if len(nodesObj) == 0:
            nodesObj.append(Node(1))
                
        if int(vertex[0]) == index:
            
            nodesObj[index - 1].add_edge(int(vertex[1]))
        
        else:
            k = int(vertex[0]) - index
            for j in range(k-1):
                index+=1
                nodesObj.append(Node(index));
            index+=1
            nodesObj.append(Node(index));
            nodesObj[index - 1].add_edge(int(vertex[1]))
            
        nodeSet.add(int(vertex[1]))
        
    maxNode = max(nodeSet)
    
    if len(nodesObj) < maxNode:
        
        k = maxNode - len(nodesObj)
        for j in range(k):
            index+=1
            nodesObj.append(Node(index));
        
            
    return nodesObj

    
def DFSloop(graph,useOrder = False, ordering = [], useStack = False):
    """
        parameters:
            graph (list): A list of Node objects
            useOrder (bool): If true then searches the graph according
                             to a topological order given by 'ordering'
            ordering (list): Node labels in increasing topological order
        returns:
            Set finished times (fTime) and leaders for each node
    """    
    size = len(graph)
    fTime = 0
    leader = 0
    
    for i in range(size - 1,-1,-1):
        
        if (useOrder):
            inx = ordering[i] - 1
        else:
            inx = i
        
        if not(graph[inx].isExplored()): #if node is not yet explored
            leader = graph[inx].get_vertex() #node number
            fTime = DFS(graph,inx,fTime,leader,size)
    
    
def DFS(graph,inx,fTime,leader,size):
    """
       applies Depth First Search (DFS) given a starting node
        
       parameters:
            graph (list): A list of Node objects
            inx(int): index of the current Node on the graph list
            fTime(int): current finishing time
            leader(int): current leader
            size(int): number of nodes in the graph
        returns:
            fTime(int): updated finishing time
    """ 
    graph[inx].set_explored()
    graph[inx].set_leader(leader)
    
    for arc in graph[inx].get_edges():
        if not(graph[arc-1].isExplored()): #if the node is not yet discovered
            fTime = DFS(graph,arc-1,fTime,leader,size)
    fTime += 1
    
    graph[inx].set_fTime(fTime)
    
    return fTime

def reverseGraph(graph):
    """
         reverses the graph (transpose) in O(n+m) ~linear time
        
        parameters:
            graph (list): A list of Node objects. The input graph
        returns:
            revGraph (list): A list of Node objects. The reversed graph.
    """
    
    revGraph = [0]*len(graph)
    
    for vertex in graph:
        
        nodeNumber = vertex.get_vertex()
        edges = vertex.get_edges()
        

        for arc in edges:
            
            if (revGraph[arc - 1] == 0):
                revGraph[arc - 1] = Node(arc)
            
            revGraph[arc - 1].add_edge(nodeNumber)
    
    inx = 0    
    for vertex in revGraph:
        if vertex == 0:
            revGraph[inx] = Node(inx + 1)
        inx+=1
        
    return revGraph

def copyInfo (toGraph,fromGraph):
    """
        Copy the leaders and fTime from fromGraph into toGraph
        in linear time
    """
    if(len(fromGraph) != len(toGraph)):
        raise Exception('Input size mismatch ')
    
    for vertex in fromGraph:
        toGraph[vertex.get_vertex() - 1].set_leader(vertex.get_leader())
        toGraph[vertex.get_vertex() - 1].set_fTime(vertex.get_fTime())

def topologicList(graph):
    """
        parameters:
            graph (list): A list of Node objects. The input graph
        returns:
            ordering (list): A list of Node labels in increasing order
            according to their finishing times.
    """
    ordering = [0]*len(graph)
    
    for vertex in graph:
        ordering[vertex.get_fTime()-1] = vertex.get_vertex()
    
    return ordering


def retrieveClusters(graph):
    """
        parameters:
            graph (list): A list of Node objects. The input graph.
                          The graph MUST be preprocessed with DFS before 
                          using this function.
        returns:
            clusters (Dictionary): A dict where each item is a list that includes
                                   the labels of a strongly connected component.
                                   The keys are the leaders of each cluster.
    """
    
    clusters = {}

    for vertex in graph:
        
        key = str(vertex.get_leader())
        
        if not(key in clusters):
            clusters[key] = []
        
        sccs = clusters[key]
        sccs.append(vertex.get_vertex())
        clusters[key] = sccs
    
    return clusters
        

## Header end ###         
       
## Testing ###

test = True #change this boolean to disable testing (test = False)
debug = False  #print intermediate steps

if(test): #choose a graph for testing
    
    nodes = [  #testing graph
                ['1','4'],
                ['2','8'],
                ['3','6'],
                ['4','7'],
                ['5','2'],
                ['6','9'],
                ['7','1'],
                ['8','5'],
                ['8','6'],
                ['9','3'],
            ]
    
    nodes = [  #testing graph
                ['1','2'],
                ['1','3'],
                ['3','4'],
                ['4','1'],
                ['4','5'],
            ]
    
    nodes = [  #testing graph
                ['1','2'],
                ['2','3'],
                ['2','4'],
                ['3','1'],
               
            ]
    
    nodes = [ #testing graph
                ['1','2'],
                ['2','5'],
                ['3','6'],
                ['3','3'],
                ['4','2'],
                ['4','7'],
                ['5','4'],
                ['5','1'],
                ['6','8'],
                ['7','5'],
                ['8','9'],
                ['9','6']
            ]
    graph = createNodes(nodes)
    
    print('graph:')
    for node in graph:
        print(node)
       
    revGraph = reverseGraph(graph)
    DFSloop(revGraph)
    
    if(debug):
        print('\nreversed graph:')
        for node in revGraph:
            print(node)
            
    copyInfo(graph,revGraph)
    
    if(debug):
        print('\ncopied graph:')
        for node in graph:
            print(node)
    
    ordering = topologicList(graph)
    
    if(debug):
        print('\nordered list:')
        print(ordering)
    
    DFSloop(graph,True, ordering)
    
    if(debug):
        print('\nclustered graph:')
        for node in graph:
            print(node)
        
    clusters =  retrieveClusters(graph) 
    
    print('\nstrongly connected components:')
    print(clusters)


## Stanford's dataset ###
        
    
#with open('graph.txt') as f:
#    nodes = f.read().splitlines()
#    
##preprosesing nodes
#for i in range(len(nodes)):
#    nodes[i] = nodes[i].split()    
#    
#del i
#    
#graph = createNodes(nodes)
#del nodes

    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    