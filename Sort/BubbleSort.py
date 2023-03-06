# coding=utf-8
# Time   :2023/2/27
# File   :BubbleSort.py
# author  : AAAHang
import time

a = [3, 7, 4, 2, 9, 1, 6, 8, 5]


def BubbleSort(a):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a


def bubbleSort(a):
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
    return a


if __name__ == '__main__':
    print(a)
    start = time.time()
    bubbleSort(a)
    end = time.time()
    print(a)
