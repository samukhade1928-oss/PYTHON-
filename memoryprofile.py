from memory_profiler import profile
@profile
def memory_profile():
    a = [i for i in range(1000)]
    b = [i**2 for i in range(1000)]
    return a,b

if __name__ == "__main__":
    result = memory_profile()
    print(len(result))