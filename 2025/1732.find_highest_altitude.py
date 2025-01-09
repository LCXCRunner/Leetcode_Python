class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        sum : int = 0
        max : int = 0
        for i in gain:
            sum += i
            if sum > max:
                max = sum
        return max
        

tester : Solution = Solution()
print(tester.largestAltitude([-5,1,5,0,-7])) # 1
print(tester.largestAltitude([-4,-3,-2,-1,4,3,2])) # 0