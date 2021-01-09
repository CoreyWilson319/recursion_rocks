# You will have to figure out what parameters to include
# 🚨 All functions must use recursion 🚨

# def find_max(l):
#     # check if the length of l is greater than 1 otherwise the max is l
#     # check every index of l and store a value for what has been the high so far
#     ordered_list = sorted(l)
#     max = ordered_list[-1]
#     return max

# This function returns the largest number in a given array.

def find_max(l):
    max = 0
    if len(l) == 1:
        max = l[0]
        return print(max)
    if len(l) > 0:
        if l[0] > l[1]:
            del l[1]
        else:
            del l[0]
        find_max(l)


find_max([1, 4, 45, 6, -50, 10, 2])
# => 45
