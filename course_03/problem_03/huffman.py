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

class Node:
    def __init__(self, symbol = None, label = None,left = None ,right = None, 
                 weight = None, parent = None):
        self.label = label
        self.left = left
        self.right = right
        self.symbol = symbol
        self.__explored = False
        self.weight = weight
        self.parent = parent
    
    def is_explored(self):
        return self.__explored
    
    def set_explored(self):
        self.__explored = True
        
    def __str__(self):
        return 'Label: %s, Symbol: %s, Weight: %d'%(self.label,self.symbol,self.weight)

    def __lt__(self,other):
        return self.weight < other.weight
    
def merge(a,b):
    a.label = '1'
    b.label = '0'
    ab = Node(weight = a.weight + b.weight, 
              left = b,
              right  = a)
    a.parent = ab
    b.parent = ab
    return ab
     
def huffman(epsilon):
    
    while(len(epsilon) > 1):
        a = hp.heappop(epsilon)
        b = hp.heappop(epsilon)
        ab = merge(a,b)
        hp.heappush(epsilon,ab)
        
def backtrack(node):
    codeword = ''
    val = node
    
    while val.parent != None:
        codeword = val.label + codeword
        val = val.parent
    
    return codeword
    
def DFS_decode(tree,symbol):
    tree.set_explored()

    if tree.symbol == symbol:
        print('found')
        print(backtrack(tree))
    
    if not(tree.right == None):
        if not tree.right.is_explored():
            DFS_decode(tree.right,symbol)
            
    if not(tree.left == None):
        if not tree.left.is_explored():
            DFS_decode(tree.left,symbol)

### IMPLEMENTATION ###
info, data = read_data('huffman.txt')
epsilon = list(map(lambda el: Node(weight = el[1],symbol = str(el[0])),list(enumerate(data))))
hp.heapify(epsilon)
huffman(epsilon)    
tree = epsilon[0]
DFS_decode(tree,'0')
