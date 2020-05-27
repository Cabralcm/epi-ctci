from typing import *

'''
H-index - a matrix that measures the productivity and citation impact of a researcher
H-index: Largest number h, s.t. the researcher has published h papers that each have been cited at least h times
'''

my_list = [4,1,2,4,5,10,22,12,4,20]

#Brute Force
# T: O(n^2) --> Unacceptable
# S: O(n) the input, O(1) --> variable, counter, etc
def h_index(input: List[int])-> int:
    h_index = 0
    count = 0
    while (count >= h_index):
        count = 0
        h_index += 1
        for paper in input:
            if paper >= h_index:
                count += 1
        h_index += 1
    return h_index - 1

print(h_index(my_list))

#            

