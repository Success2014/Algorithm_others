# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 14:43:43 2015

Tower of Hanoi.

Idea:
There is a general rule for moving a tower of size n (n > 1) from the peg S (source) 
to the peg T (target):
(1) move a tower of n - 1 discs Dn-1 ... D1 from S to A (Auxillary peg). 
Disk Dn is left alone on peg S
(2) Move disk Dn to T
(3) move the tower of n - 1 discs Dn-1 ... D1 on A to T, i.e. this tower 
will be put on top of Disk Dn

So the number of steps needed to move a tower of size n is:
S[n] = 2 * S[n-1] + 1

1,3,7,15,31,63...
that is 2**n - 1



@author: Neo
"""

def hanoi(n, source, helper, target):
    if n == 1:
        target.append(source.pop())
    if n > 1:
        # move tower of size n - 1 to helper:
        hanoi(n-1, source, target, helper)
        # move disk from source peg to target peg
        target.append(source.pop())
        # move tower of size n-1 from helper to target
        hanoi(n-1, helper, source, target)
    
source = [4,3,2,1]
target = []
helper = []
hanoi(len(source),source,helper,target)

print source, helper, target    
    
    
    

