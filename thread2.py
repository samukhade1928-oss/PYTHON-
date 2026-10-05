from  threading import *

def display():
    for i in range(10):
        print('Child Thread')   
t = Thread(target=display)
t.start()                 

#executing the main thread
for i in range(10):
    print('Main thread')