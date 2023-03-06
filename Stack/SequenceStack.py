# Coding  :utf-8
# Time   :2023/3/4 
# File   :SequenceStack.py
# Author  : AAAHang

class SequenceStack:
    def __init__(self):
        self.MaxStackSize = 10
        self.s = [None for x in range(0, self.MaxStackSize)]
        self.top = -1

    def IsEmptyStack(self):
        if self.top == -1:
            iTop = True
        else:
            iTop = False
        return iTop

    def PushStack(self, x):
        if self.top < self.MaxStackSize - 1:
            self.top = self.top + 1
            self.s[self.top] = x
        else:
            print("stack is Full")
            return

    def PopStack(self):
        if self.IsEmptyStack():
            print("stack is Empty")
        else:
            iTop = self.top
            self.top = self.top - 1
            return self.s[iTop]

    def GetStack(self):
        if self.IsEmptyStack():
            print("stack is Empty")
            return
        else:
            return self.s[self.top]

    def StackTraverse(self):
        if self.IsEmptyStack():
            print("stack is Empty")
        else:
            for i in range(0, self.top + 1):
                print(self.s[i], end=" ")

    def CreateStackByInput(self):
        data = input("enter an Element(To continue ,place enter enter to end,place enter # )")
        while data != "#":
            self.PushStack(data)
            data = input("place enter Element")


if __name__ == '__main__':
    ss = SequenceStack()
    ss.CreateStackByInput()
    print("stack Element is:",end=" ")
    ss.StackTraverse()
