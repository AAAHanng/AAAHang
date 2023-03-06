# coding=utf-8
# Time   :2023/2/27 
# File   :HeapSort.py
# author  : AAAHang
import random

a = [5, 4, 6, 2, 3, 1, 7, 8, 9, 6]


def Heapify(num, start, end):
    father = start
    son = father * 2 + 1
    while son <= end:
        if son + 1 <= end and num[son + 1] > num[son]:
            son += 1
        if num[father] < num[son]:
            num[father], num[son] = num[son], num[father]
            father = son
            son = father * 2 + 1
        else:
            return


def HeapSort(num):
    for i in range(len(num) // 2 - 1, -1, -1):
        Heapify(num, i, len(num) - 1)
    # 初始化堆 init heap
    for i in range(len(num) - 1, 0, -1):
        num[0], num[i] = num[i], num[0]
        # 交换 队首队尾
        Heapify(num, 0, i - 1)
        # 缩小堆尺寸


if __name__ == '__main__':
    a = [5, 4, 6, 2, 3, 1, 7, 8, 9]
    print(a)
    HeapSort(a)
    print(a)

    # b = [random.randint(1, 666) for i in range(666)]
    #
    # print(b)
    # HeapSort(b)
    # print(b)
