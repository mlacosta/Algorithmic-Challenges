#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Oct  15th 2020
#
#Knapsack optimization problem


### HEADER ###
import numpy as np

def read_data(file):
    parsed_data = []
    with open(file) as data:
        parsed_data = list(data.read().splitlines())
    
    info = parsed_data.pop(0)
    info = map(int,list(info.split()))
    return (info , parsed_data)


def knapsack(capacity ,size, data):
    
    '''
        Calculates the max value in the knapsack problem
        
        params:
            - capacity (int)
            - size(int)
            - data from read_data()
        
        returns:
            - the optimal vax value
    '''
    
    A = np.zeros(((size + 1),capacity))
    
    for i in range(1,size + 1):
        for x in range(capacity):
            wi = int(list(data[i-1].split())[1])
            vi = int(list(data[i-1].split())[0])
            A[i,x] = A[i-1,x] if (wi > x) else max(A[i-1,x],A[i-1,x - wi] + vi) 
    
    return A[size,capacity-1]
        
(capacity ,size), data = read_data('knapsack1.txt')
A = knapsack(capacity ,size, data)

