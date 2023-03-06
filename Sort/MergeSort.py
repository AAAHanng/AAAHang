# coding=utf-8
# Time   :2023/2/27 
# File   :MergeSort.py
# author  : AAAHang
a = [5, 4, 2, 3, 1, 7, 8, 9]


def MergeSort(a):
    n = len(a)
    if n <= 1:
        return a
    index = n // 2
    left_List = MergeSort(a[:index])
    right_List = MergeSort(a[index:])

    left_index = 0
    right_index = 0
    res = []
    while left_index < len(left_List) and right_index < len(right_List):
        if (left_List[left_index] < right_List[right_index]):
            res.append(left_List[left_index])
            left_index += 1
        else:
            res.append(right_List[right_index])
            right_index += 1
    res += left_List[left_index:]
    res += right_List[right_index:]
    return res


def mergeSort(a):
    n = len(a)
    if (n <= 1): return a
    index = n // 2
    left_List = mergeSort(a[:index])
    right_List = mergeSort(a[index:])
    left_index = 0
    right_index = 0
    res = []

    while left_index < len(left_List) and right_index < len(right_List):
        if left_List[left_index] < right_List[right_index]:
            res.append(left_List[left_index])
            left_index += 1
        else:
            res.append(right_List[right_index])
            right_index += 1

    res += left_List[left_index:]
    res += right_List[right_index:]
    return res


if __name__ == '__main__':
    print(a)
    print(mergeSort(a))
