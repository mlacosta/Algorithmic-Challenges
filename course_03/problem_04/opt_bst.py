#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Oct  15th 2020
#
#Optimal Binary Search Tree cost calculation

### HEADER ###

import numpy as np


def opt_bst(values):
    
    '''
        Computes an optimal binary search tree given a set of probabilities
        
        Params:
            values (list): input probabilities
        
        Returns:
            the optimal cost, i.e: the avg search time
    '''
    
    n = len(values) 
    A = np.zeros((n + 1 )**2).reshape(n + 1 ,n + 1 )
    
    for s in range(n):
        for i in range(n):
            inx = i + s + 1
            inx =  inx  if (inx < n) else n
            cost = 10e9
            
            for r in range(i,inx):
                temp = 0
                first = 0 if (i > inx) else A[i,r-1]
                second = 0 if ( (r + 1) > ( inx -1 ) ) else A[r+1,inx-1]
                sum_pk = 0
                
                for k in range(i,inx):
                    sum_pk += values[k]
                
                temp = sum_pk + first + second
                cost = temp if temp<cost else cost
            
            A[i,inx-1] = cost
    
    return A[0,n-1]
                

print(opt_bst([.05,.4,.08,.04,.10,.10,.23]))

