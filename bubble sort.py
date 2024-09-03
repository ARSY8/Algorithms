
def bubble_sort(arr):
    n = len(arr)
    for i in range(0, n - 1):
        for j in range(0, n-1-i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


arr = [64, 25, 11, 12, 22, 11]

print(bubble_sort(arr))