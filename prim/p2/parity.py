from typing import *

#Computing Parity
#Q: Compute parity of  a very large number of 64-bit words?

#Returns 1 if number of 1 bits is ODD
#Returns 0 if number of 1 bits is EVEN

#Hint: Use a lookup table, but don't use 2^64 entries!

#Count the number of bits, apply mod 2
def parity_bf(n:int)-> int:
    ans = 0
    while x:
        ans += x & 1
        x >> 1
    return ans % 2

#Flip bit if 1-bit is found, o.w do nothing. Start from 0 bits found.
# 1 == True, 0 == False
# T: O(n), n == The word size.
# S: O(1)
def parity_bf2(n:int) -> int:
    ans = 0
    while x:
        ans ^= x & 1
        x >> 1
    return ans


# Bit erasure solution
# If k is the number of bits set to 1,
# Then, T.C is O(k), instead of O(n) for brute force
def parity_erasure(n:int) -> bool:
    ans = 0
    while x:
        ans ^= 1 #flip the bit count
        x &= x - 1 #erase the least significant set bit (lowest set bit)
    return ans

def 

cache: Dict[int, bool] = {}

def parity_dp(n:int) -> bool:
    return