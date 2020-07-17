# Swap bits

# 64 bit integer
# Take 64-bit int, swap bits at indicies i and j
# Q: When is the swap necessary? If the bits being swapped are DIFFERENT! 
# If the bits being swapped are different, then it is the same as flipping their individual values.

from typing import *

def swap(x:int, i:int, j:int ) -> x:
    # Extract the i-th and j-th bits, and see if they differ
    # The index j or j are the bit positions, thus we can use bit shifting, and then 0x1 mask to extract the i-th and j-th bit respectively
    if (x >> i) & 1 != (x >> j) & 1: 
        # i-th and j-th bits, differ. We will swap them by flipping their respective values
        # Select the bits to flip with bit_mask.
        # Since x^1 = 0, when X =1, and 1 when x = 0. Thus we can perform the flip XOR

        bit_mask = (1 << i) | (1 << j)
        x ^= bit_mask
    return x

# Reverse Bits

# Take a 64-bit unsinged integer and returns the 64-bit unsigned integer consisting of the bits of the input in reverse order.

# Hint: Use a look-up table

# Akin to using 16-bit look-up tables for finding the parity of a 64-bit integer, we can employ the same technique for reversing the 64-bit integer
# number = y3,y2,y1,y0 = MSB -- LSB
# rev_number = rev(y0), rev(y1), rev(y2), rev(y3) 
# where rev() is a look up table A, where A[y] = bit-reversal of y
# 2 bit look up table is A = [00, 10, 01, 11], for indices = 00, 01, 10, 11!

# Input is 64-bit integer, 
def reverse(x:int) -> x:
    mask_size = 16
    bit_mask = 0xFFFF
    return (PRECOMPUTED_REVERSE[x & bit_mask] << (3* mask_size) |
            PRECOMPUTED_REVERSE[(x >> mask_size) & bit_mask] << (2*mask_size) | 
            PRECOMPUTED_REVERSE[(x >> 2*(mask_size)) & bit_mask] << mask_size |
            PRECOMPUTED_REVERSE[(x >> 3*(mask_size)) & bit_mask]
            )

# The time complexity of this is equivalent to the Look-up table for parity, which is
# O(n/L), for n-bit integers, and L-bit cache keys (or LUTs)










