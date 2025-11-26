class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack : list[int] = []
        next_greater : dict[int, int] = {}
        result : list[int] = []

        for num in nums2:
            if len(stack) == 0:
                stack.append(num)
                continue
            while len(stack) > 0 and stack[len(stack) - 1] < num:
                next_greater.update({stack.pop() : num})
            stack.append(num)
        while len(stack) > 0:
            next_greater.update({stack.pop() : -1})
        for i in nums1:
            result.append(next_greater.get(i))
        return result
            
solution : Solution = Solution()
print(solution.nextGreaterElement([4,1,2], [1,3,4,2])) # [-1,3,-1]
print(solution.nextGreaterElement([2,4], [1,2,3,4])) # [3,-1]
print(solution.nextGreaterElement([1,3,5,2,4], [5,4,3,2,1])) # [-1,-1,-1,-1,-1]
print(solution.nextGreaterElement([1,3,5,2,4], [6,5,4,3,2,1,7])) # [7,7,7,7,7]