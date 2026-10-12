'''
Reference Counting
objects - lists, tuple,set ,dic,variables etc.
'''

import sys
a=[0,1,2,3]#1
#getrefcount #1
#Total : 2
b=a
c=b
del c,b
print(f"Total objeccts in Ram: {sys.getrefcount(a)}")