class MyStack:

    def __init__(self):
        self.queue : list = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        return self.queue.pop()

    def top(self) -> int:
        if not self.empty():
            return self.queue[len(self.queue) - 1]
        return []

    def empty(self) -> bool:
        if len(self.queue) == 0:
            return True
        else:
            return False


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
x=1
obj.push(x)
print(obj.top())
print(obj.pop())
print(obj.top())
print(obj.empty())