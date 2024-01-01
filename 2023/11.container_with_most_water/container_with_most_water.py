class Solution:
    def maxArea(self, height: list[int]) -> int:
        temp : int = 0
        result : int = 0
        leftPointer : int = 0
        rightPointer : int = len(height) - 1

        while(leftPointer < rightPointer):
            temp = self.usableArea(self,height[leftPointer], height[rightPointer], leftPointer, rightPointer)
            result = max(temp, result)

            if(height[leftPointer] < height[rightPointer]):
                leftPointer += 1
            else:
                rightPointer -= 1
        return result
    
    @staticmethod
    def usableArea(self, height1 : int, height2 : int, index1 : int, index2 : int) -> int:
        result : int
        usableWidth : int = 0
        usableHieght : int = 0
        if(height1 > height2 or height1 == height2):
            usableHieght = height2
        else:
            usableHieght = height1
        
        usableWidth = abs(index1 - index2)

        result = usableHieght * usableWidth
        return result
    

solution = Solution()
tester : list = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(tester))