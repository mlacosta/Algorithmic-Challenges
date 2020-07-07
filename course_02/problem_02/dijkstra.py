#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: July 7th 2020
#
#Implement Dijkstra's Shortest Path Algorithm with a Heap Data structure
#

## HEADER ###
import heapq as hp

class Edge:
    def __init__(self,destNode,cost):
        self.__destNode = destNode
        self.__cost = cost
    
    def get_cost(self):
        return self.__cost
    
    def get_destNode(self):
        return self.__destNode

class Node:
    def __init__(self,nodeNumber,edges):
        self.__nodeNumber = nodeNumber
        self.__edges = edges
        
        if (nodeNumber == 1):
            self.__key = 0
        else:
            self.__key = 10e9

    def set_nodeNumber(self,number):
        self.__nodeNumber = number
    
    def add_edge(self,edge):
        self.__edges.append(edge)
    
    def get_edges(self):
        return self.__edges
    
    def get_vertex(self):
        return self.__nodeNumber
    
    def get_key(self):
        return self.__key
    
    def set_key(self,value):
        self.__key =  value
    
    def __lt__(self,other): #comparison function to use in the heap structure
        return self.get_key() < other.get_key()
    
    def __eq__(self, other):
        return self.get_vertex() == other.get_vertex()
    
    def __str__(self):
        pass

class Graph:
    def __init__(self,nodes):
        self.__nodes = nodes
        self.__heap =  nodes[1:]
        hp.heapify(self.__heap)
    
    def get_size(self):
        return len(self.__nodes)
    
    def get_nodes(self):
        return self.__nodes
    
    def get_node_edges(self,label):
        return self.__nodes[label-1].get_edges()
    
    def isExplored(self):
        return len(self.__heap) == 0
    
    def node_in_heap(self,label):
        return Node(label,[]) in self.__heap
    
    def update_key(self,label,greedyScore):

        if (greedyScore < self.get_node_key(label)):
            index =  self.__heap.index(Node(label,[]))
            node = self.__heap.pop(index)            
            node.set_key(greedyScore)
            hp.heapify(self.__heap)
            hp.heappush(self.__heap,node)
    
    def get_node_key(self,label):
        return self.__nodes[label - 1].get_key()
    
    def pop_min(self):
        return hp.heappop(self.__heap)
        
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
    
    for val in data:
        parsedData.append(val.split('\t'))
        
    for val in parsedData: #removes line break
        val.pop(-1)
        
    return parsedData


def data2Graph(parsedData):
    '''
        parameters:
            parsedData (list): parsed data generated with funcion readData()
        returns:
            graph (Graph object): a graph containing the nodes
    '''
    
    nodes = []
    
    for data in parsedData:
        length =  len(data)
        edges = []
        
        for i in range(length):
            if i == 0:
                nodeNumber = int(data[i])
            else:
                buffer = data[i].split(',')
                edges.append(Edge(int(buffer[0]),int(buffer[1])))
        
        nodes.append(Node(nodeNumber,edges))
    
    return Graph(nodes)


def shortestPath(graph):
    """
        computes the shortest distance from the source node to each vertex.
        
        parameters:
            graph (Graph Object): the input graph you want to calculate its shortest paths
        
        returns:
            for each node in graph, it sets the key attribute equal to the shortest distance from node 1
        
    """
    
    nodeNumber = 1 #start from the source vertex
    
    while not(graph.isExplored()):
        
        for edge in graph.get_node_edges(nodeNumber):
            
            endpoint = edge.get_destNode()
           
            if graph.node_in_heap(endpoint):
        
                greedyScore = graph.get_node_key(nodeNumber) + edge.get_cost()
                graph.update_key(endpoint,greedyScore)
        
        nodeNumber = graph.pop_min().get_vertex()

                
def getShortestPath(labels,graph):
    """
        Given a list of labels, it prints the shortest distance for each vertex.
        
        parameters:
            label (list): a list of labels
        
        returns:
            prints the shortest distance for each vertex, separated by a comma.
        
    """
    
    distances = []

    for label in labels:
        distances.append(graph.get_node_key(label))
    
    string = ''
    
    for path in distances:
        string += str(path) + ','
    
    print(string[:-1])

## Implementation ###

parsedData = readData('dijkstraData')
graph = data2Graph(parsedData)
shortestPath(graph)
getShortestPath([7,37,59,82,99,115,133,165,188,197],graph)


