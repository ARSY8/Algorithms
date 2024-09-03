def counting_sort(arr):
    if len(arr) == 0:
        return arr

    max_val = max(arr)

    count = [0] * (max_val + 1)

    for num in arr:
        count[num] += 1

    sorted_arr = []

    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr

arr = [53, 12, 89, 24, 67, 98, 11]
print(counting_sort(arr))