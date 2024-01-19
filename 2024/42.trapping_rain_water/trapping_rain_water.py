class Solution:
    def trap(self, height: list[int]) -> int:
        vol : int = 0
        left : int = 0
        right : int = len(height) - 1
        lValue : int = height[0]
        rValue : int = height[len(height) - 1]

        while left < right:
            if lValue < rValue:
                left += 1
                if height[left] < lValue:
                    vol += lValue - height[left]
                else:
                    lValue = height[left]
            else:
                right -= 1
                if height[right] < rValue:
                    vol += rValue - height[right]
                else:
                    rValue = height[right]   
        return vol
            

solution : Solution = Solution()
print(solution.trap([0,1,0,2,1,0,1,3,2,1,2,1]))#6
print(solution.trap([4,2,0,3,2,5]))#9
print(solution.trap([4,2,3]))#1

#works on all but the very worst test cases. To try two pointers as opposed to sliding window
        # vol : int = 0
        # reservior : int = 0
        # left : int = 0
        # right : int = 1
        # copyHeight : list = height.copy()

        # while left < len(copyHeight) - 1:
        #     right = left + 1
        #     while right < len(copyHeight):
        #         if copyHeight[left] <= copyHeight[right]:
        #             left = right
        #             right += 1
        #             vol += reservior
        #             reservior = 0
        #             break
        #         else:
        #             reservior += abs(copyHeight[left] - copyHeight[right])
        #             right += 1
        #         if right == len(copyHeight):
        #             copyHeight[left] = copyHeight[left] - 1
        #             reservior = 0
        # return vol