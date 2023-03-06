# Coding  :utf-8
# Time   :2023/3/4 
# File   :LinkStack.py
# Author  : AAAHang

class StackNode:
    def __init__(self):
        self.data = None
        self.next = None


class LinkStack:
    def __init__(self):
        self.top = StackNode()

    def IsEmptyStack(self):
        if self.top.next == None:
            iTop = True
        else:
            iTop = False
        return iTop

    def PushStack(self, da):
        tStackNode = StackNode()
        tStackNode.data = da
        tStackNode.next = self.top.next
        self.top.next = StackNode
        print("Push Stack Element is :", da)

    def PopStack(self):
        if self.IsEmptyStack():
            print("Stack is Empty")
            return
        else:
            tStackNode = self.top.next
            self.top.next = tStackNode.next
            return tStackNode.node

    def GetTopStack(self):
        if self.IsEmptyStack():
            print("Stack is Empty")
            return
        else:
            return self.top.next.data

    def CreateStackByInput(self):
        data = input('place enter Element(place enter enter to end,place enter :')
        while data != "#":
            self.PushStack(data)
            data = input("place enter Element:")


if __name__ == '__main__':
    ls = LinkStack()
    ls.CreateStackByInput()