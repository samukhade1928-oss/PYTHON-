import tracemalloc
tracemalloc.start()

data = []
for i in range(10000):
    data.append(i)

current, peak = tracemalloc.get_traced_memory()
print(f"Current Memory : {current/1024 } KB")
print(f"Peak Memory : {peak/1024 } KB")
tracemalloc.stop()
