'''
Circular reference = a->b & b->a
'''
import gc
class Student:
    def __init__(self,name):
        self.name = name
        self.friend=None
s1=Student("Amit") 
s2=Student("Rahul")  
s1.friend = s2
s2.friend = s1

print("Circular references created")
del s1
del s2

print("Circular references deleted")
gc.enable()
collected = gc.collect()
print("Object collected:" , collected)