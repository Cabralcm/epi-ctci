from typing import *
import time

#Naive recursive fib
#Time Complexity: O(n^2)
#Space Complexity O(n^2) --> due to the stack calls
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2) 


#Fib with DP (memozied solution)
#Time - O(n)
#Space - O(n)
cache: Dict[int, int] = {}

def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fib_dp(n-1) + fib_dp(n-2)
    return cache[n]

# DP Fib with Minimized Cache Space
# Looks like iterative method
# Time - O(n)
# Space - O(1)
def fib_cache(n:int) -> int:
    if n <= 1:
        return n
    f_2, f_1 = 1,0
    for _ in range(0,n):
        f = f_2 + f_1
        f_2, f_1 = f_1, f
    return f_1

#Testing
n_list = [2,4,8,16,32]
funcs = {"Fib":fib, "Fib DP":fib_dp, "Fib Cache":fib_cache}
for name,func in funcs.items():
    print(name)
    for n in n_list:
        start = time.time()
        print(func(n))
        end = time.time() - start
        print(f"Fib({n}) completed in {end} seconds")