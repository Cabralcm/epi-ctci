# Primitives

## Prims in Python

Ints in Python3 - unbounded, the maximum integer representable is a function of the available memory

`sys.maxsize` - can be used to find the word-size
- corresponds to the maximum value int that can be stored in the word (within the memory blocks)
- e.g. 2^63-1 --> corresponds to the size an int on a 64-bit machine
- `sys.float_info` - bounds on floats

**Variables**
- Come in types
- Type --> Classification of data that provides the possible encodings for information to be represented
- I.e. The possible values for that type, and the operations that are allowed to be performed on it


## Bootcamp and Helpful Hints

```
Be vary comfortable with BITWISE operators, particularly XOR.

Understand how to use masks (bit-wise masks) and create them in an machine INDEPENDENT way.

Know fast ways to CLEAR the Lower-most Set Bit. To SET the lower-most 0 bit. Get it's index. And other related operations.

Understand signedness and its implications to shifting.

Consider using a CACHE to accelerate operations by using it to brute-force small inputs.

Be aware that commutativity and associativity can be used to perform operation in parallel and recorder operations.
```

## Bit-wise operators:
`&` - Bit-wise AND

`|` - Bit-wise OR

pos num `>>` pos num

neg num '>>' pos num

`~' - tilde --> inversion

`^` - Bit-wise XOR

Negative numbers are treated as their 2's compliment value. No concept of an unsigned shift in Python. Since integers have infinite precision.

## Key Prim Methods
- abs(-77)
- math.ceil(2.17)
- math.floor(3.14)
- min( , , ,)
- max(, , , )
- pow(x,y) OR x**y
- Convert strings to ints (e.g. str(), int()), and str to floats (e.g. str(), float())
- Integers are infinite precision. Floats are NOT infinite precision.
   - Float Pos Inf --> float('inf')
   - Float Neg Int --> float('-inf')
   - Used to create pseduo max-int, and pseduo min-int
- math.isclose() --> when comparing FLOATING point values. It is robust (compare very large values, can handle both absolute and relative differences)

random() Library (import random)
- random.randrange()
- random.randint()
- random.random()
- random.shuffle()
- random.choice()

### Bit shifting
```
x >> num - right shift (shift x by num bits to the right)
x << num  - left shift (shift x by num bits to the left)
x & y - bit-wise AND
x | y - bit-wise OR
x ^ y - bit-wise XOR
```

### Bit-Hacking

1) x & (x - 1) --> Returns x with its lowest SET bit erased.

Ex: if x = 1011, this returns: x = 1010.

Ex2: if x = 111010, this returns: x = 111000
```
 111010
&111001
--> 111000
```

2) x & ~(x - 1) --> Isolates the lowest SET bit (i.e. the lowest bit that is 1 in x).
Ex: 
```
x= 1011
x-1 = 1010
~(x-1) = 0101
 1011
&0101
--> 0001
```
Ex2:
```
x: 11100
(x-1): 11011
~(x-1): 00100

 11100
&00100
--> 00100
```

3) Divide and Conquer Method
Given: 64 bit integer, cannot use array with 2^64 bits (2 exabytes of storage)
Instead use: 2^16 bit look-up tables, 64/16 = 4. Divide the original number into 4 sets. Determine parity using the look-up tables.
Add or concatenate the results from the look-up tables. If the number of 1's is ODD --> function returns 1. Else, return 0!
