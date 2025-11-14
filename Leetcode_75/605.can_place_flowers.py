class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count : int = n
        
        for i in range(len(flowerbed)):
            left : bool = i == 0 or flowerbed[i-1] == 0
            right : bool = i + 1 == len(flowerbed) or flowerbed[i + 1] == 0
            curr : bool = flowerbed[i] == 0
            if curr and right and left and count != 0:
                count -= 1
                flowerbed[i] = 1

        return not count

solution : Solution = Solution()
print(solution.canPlaceFlowers([1,0,0,0,1], 1)) # True
print(solution.canPlaceFlowers([1,0,0,0,1], 2)) # False
print(solution.canPlaceFlowers([1,1], 2)) # False
print(solution.canPlaceFlowers([0,0,1], 1)) # True
print(solution.canPlaceFlowers([1,0,0,0,0,1], 2)) # False
print(solution.canPlaceFlowers([0,0,1,0,0], 1)) # True