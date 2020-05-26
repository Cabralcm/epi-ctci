from typing import *

#Naive recursive fib
#Time Complexity: O(n^2)
#Space Complexity O(n^2) --> due to the stack calls
def fib(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fib (n-1) + fib(n-2) 


#Na
def fib_dp(n: int) -> int:
    if n <= 1:
        return n
    elif 