#Author: Mariano Leonel Acosta
#Github: mlacosta
#mail: marianoacosta.003@gmail.com
#date: Aug 26th 2020
#
#Calculate number of clusters such that max dist >= 3

### HEADER ###
import clustering as ctr

def bin2dec(num,size):
    dec = 0        
    for bit in num:
        dec += (2 ** size) * bit
        size -= 1
    return dec

def decList()
# IMPLEMENTATION 