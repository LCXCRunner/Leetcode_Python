class MyQueue:
    def __init__(self):
        self.mainStack : list = []

    def push(self, x: int) -> None:
        self.mainStack.append(x)

    def pop(self) -> int:
        return self.mainStack.pop(0)

    def peek(self) -> int:
        return self.mainStack[0]

    def empty(self) -> bool:
        if len(self.mainStack) == 0:
            return True
        else:
            return False
        
    def printElements(self) -> None:
        print(self.mainStack)

tester : MyQueue = MyQueue()
tester.printElements()
tester.push(1)
tester.printElements()
tester.push(2)
tester.printElements()
print(tester.peek())
print(tester.pop())
tester.printElements()
print(tester.empty())