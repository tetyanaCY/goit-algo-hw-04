import random
import timeit

# Implementation of merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Implementation of insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Function to copy arrays
def copy_array(arr):
    return arr.copy()

# Timing function
def time_algorithm(algorithm, arr):
    copied_arr = copy_array(arr)
    start_time = timeit.default_timer()
    algorithm(copied_arr)
    return timeit.default_timer() - start_time

# Generate random arrays of different sizes
small_array = [random.randint(0, 100) for _ in range(100)]
medium_array = [random.randint(0, 100) for _ in range(1000)]
large_array = [random.randint(0, 100) for _ in range(10000)]

# Time each algorithm on each array size
timings = {
    'merge_sort': {
        'small': time_algorithm(merge_sort, small_array),
        'medium': time_algorithm(merge_sort, medium_array),
        'large': time_algorithm(merge_sort, large_array)
    },
    'insertion_sort': {
        'small': time_algorithm(insertion_sort, small_array),
        'medium': time_algorithm(insertion_sort, medium_array),
        'large': time_algorithm(insertion_sort, large_array)
    },
    'timsort': {
        'small': time_algorithm(sorted, small_array),
        'medium': time_algorithm(sorted, medium_array),
        'large': time_algorithm(sorted, large_array)
    }
}

# Display the timings
for sort_type, times in timings.items():
    print(f"Timing for {sort_type}:")
    for size, time in times.items():
        print(f"\tSize {size}: {time:.6f} seconds")
