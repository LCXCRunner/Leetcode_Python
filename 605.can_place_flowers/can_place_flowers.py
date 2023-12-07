import math
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        # if n == 1 and flowerbed.count(1) == 0 and len(flowerbed) == 2:
        #     return True
        prior : bool = False
        after : bool = False
        current : bool = False

        #chop off the outers so you dont go out of index. 
        for i in range(1,len(flowerbed) - 1):
            if flowerbed[i-1] == 0:
                prior = True
            else:
                prior = False
            if flowerbed[i] == 0:
                current = True
            else: 
                current = False
            if flowerbed[i+1] == 0:
                after = True
            else:
                after = False

            if prior and current and after == 0:
                n -= 1
                flowerbed[i] = 1
            if n == 0:
                return True
        return False
        
        # for i in range(len(flowerbed)):
        #     #address each case a flower could be planted
        #     #space must be empty, not be the first space or last, and have empty adjacent spots. decriment n and add in a flower
        #     if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
        #         flowerbed[i] = 1
        #         n -= 1
        #         if n == 0:
        #             return True
        # return False
    
solution : Solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,0,0,1],2))#T
# print(solution.canPlaceFlowers([1,0,0,0,1],2))#F
# print(solution.canPlaceFlowers([1,0,0,0,0,1],2))#F
print(solution.canPlaceFlowers([0,0],1))#F