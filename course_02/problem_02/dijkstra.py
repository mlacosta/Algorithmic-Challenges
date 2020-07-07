#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: July 7th 2020
#
#Implement Dijkstra's Shortest Path Algorithm with a Heap Data structure
#

import heapq as hp
import copy

class Edge:
    def __init__(self,startNode,destNode,cost):
        self.__startNode = startNode
        self.__destNode = destNode
        self.__cost = cost
    
    def get_cost(self):
        return self.__cost
    
    def get_destNode(self):
        return self.__destNode
    
    def get_startNode(self):
        return self.__startNode
    
    def __lt__(self,other): #comparison function to use in the heap structure
        return self.get_cost() < other.get_cost()

class Node:
    
    def __init__(self,nodeNumber,edges):
        self.__nodeNumber = nodeNumber;
        self.__edges = edges;

    def set_nodeNumber(self,number):
        self.__nodeNumber = number;
    
    def add_edge(self,edge):
        self.__edges.append(edge);
    
    def get_edges(self):
        return self.__edges
    
    def get_vertex(self):
        return self.__nodeNumber
    
    def __str__(self):
        pass

class Graph:
    
    def __init__(self,nodes):
        self.__nodes = nodes
        self.Xset = set([1]) #explored set of the graph
#        self.frontier = [10e9]*self.get_size()
        self.frontier = copy.copy(nodes[0].get_edges())
        hp.heapify(self.frontier) #I create a heap structure to store the frontier
    
    def get_node(self,label):
        return self.__nodes[label-1]
    
    def pop_min_edge(self):
        return hp.heappop(self.frontier)
    
    def add_to_frontier(self,edges):
        
        if not(isinstance(edges, list)):
            raise Exception("input edges are not in a list");
        
        for edge in edges:
            if not(edge.get_destNode() in self.Xset):
                hp.heappush(self.frontier,edge)

    
    def get_size(self):
        return len(self.__nodes)
    
    def isExplored(self):
        return self.get_size() == len(self.Xset)
    
    def add_to_set(self,label):
        if(label in self.Xset):
            raise Exception('something went wrong')
        self.Xset.add(label)

    def remove_from_frontier(self,label):
        
        for edge in self.frontier:
            if edge.get_destNode() == label:
                self.frontier.remove(edge)
        
        
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
            edges (list): a list of Edge objects
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
                edges.append(Edge(nodeNumber,int(buffer[0]),int(buffer[1])))
        
        nodes.append(Node(nodeNumber,edges))
    
    return Graph(nodes)

def shortestPath(graph):
    """
        computes the shortest distance from the source node to each vertex.
        
        parameters:
            graph (Graph Object): the input graph you want to calculate its shortest paths
        
        returns:
            paths (list): Each element of the list is the shortest distance from node 1 to the node (index + 1)
        
    """

    paths = [0]*graph.get_size()
    startNode = 1
    
    while not(graph.isExplored()):
        minEdge = graph.pop_min_edge()
        
        destNode = minEdge.get_destNode()
        startNode = minEdge.get_startNode()
        
        if not(destNode in graph.Xset):
        
            graph.add_to_set(destNode)
            graph.remove_from_frontier(destNode)
            dist = minEdge.get_cost()
            newNode =  graph.get_node(destNode)
            
            paths[destNode-1] = paths[startNode - 1] + dist
            graph.add_to_frontier(newNode.get_edges())
        
    return paths
        
        
def getShortestPath(labels,paths):
    
    distances = []
    
    for label in labels:
        distances.append(paths[label-1])
    
    string = ''
    
    for path in distances:
        string += str(path) + ','
    
    print(string[:-1])


parsedData = readData('dijkstraData')
#parsedData = [['1','2,1','4,5','3,2'],
#              ['2','5,4','6,11',],
#              ['3','5,9','6,5','7,16'],
#              ['4','7,2'],
#              ['5','8,18'],
#              ['6','8,13'],
#              ['7','8,2'],
#              ['8','1,100000'],
#                ]
graph = data2Graph(parsedData)
paths =  shortestPath(graph)
getShortestPath([7,37,59,82,99,115,133,165,188,197],paths)


