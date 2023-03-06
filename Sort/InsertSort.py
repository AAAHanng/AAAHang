# coding=utf-8
# Time   :2023/2/27
# File   :InsertSort.py
# author  : AAAHang


# a = [9, 7, 4, 2, 3, 1, 6, 8, 5]
a = [9, 4, 7, 2, 3, 1, 6, 8, 5]


def InsertSort(a):
    for i in range(1, len(a)):
        for j in range(i + 1):
            if (a[j] > a[i]):
                print(a)
                print(i, j)
                print("----------------")
                ins = a[i]
                a.pop(i)
                a.insert(j, ins)
    return a


def insertSort(a):
    for i in range(1, len(a)):
        for j in range(i + 1):
            if (a[j] > a[i]):
                ins = a[i]
                a.pop(i)
                a.insert(j, ins)
    return a


if __name__ == "__main__":
    print(a)
    insertSort(a)
    print(a)
