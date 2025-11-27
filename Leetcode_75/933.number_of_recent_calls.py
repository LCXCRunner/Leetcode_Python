from collections import deque

class RecentCounter:

    def __init__(self):
        self.queue : deque = deque()

    def ping(self, t: int) -> int:
        self.queue.append(t)
        while not self.queue[0] >= t - 3000 and len(self.queue) > 0:
            self.queue.popleft()
        return len(self.queue)


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
obj.ping(1)
obj.ping(2)
obj.ping(100)
obj.ping(3001)
obj.ping(3002)
obj.ping(10000)