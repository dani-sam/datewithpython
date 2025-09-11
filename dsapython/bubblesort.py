def bubblesort(arr):
    s = len(arr)
    print(s)
    for i in range(s):
        for j in range(0, s - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


data = [-2, 11, 0, -9]
r = bubblesort(data)
print(r)
