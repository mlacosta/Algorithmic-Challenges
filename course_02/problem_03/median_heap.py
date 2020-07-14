#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: July 13th 2020
#
#Implement A "Median Maintenance" algorithm using a Heap Data structure
#

### HEADER ###
import heapq as hp

def readData(filename):
    '''
        parameters:
            filename (string): Name of the txt file you want to read 
        returns:
            parsedData (list): parsed data.
    '''
    parsedData = []
    
    with open(filename) as f:
        data = f.read().splitlines()
    
    for val in data:
        parsedData.append(int(val))
    
    return parsedData


### END HEADER ###

### IMPLEMENTATION