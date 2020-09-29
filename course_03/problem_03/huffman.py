#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Sep  28th 2020
#
#Huffman encoding with greedy algorithm

#I use a heap for min search and Depth First Search for encoding

### HEADER ###
import heapq as hp

def read_data(file):
    parsed_data = []
    with open(file) as data:
        parsed_data = list(map(int, data.read().splitlines()))
    
    info = parsed_data.pop(0)
    return (info , parsed_data)

class Symbol:
    def __init__(self,index,weight):
        self.symbol = str(index)
        self.weight  = weight

    def __lt__(self,other):
        return self.weight < other.weight
    
    def __str__(self):
        return self.symbol
class Node:
    def __init__(self, symbol = None, label = None,left = None ,right = None, depth = 0, weight = None):
        self.label = label
        self.left = left
        self.right = right
        self.symbol = symbol
        self.__explored = False
        self.depth = depth
        self.weight = weight
    
    def is_explored(self):
        return self.__explored
    
    def set_explored(self):
        self.__explored = True
        
    def __str__(self):
        return 'Label: %s, Symbol: %s, Depth: %d, Weight: %d'%(self.label,self.symbol,self.depth,self.weight)

    def __lt__(self,other):
        return self.weight < other.weight
    
    def increase_depth(self):
        self.depth += 1

def to_symbol(el):
    return Symbol(el[0],el[1])

def merge(a,b):
    a.label = '0'
    b.label = '1'
    
    ab = Node(weight = a.weight + b.weight, 
              left = a,
              right  = b)
    
    return ab
     
def huffman(epsilon):
    
    while(len(epsilon) > 1):
        a = hp.heappop(epsilon)
        b = hp.heappop(epsilon)
        ab = merge(a,b)
        hp.heappush(epsilon,ab)
        
def decode(tree,symbol):
    pass

  
### IMPLEMENTATION ###
info, data = read_data('huffman.txt')
data = [3,2,6,8,2,6]
epsilon = list(map(lambda el: Node(weight = el[1],symbol = str(el[0])),list(enumerate(data))))
hp.heapify(epsilon)
huffman(epsilon)    
