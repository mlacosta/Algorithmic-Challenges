# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 17:36:23 2020

@author: Deep Marian
"""
import math



def karatsuba(x,y):
	"""Function to multiply 2 numbers in a more efficient manner than the grade school algorithm"""
	if int(math.log10(x)) + 1 == 1 or int(math.log10(y)) == 1:
		return x*y
	else:
		n = max(int(math.log10(x)+1),int(math.log10(y)+1))
		nby2 = n / 2
		
		a = x / 10**(nby2)
		b = x % 10**(nby2)
		c = y / 10**(nby2)
		d = y % 10**(nby2)
		
		ac = karatsuba(a,c)
		bd = karatsuba(b,d)
		ad_plus_bc = karatsuba(a+b,c+d) - ac - bd
        
        	# this little trick, writing n as 2*nby2 takes care of both even and odd n
		prod = ac * 10**(2*nby2) + (ad_plus_bc * 10**nby2) + bd

		return prod
    
n = 4
x = random.randrange(10**(n-1),10**n)
y = random.randrange(10**(n-1),10**n)
k = karatsuba(x,y)

print('x:%d, y:%d\n'%(x,y))
print('karatzuba:%d\n'%k)
print('normal mult:%d\n'%(x*y))
print('error:%d\n'%(abs(x*y-k)))


