# Coding  :utf-8
# Time   :2023/3/4 
# File   :LinkQueue.py
# Author  : AAAHang

class QueueNode():
    def __init__(self):
        self.data = None
        self.next = None


class LinkQueue():
    def __init__(self):
        tQueueNode = QueueNode()
        self.front = tQueueNode
        self.rear = tQueueNode

    def IsEmptyQueue(self):
        if self.front == self.rear:
            iQueue = True
        else:
            iQueue = False
        return iQueue

    def EnQueue(self, da):
        tQueueNode = QueueNode()
        tQueueNode.data = da
        self.rear.next = tQueueNode
        self.rear = tQueueNode
        print("Enter Queue Element is :", da)

    def DeQueue(self):
        if self.IsEmptyQueue():
            print("Queue is Empty")
            return
        else:
            tQueueNode = self.front.next
            self.front.next = tQueueNode.next
            if self.rear == tQueueNode:
                self.rear = self.front
            return tQueueNode.data

    def GetHead(self):
        if self.IsEmptyQueue():
            print("Queue is Empty")
            return
        else:
            return self.front.next.data

    def CreateQueueByInput(self):
        data = input("place enter Element(place enter enter to end ,place enter '#':")
        while data != '#':
            self.EnQueue(data)
            data = input("请输入元素")


if __name__ == '__main__':
    lq = LinkQueue()
    lq.CreateQueueByInput()