import sys 
a=10
b='Python Programming'
c=[1,2,3,4,5]
d={'name' :'Amit' , 'age' : 25}

print(f"Integer Size {sys.getsizeof(a)}")
print(f"String size {sys.getsizeof(b)}")
print(f"list size {sys.getsizeof(c)}")
print(f"Dictionary size {sys.getsizeof(d)}")