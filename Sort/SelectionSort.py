# coding=utf-8
# Time   :2023/2/27
# File   :SelectionSort.py
# author  : AAAHang

a = [9, 7, 4, 2, 3, 1, 6, 8, 5]


def SelectionSort(a):
    for i in range(len(a) - 1):
        index = i
        for j in range(i + 1, len(a)):
            if (a[j] < a[index]):
                index = j
            print(a)
        temp = a[i]
        a[i] = a[index]
        a[index] = temp
    return a


def selectionSort(a):
    for i in range(len(a) - 1):
        min_index = i
        for j in range(i + 1, len(a)):
            if a[min_index] > a[j]:
                min_index = j
        temp = a[min_index]
        a[min_index] = a[i]
        a[i] = temp
    return a


if __name__ == "__main__":
    print(a)
    selectionSort(a)
    print(a)
