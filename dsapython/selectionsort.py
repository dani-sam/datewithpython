def selectionsort(m, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if m[j] < m[min]:
                min = j
        m[i], m[min] = m[min], m[i]


data = [20, 12, 10, 15, 2]
size = len(data)
selectionsort(data, size)
print("Sort array in ascending order")
print(data)


def fname():
    pass
