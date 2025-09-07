class Solution:
    def sumZero(self, n: int) -> list[int]:
        half : int = n // 2
        if n % 2 == 1:
            result = list(range(-half, half + 1))
        else:
            result = list(range(-half, half)) 
            result.remove(0)
            result.append(half)
        return result


solution : Solution = Solution()
print(solution.sumZero(5)) #[-2,-1,0,1,2]
print(solution.sumZero(3)) #[-1,0,1]
print(solution.sumZero(1)) #[0]
print(solution.sumZero(4)) #[-2,-1,1,2]