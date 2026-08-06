#Uses Singleton(Single-ton)
#Database connection class
#Logger 
# Configuration manager
#Cache manager
#printer spooler


class Singleton:

     def __init__(self):
          pass


     '''
     
                         _instance = None
                def __new__(cls):
                        if cls._instance is None:
                                print("Creating a new Object")
                                cls._instance = super().__new__(cls)
                        return cls._instance

    '''                    
#  createing objects  
obj1= Singleton()  
print(id(obj1))              
obj2= Singleton()
print(id(obj2))
print( obj1 is obj2)