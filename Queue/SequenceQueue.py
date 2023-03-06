# Coding  :utf-8
# Time   :2023/3/4 
# File   :SequenceQueue.py
# Author  : AAAHang
class SequenceQueue:
    def __init__(self):
        self.MaxQueueSize = 10
        self.s = [None for x in range(0, self.MaxQueueSize)]
        self.front = 0
        self.rear = 0

    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    def EnQueue(self, x):
        if (self.rear < self.MaxQueueSize - 1):
            self.rear = self.rear + 1
            self.s[self.rear] = x
            print("Queue Element is: ", x)
        else:
            print("Queue is Full")
            return

    def DeQueue(self):
        if self.IsEmptyQueue():
            print("Queue is Empty")
            return
        else:
            self.front = self.front + 1
            return self.s[self.front]

    def GetHead(self):
        if self.IsEmptyQueue():
            print("Queue is Empty")
            return
        else:
            return self.s[self.front + 1]

    def CreateQueueByInput(self):
        data = input("place enter Element(place enter enter to end ,place enter '#':")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素")


if __name__ == '__main__':
    sq = SequenceQueue()
    sq.CreateQueueByInput()
