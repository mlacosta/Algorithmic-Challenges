#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Sep  28th 2020
#
#Huffman encoding with greedy algorithm

#I use a heap for min search and Depth First Search for encoding

### HEADER ###
def read_data(file):
    parsed_data = []
    with open(file) as data:
        parsed_data = list(map(int, data.read().splitlines()))
    
    info = parsed_data.pop(0)
    return (info , parsed_data)

def mwis(data):
    A = [0,data[0]]
    
    for i in range(2,len(data)):
        A.append(max([A[i-1],A[i-2] + data[i-1]]))
    
    return A

def reconstruct(A,data):
    S = []
    i = len(A)
    
    while i>=1:
        if A[i-1] >= (A[i-2] + data[i-1]):
            i-=1
        else:
            S.append(i)
            i-=2
    return S
            
### IMPLEMENTATION ###
info, data = read_data('mwis.txt')
A = mwis(data)
S = reconstruct(A,data)

vertex = [1,2,3,4,17,117,517,997]
result = []

for node in vertex:
    if node in S:
        result.append(1)
    else:
        result.append(0)
        
