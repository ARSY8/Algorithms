def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            current_value = arr[i]
            position = i
            while arr[position - gap] > current_value and position >= gap:
                arr[position] = arr[position - gap]
                position -= gap
                arr[position] = current_value
        gap //= 2
    return arr




arr = [64, 34, 25, 12, 22, 11, 90]
print(len(arr))
sorted_array = shell_sort(arr)
print(sorted_array)