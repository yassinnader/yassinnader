import time
import random
import matplotlib.pyplot as plt

# Linear Search
def linear_search(arr, target):
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons
    return -1, comparisons

# Binary Search
def binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# مقارنة على أحجام مختلفة
sizes = [100, 1000, 10000, 100000, 1000000]
linear_times = []
binary_times = []
linear_comps = []
binary_comps = []

for size in sizes:
    arr = sorted(random.sample(range(size * 10), size))
    target = arr[-1]

    start = time.perf_counter()
    _, lin_comp = linear_search(arr, target)
    lin_time = time.perf_counter() - start

    start = time.perf_counter()
    _, bin_comp = binary_search(arr, target)
    bin_time = time.perf_counter() - start

    linear_times.append(lin_time)
    binary_times.append(bin_time)
    linear_comps.append(lin_comp)
    binary_comps.append(bin_comp)

# رسم الزمن
plt.figure(figsize=(10, 5))
plt.plot(sizes, linear_times, marker='o', label='Linear Search Time')
plt.plot(sizes, binary_times, marker='o', label='Binary Search Time')
plt.xlabel("Array Size")
plt.ylabel("Time (seconds)")
plt.title("Search Time vs Array Size")
plt.legend()
plt.grid(True)
plt.show()

# رسم عدد المقارنات
plt.figure(figsize=(10, 5))
plt.plot(sizes, linear_comps, marker='o', label='Linear Search Comparisons')
plt.plot(sizes, binary_comps, marker='o', label='Binary Search Comparisons')
plt.xlabel("Array Size")
plt.ylabel("Comparisons")
plt.title("Comparisons vs Array Size")
plt.legend()
plt.grid(True)
plt.show()