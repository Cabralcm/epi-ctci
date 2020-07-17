# Efficient Parity

Cache'ing --> split 64 bit number into 4 x 16 bit numbers. 

Each 16 bit number is stored in an array. Where the index is the number, and the value stored at that index is the parity.
1) ODD parity = 1
2) EVEN parity = 0

itime complexity - function of the size of the keys used to index the lookup table. 
**L** is the width of the words for which we cache the results, and **n** the word size.
That is L is the size of the array/list that caches the 16 bit parity results, and n is the 64-bit input word.

Thus the time complexity: `O(n/L)`.

This assumes word-level operations, such as shifting, which take O(1) time. 

This does NOT include the time for initalization of the lookup table.

We can improve on the O(n) worst-case time complexity of the previous algorithms by exploiting some simple properties.

XOR - it is both Associative and Commutative
1) Associative - It doesn't matter how we group bits
2) Commutative - The order in which we perform the XOR operation does not change the result

XOR of a group of bits == It's parity

Use the CPU's word-level XOR instruction to process multiple bits at a time.

# Parity with Shifting

The time complexity is `O(logN)`, where you perform division by 2, and taking the XOR of the remaining portions with one another

```
def parity(x:int)-> x:
    x ^= 32
    x ^= 16
    x ^= 8
    x ^= 4
    x ^= 2
    x ^= 1
    return x
```

We can combine caching with word-level operations (e.g. doing a lookup in the XOR-based approach once we get to 16 bits).

# Speed improvement 

Sparse-level inputs -> IMPROVEMENTS/OPTIMIZED version of the brute-force algorithm are very fast on sparse level inputs

Random inputs -> The refinement of the brute-force is roughly 20% faster than brute-force algorithms

Table-based approach is four times faster still, and using associativity reduces run time by another factor of two!



