# Compute product without arithmetical operators

# Sometimes processors in ultra low-power device (such as hearing aids) do not have dedicated haredware for performing multiplciation
# A program that needs to perform multiplciation must do so explicitly using lower-level primitives

# Problem 1

'''
Write a program that multiples two nonnegative integers.
The only operators you are allowed to use are:

- assignment
- bitwise operators ( >> , << | , &, ~ ,^)
- equality checks and boolean combinations thereof

You may use loops and functions that you write yourself.

These constraints imply, for example, that you cannot use increment or decrement, or test if x < y
'''

'''
Brute force solution 
1) perform repeated addition - time complexity very high O(2^n)

2) Grade school multiplication - uses shift and add to achieve much better time complexity

Do the same with binary numbers - to multiply x and y, initialize the result to 0, 
and iterate through the bits of x, adding 2^k*y to the result if the kth bit of x is 1.

The value 2&ky can be computed by left-shifting y by k

we cannot use ADD directly, thus we must implement it

We apply the grade-school algorithm for addition to the binary case, 
i.e. compute the sum bit-by-bit, and "rippling" the carry along.

multiply 13 by 9
(1101), (1001)

LSB of 13 is 1, thus we add 1001 to the result
next bit of 13 is 0, thus we pass this bit (since it adds 0 to the result)
next bit is 1, shift (1001) to the left by 2 to obtain (100100), and add it to the current result of 1001
This gives us: 101101
The fourth and final bit of 1101 is 1, thus we shift (1001) to the left by 3, to obtain (1001000), which we 
add to 101101 to get 1110101, which is 117

Each addition is itself performed bit-by-bit. 

When adding (101101) and (1001000), the LSB of the result is 1, since exactly one of the two LSBs of the operand is 1
The next bit is 0, since both the next bits of the operands are 0
The next bits is 1 (since exactly one of the next bits of the operands is 1)
The next bit is 0 (since both of the next bits of the operands are 1)
We also 'carry' a 1 to the next position.
The next bit is 1 (since the carry-in is 1, and both the next bits of the operands are 0).
The remaining bits are assigned similarly
'''

def multiply(x: int, y:int) -> int:
    def add(a,b):
        while b:
            carry = a & b
            a,b = a ^ b, carry << 1
        return a
    
    running_sum = 0
    while x:
        if x & 1: #examines each bit of x
            running_sum = add(running_sum, y)
        x,y = x >> 1, y << 1
    return running_sum

# Time complexity is O(n), where n is the number of bits needed to represnt the operands.
# Since we do n additions to perform a single multiplication, the total time complexity is O(n^2)

test = 0b1101
test2 = 0b1001

test3 = test + test2

print(bin(test&test2))
print(bin(test3))


