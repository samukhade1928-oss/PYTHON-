'''
1.Multiprocessing - CPU
2.Threading - I/O
3.Async Programming - Fast Execution
image - Invert image , crop , scale , matrix multiplication etc - cpu process 
file reading, file writing - I/O
processor - i5 or i7
cores - 16, if more cores are available then processing power will be more
'''
import multiprocessing as mp
print(mp.cpu_count())