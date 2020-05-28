# Primitives

## Prims in Python

Ints in Python3 - unbounded, the maximum integer representable is a function of the available memory

`sys.maxsize` - can be used to find the word-size
- corresponds to the maximum value int that can be stored in the word (within the memory blocks)
- e.g. 2^63-1 --> corresponds to the size an int on a 64-bit machine
- `sys.float_info` - bounds on floats


## Bootcamp and Helpful Hints

```
Be vary comfortable with BITWISE operators, particularly XOR

Understand how to use masks (bit-wise masks) and create them in an machine INDEPENDENT way

Know fast ways to CLEAR the Lower-most Set Bit. To SET the lower-most 0 bit. Get it's index. And other related operations.

Consider using a CACHE to accelerate operations by using it to brute-force small inputs.

Be aware that commutativity and associativity can be used to perform operation in parallel and recorder operations.
```

## Bit-wise operators:
`&`


Variables
- Come in types
- Type --> Classification of data that provides the possible encodings for information to be represented
- I.e. The possible values for that type, and the operations that are allowed to be performed on it

### Bit shifting

```
x >> num - right shift (shift x by num bits to the right)
x << num  - left shift (shift x by num bits to the left)
x & y - bit-wise AND
x | y - bit-wise OR
x ^ y - bit-wise XOR
```
