import time
def task(name):
    print('Starting ',name )
    time.sleep(2)
    print('Finished' ,name)

start = time.time()

task("A")
task("B")
task("C")
print("Time : ",time.time()-start)
