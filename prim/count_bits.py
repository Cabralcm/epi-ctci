from typing import *

def count_ones(num: int) -> int:
    num_1_bits = 0
    while num:
        num_1_bits += num & 1
        num = num >> 1
        # num >>= 1
    return num_1_bits

def count_zeros(num: int) -> int:
    num_0_bits = 0
    length = bit_length(num)
    ones = 2**(length) - 1
    num = num ^ ones 
    while num:
        num_0_bits += num & 1
        num >>= 1
    return num_0_bits

def bit_length(num :int) -> int:
    length = 0
    while num:
        length += 1
        num >>= 1
    return length


# Testing
x = 31 #All ones (5 in total)
print("\n"f"Num: {x}")
print(f"Bit length: {bit_length(x)}")
print(f"Num of ones: {count_ones(x)}")
print(f"Num of zeros: {count_zeros(x)}")

# Testing
x = 32 #Single one, 5 zeros
print("\n"f"Num: {x}")
print(f"Bit length: {bit_length(x)}")
print(f"Num of ones: {count_ones(x)}")
print(f"Num of zeros: {count_zeros(x)}")
