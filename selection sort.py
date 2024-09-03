import random
def selection_sort(arr):
    for i in range(len(arr)):
        min_number = arr[i]
        min_index = i
        for j in range(i + 1, len(arr)):
            if min_number > arr[j]:
                min_number = arr[j]
                min_index = j
        if min_index != i:
            # t = arr[i]
            # arr[i] = arr[min_index]
            # arr[min_index] = t
            arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


arr = [64, 25, 11, 12, 22, 11]

print(selection_sort(arr))
