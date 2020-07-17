# Closest integer with the same weight

# weight - nonengative interger is the numnber of bits that are set to 1  in its binary representation
# E.g. 92 - (1011100), weight of 92 is 4

'''
Diff = | y - x |
flip  the bit at index k1, flip the bit at index k2, k1 > k2
absolute value of the diff between the original integer and the new one is 2^k1-2^k2
to minimize this: k1 should be as small as possible, and k2 is as close to k1

must preserve the weight, bit at index k1 has to be different from the bit in k2
Otherwise the flips lead to an integer with different weight.

Smallest k1 is the rightmost bit that's "different" from the LSB, and k2 must be the very next bit.
- thus extract the first right most bit --> x&~(x-1)
- x&(x-1) - x with the lowest bit erased

correct approach is to swap the two rightmost consecutive bits that differ
'''

from typing import *

#Variant Solution

def smallest_diff(x:int) -> int:
    high_bit = x << 1
    length = len(bin(high_bit)) - 3
    mask = (1 << length) - 1
    if (not(x ^ mask)): #x is completely 1's
        erase_bit = 1 << (length-1)
        output = high_bit - erase_bit + 0b1
    else:
        lowest_bit = x&~(x-1)
        shift_bit = lowest_bit >> 1
        remove_lowest_bit = x&(x-1)
        output = remove_lowest_bit ^ shift_bit
    print("Output")
    print(bin(output))
    return output

def closest_int_same_bit_count(x:int) -> int:
    num_unsigned_bits = 64
    for i in range(num_unsigned_bits -1):
        if(x >> i) & 1 != (x >> (i + 1)) & 1:
            x ^= (1 << i) | (1 << (i+1)) #Swaps bit-i and bit-(i + 1)
            return x
    # Raise error is fall bits of x are 0 or 1.
    raise ValueError('All bits are 0 or 1')




x = 0b111111111
smallest_diff(x)
