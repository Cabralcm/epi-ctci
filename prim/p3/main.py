# 64-bit input

from typing import *

# Typing Reference
# cache: Dict[int, int] = {}

PRECOMPUTED_PARITY = List[int]

def parity(x: int) -> int:
    mask_size = 16
    bit_mask = 0xFFFF #return all the bits from a 16 bit number
    return (PRECOMPUTED_PARITY[x >> (3* mask_size)] ^ 
            PRECOMPUTED_PARITY[(x >> (2*mask_size)) & bit_mask] ^
            PRECOMPUTED_PARITY[(x >> (mask_size)) & bit_mask] ^
            PRECOMPUTED_PARITY[x & bit_mask]
            )

def parity2(x:int) -> int:
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x

x = 0b11010111

def parity3(x):
    print(bin(x))
    x ^= x >> 4
    print(bin(x))
    x ^= x >> 2
    print(bin(x))
    x ^= x >> 1
    print(bin(x))
    return x

# parity3(x)

# Write expressions that use bitwise operations, equality checks, and Boolean operators to do the following in O(1) time

# 1) Right propagate the rightmost set bit in x. E.g. Turn (01010000) to (01011111)

# x&(x-1) --> x with the lowest bit erased
# x&~(x-1) - isolates the lowest bit that is 1 in x

def right(x:int) -> x:
    lower = x&~(x-1) #Extract the lowest set bit in x
    lower -= 1 #convert all LSBs below the set bit into 1s,
    x ^= lower #flip all the LSBs befow the lowest set bit in x to 1s!
    print(bin(x))

# bin_num = 0b01010000
# right(bin_num)

# 2) Compute x mod a power of two, e.g. returns 13 for 77 mod 64

def bin_mod(x:int, mod = 64) -> x:
    mod &= ~(mod-1) #Extract the lowest set bit in x
    mod = mod-1 #convert all LSBs below the set bit into 1s
    x &= mod #extract all values below the set bit using AND
    print(bin(x))
    print(x)

# bin_mod(279, mod = 4)

# 3) Test if x is a power of 2, i.e., evaluates to true for x = 1,2,3,4,8.. etc

def power_of_two(x:int) -> x:
    print(bin(x))
    erased = x&(x-1) #X with its lowest set bit erased
    if not erased:
        print("Power of Two")
        return True
    else:
        print("Not power of Two")
        return False

# power_of_two(256)






