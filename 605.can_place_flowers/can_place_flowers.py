import math
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        prior : bool = False
        after : bool = False
        current : bool = False
        
        if len(flowerbed) == 1 and n == 1 and flowerbed[0] == 0:
            return True

        for i in range(len(flowerbed)):
            #first and end cases
            if i == 0 or i == len(flowerbed) - 1:
                if i == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                if i == len(flowerbed) - 1 and flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    n -= 1
                    flowerbed[i] = 1
                if n == 0:
                    return True
                continue

            #inner cases
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
                
            if prior and current and after == True:
                n -= 1
                flowerbed[i] = 1
            if n == 0:
                return True
        return False
    
solution : Solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,0,0,1],2))#T
print(solution.canPlaceFlowers([1,0,0,0,1],2))#F
print(solution.canPlaceFlowers([1,0,0,0,0,1],2))#F
print(solution.canPlaceFlowers([0,0],1))#F
print(solution.canPlaceFlowers([0,0,1,0,1],1))#T
print(solution.canPlaceFlowers([1,0,0,0,1,0,0],2))#T
print(solution.canPlaceFlowers([0],1))#T
print(solution.canPlaceFlowers([1,0,0,0],1))#T
print(solution.canPlaceFlowers([0,0],1))#T
print(solution.canPlaceFlowers([0,0,0,0],3))#F
print(solution.canPlaceFlowers([0,0,0],2))#T