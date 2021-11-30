"""
Author: Atahan Koc
Description Part: The idea is to loop from 1 to n and keep adding to the main output while recurring with the remaining required total.
When we get 0 we know we've reached the requisite sum and may print the combinations. We expand in decreasing order to avoid permutations.
"""

def combinations(start, end, result, index):

    if end == 0:
        print(result[: index])

    for i in range(start, end + 1):
        result[index] = i
        # recur with reduced sum
        combinations(i, end - i, result, index + 1)


N = int(input("Enter value for n:: "))
res = [None] * N  # initializing output array
combinations(1, N, res, 0)