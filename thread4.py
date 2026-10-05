import threading
import time
def task(name):
    print("Starting" ,name)
    time.sleep(2)
    print("Finished" ,name)

start = time.time()    

threads = []

for name in["A","B","C"]:
    t = threading.Thread(target=task, args=(name))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
    print("Time : ",time.time()-start)   