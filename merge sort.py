

def merge_sort(arr):
    n = len(arr)
    if n < 2:
        return arr
    else:
        left = merge_sort(arr[: n // 2])
        right = merge_sort(arr[n // 2 :])

        return merge(left, right)


def merge(left, right):
    i = j = 0
    result = []
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

arr = [64, 25, 11, 12, 22, 11]

print(merge_sort(arr))



