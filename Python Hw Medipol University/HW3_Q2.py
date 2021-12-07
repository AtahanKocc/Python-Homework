"""
Author: Atahan Koc
Description Part: This algorithm is used to sort integers of the floating type. It operates by dividing the array into an average number of buckets.
Execution takes linear time. In this code, it was calculated that (n + k) is the execution time, and it was shown that the average complexity of the draw and bucket order is O (n + k), and the output was successfully obtained.
"""
import math
import time
from random import randint
import matplotlib.pyplot as plt

def bucket_sort(lst):
    # check the list if it's empty or not
    if len(lst) == 0:
        return lst
    bucket_size = 100  # The bucket size is chosen as 100
    # The maximum and minimum values are determined by the number of buckets used to distribute the numbers.
    min_value = min(lst)
    max_value = max(lst)
    n_buckets = int(math.floor((max_value - min_value) / bucket_size) + 1)

    buckets = [[] for _ in range(n_buckets)]
    # The numbers are distributed to the buckets
    for i in range(0, len(lst)):
        buckets[int(math.floor((lst[i] - min_value) / bucket_size))].append(lst[i])
    lst = []  # keep the sorted elements
    for i in range(0, len(buckets)):
        buckets[i].sort()
        for j in range(0, len(buckets[i])):
            lst.append(buckets[i][j])
    return lst

# keeps execution time for different "n and k" values
timer = []
n_k = []  # keeps (n+k) for each iteration
k = 61  # range of list elements
for n in range(100, 10000, 1000):
    lst = [randint(0, k) for x in range(n)]  # The random list is implemented for the provided n and k values.
    print("k:", k)
    print("n:", n)
    # k is incremented by 100
    k += 100
    start_time = time.time()  #measure execution times
    bucket_sort(lst)
    timer.append(time.time() - start_time)  
    print("Execution Time = %s seconds " % (time.time() - start_time))
    n_k.append(n + k + 1)

# result part
plt.plot(n_k, timer)
plt.xlabel("n + k")
plt.ylabel("Time: ")
plt.title("Execution Time vs (n+k)")
plt.show()
