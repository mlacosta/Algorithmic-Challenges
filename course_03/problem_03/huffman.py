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
    def __init__(self, symbol = None, label = None,left = None ,right = None, depth = 0):
        self.label = label
        self.left = left
        self.right = right
        self.symbol = symbol
        self.__explored = False
        self.depth = depth
    
    def is_explored(self):
        return self.__explored
    
    def set_explored(self):
        self.__explored = True
        
    def __str__(self):
        return 'Label: %s, Symbol: %s Depth: %s'%(self.label,self.symbol,self.depth)

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
    
def decompress(tree):
    s_left = tree.left.symbol.split()
    s_right = tree.right.symbol.split()
    left = create_node(s_left,'0', depth = 0)
    right = create_node(s_right, '1', depth = 0)
    
    return Node(left=left, right=right)
     
def huffman(epsilon):
    print('----')
    for s in epsilon:
        print(s)
    
    if len(epsilon) == 2:
        left = Node(symbol = epsilon[1].symbol, label = '0')
        right = Node(symbol = epsilon[0].symbol, label = '1')
        return Node(left=left,right=right)
    
    a = hp.heappop(epsilon)
    b = hp.heappop(epsilon)
    
    ab = Symbol(a.symbol + ' ' + b.symbol,a.weight + b.weight)
    


    hp.heappush(epsilon,ab)
    tree = huffman(epsilon)
    
    return tree    

def DFS(encoding,symbol, max_depth = 0):
    
    encoding.set_explored()
    
    if encoding.symbol == symbol:
        print("Symbol found, depth = %d"%encoding.depth)
        return
    
    if not(encoding.right == None):
        if not(encoding.right.is_explored() and (encoding.right.symbol == None)):
            DFS(encoding.right,symbol)
    
    if not(encoding.left == None):
        if not(encoding.left.is_explored() and (encoding.left.symbol == None)):
            DFS(encoding.left,symbol)
    
    return
    
### IMPLEMENTATION ###
info, data = read_data('huffman.txt')
data = [3,2,6,8,2,6]
epsilon = list(map(lambda el: Symbol(el[0],el[1]),list(enumerate(data))))
hp.heapify(epsilon)
tree = huffman(epsilon)    
encoding  = decompress(tree)