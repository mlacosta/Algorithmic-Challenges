#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Sep  28th 2020
#
#Huffman encoding with greedy algorithm

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
    def __init__(self, data = None, label = None,left = None ,right = None):
        self.label = label
        self.left = left
        self.right = right
        self.data = data

def to_symbol(el):
    return Symbol(el[0],el[1])
     
def huffman(epsilon):
    if len(epsilon) == 2:
        left = Node(data = epsilon[0], label = '0'), 
        right = Node(data = epsilon[1], label = '1')
        return Node(left=left,right=right)
    
### IMPLEMENTATION ###
info, data = read_data('huffman.txt')
epsilon = list(map(lambda el: Symbol(el[0],el[1]),list(enumerate(data))))
hp.heapify(epsilon)

