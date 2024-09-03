
def table(image):
    unique = set()
    dictionary = {}
    m = len(image)

    for i in range(m - 2, -1,-1):
        if image[i] not in unique:
            dictionary[image[i]] = m - i - 1
            unique.add(image[i])

    if image[m - 1] not in unique:
        dictionary[image[m - 1]] = m

    dictionary["*"] = m
    return dictionary


def search(image, lane):
    dictionary = table(image)
    m = len(image)
    n = len(lane)
    if n >= m:
        i = m - 1
        while(i < n):
            k = 0
            for j in range(m-1, -1,-1):
                if lane[i - k] != image[j]:
                    if j == m - 1:
                        off = dictionary[lane[i]] if dictionary.get(lane[i], False) else dictionary["*"]
                    else:
                        off = dictionary[image[j]]

                    i += off
                    break

                k += 1

            if j == 0:
                print(f"Образ найден по индексу {i - k + 1}")
                break
        else:
            print("образ не найден")
    else:
        print("образ не найден")


image = "данные"
lane = "большые метеоданные"
m = len(image)
n = len(lane)
search(image, lane)
