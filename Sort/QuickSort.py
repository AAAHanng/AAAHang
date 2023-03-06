# coding=utf-8
# Time   :2023/2/27 
# File   :QuickSort.py
# author  : AAAHang

a = [9, 7, 4, 2, 3, 1, 6, 8, 5]


# a = [3, 2, 1, 9, 6, 5, 4]


def QuickSortOne(a):
    if (len(a)) <= 1:
        return a
    key = a[0]
    llist, rlist, mlist = [], [], [key]
    for i in range(1, len(a)):
        if (a[i]) > key:
            rlist.append(a[i])
        elif (a[i]) == key:
            mlist.append((a[i]))
        else:
            llist.append((a[i]))
    return QuickSortOne(llist) + mlist + QuickSortOne(rlist)
    #     这样也行


def QuickSortTwo(a, left, right):
    if (left >= right): return
    leftp = left
    rightp = right
    key = a[leftp]
    print(a)
    while (leftp < rightp):
        while (leftp < rightp and rightp >= key):
            rightp -= 1
        temp = a[rightp]
        a[rightp] = a[leftp]
        a[leftp] = temp
        while (leftp < rightp and leftp <= key):
            leftp += 1
        temp = a[rightp]
        a[rightp] = a[leftp]
        a[leftp] = temp
    print("---------------")
    QuickSortTwo(a, left, rightp - 1)
    QuickSortTwo(a, leftp + 1, right)


def quickSortdemo1(a, head, tail):
    if head >= tail:
        return a
    index = a[head]
    low = head
    high = tail
    while low != high:

        while low < high and a[high] > index:
            high -= 1
        a[low] = a[high]
        print(a)

        while low < high and a[low] < index:
            low += 1
        a[high] = a[low]
    a[low] = index
    quickSortdemo1(a, head, low - 1)
    quickSortdemo1(a, low + 1, tail)

    return a


def quickSoridemo2(a, left, right):
    if left >= right: return
    index = a[left]
    lp = left
    rp = right

    while lp != rp:
        while lp < rp and index < a[rp]:
            rp -= 1
        a[lp] = a[rp]
        while lp < rp and index > a[lp]:
            lp += 1
        a[rp] = a[lp]
    a[lp] = index
    quickSoridemo2(a, left, lp - 1)
    quickSoridemo2(a, rp + 1, right)
    return a


if __name__ == '__main__':
    print(a)
    quickSoridemo2(a, 0, len(a) - 1)
    print(a)
