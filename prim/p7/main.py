# Compute quotient without arithmetical operators
# Given two positive integers, compute their quotient, using only the addition, subtraction, and shifting operators

# Hint: relate x/y to (x-y)/y

'''
brute force approach 

iteratively subtract y from x until what remains is less than y

The number of such subtractions is exactly the quotient, x/y

The remainder is the term that's less than y.

The complexity of the brute-force approach is very high, e.g., when y =1, and x = 2^31-1, it will take 2^31-1 iterations.
'''

'''
Better Approach

- try to get more work done in each iteration

- compute the largest k such that 2^ky <= x, subtract 2^ky from x, and add 2^k to the quotient

for example, x=(1011), and y = (10), then k =2, since 2 X 2^2 <= 11, and 2 x 2^3 > 11

We subtract (1000) from (1011) to get (11), add 2^k = 100 to get the quotient, and continue by updating x to (11).
 
'''