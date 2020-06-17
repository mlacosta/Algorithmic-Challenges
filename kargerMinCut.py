#Author: Mariano L. Acosta
#17 June 2020

with open('kargerMinCut.txt') as f:
    nodes = f.read().splitlines()
    
#Preprocessing 
    
nodesArray = []

for node in nodes: #removes tabspace
    nodesArray.append(node.split('\t'))
    
for node in nodesArray: #removes empty element
    node.pop(-1)
    
#convert to integer
def ToInt (array):
    return int(array)
        
    
nodes = []    

for node in nodesArray:
    nodes.append(list(map(ToInt,node)))
    