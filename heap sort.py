
def heapify(arr, i, n):
    largest = i
    left, right = i * 2 + 1, i * 2 +2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        return heapify(arr, largest, n)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, i, n)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)


arr = [53, 12, 89, 24, 67, 98, 11,]
heap_sort(arr)
print("Отсортированный массив:", arr)


