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
print(solution.canVisitAllRooms([[2],[],[1]]))  # True
print(solution.canVisitAllRooms([[1,3],[1,4],[2,3,4,1],[],[4,3,2]]))  # True
print(solution.canVisitAllRooms([[1],[],[0,3],[1]]))  # False
print(solution.canVisitAllRooms([[],[1,15,18],[16],[2,3,9,11,17,5],[15,19,8,12,14],[10,1,6],[12,9,11],[],[7],[13],[3],[16,2],[4],[18,13],[7,17],[6],[14,4],[5],[8,19],[10]]))  # False
print(solution.canVisitAllRooms([[1],[],[0,3],[1]]))  # False
print(solution.canVisitAllRooms([[1,3],[1,4],[2,3,4,1],[],[4,3,2]]))  # True