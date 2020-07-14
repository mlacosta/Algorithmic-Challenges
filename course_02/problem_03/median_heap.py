#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: July 13th 2020
#
#Implement a "Median Maintenance" algorithm using a Heap Data structure
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


def medianMaintenance(data):
    """
        computes the median of a stream of integers as they are read in secuencial order
        parameters: 
            data (list): stream of integers
        returns
            medians (list): stream of medians
    """
    
    minHeap = []
    maxHeap = []
    hp.heapify(minHeap)
    hp.heapify(maxHeap)
    
    medians = []
    
    for val in data:

        #fill the heaps while they are empty
        if not(len(maxHeap)):
            medians.append(val)
            hp.heappush(maxHeap,-val)
            continue
        elif not(len(minHeap)):
            if val< -maxHeap[0]:
                hp.heappush(minHeap,-hp.heappop(maxHeap))
                hp.heappush(maxHeap,-val)
                medians.append(val)
            else:
                hp.heappush(minHeap,val)
                medians.append(-maxHeap[0])
            continue
        
        #put in heaps
      
        if val<= -maxHeap[0]:
            hp.heappush(-maxHeap[0],-val)
        else:
            hp.heappush(minHeap,val)
            
        #balance heaps
        
        if abs(len(maxHeap) - len(minHeap))==2:
            if(len(maxHeap)>len(minHeap)):
                hp.heappush(minHeap,-hp.heappop(maxHeap))
            else:
                hp.heappush(maxHeap,-hp.heappop(minHeap))
        
        #obtain median
  
        if (len(maxHeap) >= len(minHeap)):
            medians.append(-maxHeap[0])
        else:
            medians.append(minHeap[0])
        
    return medians
              
### END HEADER ###

### IMPLEMENTATION

parsedData = readData('median.txt')
medians = medianMaintenance(parsedData)
print('sum of first 10000 medians (last four digits): %d'%(sum(medians)%10000))