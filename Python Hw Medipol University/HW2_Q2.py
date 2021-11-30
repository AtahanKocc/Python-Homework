"""
Author: Atahan Koc
Description Part: In this question, the difference in permutations, that is, the length of each list, is printed.
"""

def permutation(ls, rs):  # Takes 2 lists as parameters

    ls_copy = ls.copy()  # copy the first list to ls_copy
    for i in ls:
        if i in rs:  # if the element exists in second list  : rs
            rs.remove(i)  # remove that element in second list : rs
            ls_copy.remove(i)  # remove that element from the copy of first list : ls_copy
    # At the end of this for loop all elements that exist in both the given input lists are removed
    # if loop checks if length of two lists are 0
    if len(rs) + len(ls_copy) == 0:
        return True
    # else,print the difference in permutations i.e the length of each list
    # This is indirectly the number of elements left in both list
    print('Difference in elements : ', len(rs) + len(ls_copy))
    return False

print(permutation([10, 9, 11, 1], [9, 1, 11, 10]))
print(permutation([10, 9, 1, 10], [8, 1, 11, 10]))
print(permutation([8, 8, 8, 8, 8, 8, 9], [8, 8, 9, 8, 8, 8, 8]))
print(permutation([8, 9, 8, 9, 8, 9, 8, 8], [8, 9, 8, 9, 8, 9]))