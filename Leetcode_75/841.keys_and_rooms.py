from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        # keep track of what keys you have. You start with index 0     
        keyRing : set = set()
        stack : deque = deque([0])
        
        while len(stack) > 0:
            # use a key
            key : int = stack.pop()
            keyRing.add(key)

            # add the new keys that you find
            for newKeys in rooms[key]:
                if newKeys not in keyRing and len(rooms[key]) > 0:
                    stack.append(newKeys)
                    
        # if you successfully got all the keys
        if len(keyRing) == len(rooms):
            return True
        return False
            


solution : Solution = Solution()

print(solution.canVisitAllRooms([[1],[2],[3],[]])) # True
print(solution.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) # False