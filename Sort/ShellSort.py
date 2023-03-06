# coding=utf-8
# Time   :2023/2/27 
# File   :ShellSort.py
# author  : AAAHang

import random


def ShellSort(a):
    gap = len(a) // 2
    while gap >= 1:
        for i in range(gap, len(a)):
            while i > 0:
                if a[i] < a[i - gap]:
                    temp = a[i]
                    a[i] = a[i - gap]
                    a[i - gap] = temp
                    i -= gap
                else:
                    break
        gap //= 2
    return a


def shellSort(a):
    gap = len(a) // 2
    while gap > 0:
        for i in range(gap, len(a)):
            while i > 0:
                if a[i - gap] > a[i]:
                    temp = a[i - gap]
                    a[i - gap] = a[i]
                    a[i] = temp
                    i -= gap
                else:
                    break
        gap //= 2


if __name__ == '__main__':
    b = [random.randint(1, 15) for i in range(15)]
    print(b)
    shellSort(b)
    print(b)
