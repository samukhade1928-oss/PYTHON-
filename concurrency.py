import threading

def task():
     print("Thread running")

thread = threading.Thread(target=task) 
print(f'thread created:{thread.name}')    