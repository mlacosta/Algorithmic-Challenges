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
        return 'Label: %s, Symbol: %s Depth: %s'%(self.label,self.symbol,self.depth)

    def __lt__(self,other):
        return self.weight < other.weight
    
    def increase_depth(self):
        self.depth += 1

def to_symbol(el):
    return Symbol(el[0],el[1])

def create_node(s_tree, label, depth = 0):

    if len(s_tree) == 2:
        left = Node(symbol = s_tree[0], label = '0',depth = depth + 2)
        right = Node(symbol = s_tree[1], label = '1',depth = depth + 2)
        return Node(left=left, right=right, label= '1',depth = depth + 1)
    
    else:
        left = Node(symbol = s_tree[0], label = '0',depth = depth + 2)
        right = create_node(s_tree[1:],label = '1',depth = depth + 1)
        return Node(left=left, right=right, label = label, depth = depth + 1)

def merge(a,b):
    a.label = '0'
    b.label = '1'
    
    ab = Node(symbol = a.symbol + ' ' + b.symbol, 
              weight = a.weight + b.weight, 
              left = a,
              right  = b)
    
    return ab
     
def huffman(epsilon):
    
    while(len(epsilon) > 2):
        a = hp.heappop(epsilon)
        b = hp.heappop(epsilon)
        ab = merge(a,b)
        hp.heappush(epsilon,ab)
        
    a = epsilon[0]
    b = epsilon[1]
    return merge(a,b) 


def decode(tree,symbol):
    pass

  
### IMPLEMENTATION ###
info, data = read_data('huffman.txt')
epsilon = list(map(lambda el: Node(weight = el[1],symbol = str(el[0])),list(enumerate(data))))
hp.heapify(epsilon)
tree = huffman(epsilon)    
