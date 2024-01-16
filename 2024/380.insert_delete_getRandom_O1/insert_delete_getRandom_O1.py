import random
class RandomizedSet:
    def __init__(self):
        self.randomSet : set = set()
        self.randomList : list = []

    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        else:
            self.randomSet.add(val)
            self.randomList.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val in self.randomSet:
            self.randomSet.remove(val)
            self.randomList.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        #had to use a list because random.choice will not iterate over a set. 
        return random.choice(self.randomList)


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
print(obj.insert(1))#T
print(obj.insert(1))#F
print(obj.insert(2))#T 1,2
print(obj.remove(3))#F
print(obj.remove(2))#T 1
print(obj.insert(2))#T 1,2
print(obj.insert(3))#T 1,2,3
for i in range(10):
    print(obj.getRandom())
