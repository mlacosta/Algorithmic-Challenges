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
        
class Node:
    def __init__(self, symbol = None, label = None,left = None ,right = None):
        self.label = label
        self.left = left
        self.right = right
        self.symbol = symbol
        self.explored = False
    
    def is_explored(self):
        return self.explored
    
    def __str__(self):
        return 'Label: %s, Symbol: %s'%(self.label,self.symbol)

def to_symbol(el):
    return Symbol(el[0],el[1])

def create_node(s_tree,label):

    if len(s_tree) == 2:
        left = Node(symbol = s_tree[0], label = '0')
        right = Node(symbol = s_tree[1], label = '1')
        return Node(left=left, right=right, label= '1')
    
    else:
        left = Node(symbol = s_tree[0], label = '0')
        right = create_node(s_tree[1:],label = '1')
        return Node(left=left, right=right, label = label)
    
    
def decompress(tree):
    s_left = tree.left.symbol.split()
    s_right = tree.right.symbol.split()
    
    left = create_node(s_left,'0')
    right = create_node(s_right, '1')
    
    return Node(left=left, right=right)
     
def huffman(epsilon):
    if len(epsilon) == 2:
        left = Node(symbol = epsilon[0].symbol, label = '0')
        right = Node(symbol = epsilon[1].symbol, label = '1')
        return Node(left=left,right=right)
    
    a = hp.heappop(epsilon)
    b = hp.heappop(epsilon)
    
    ab = Symbol(a.symbol + ' ' + b.symbol,a.weight + b.weight)    
    hp.heappush(epsilon,ab)
    tree = huffman(epsilon)
    
    return tree    
    
### IMPLEMENTATION ###
info, data = read_data('huffman.txt')
epsilon = list(map(lambda el: Symbol(el[0],el[1]),list(enumerate(data))))
hp.heapify(epsilon)
tree = huffman(epsilon)    
encoding  = decompress(tree)