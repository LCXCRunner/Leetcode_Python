class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window_set = set()
        
        for i in range(len(nums)):
            # Remove element that is no longer in the window
            if i > k:
                window_set.remove(nums[i - k - 1])
            
            # Check for duplicate in the current window
            if nums[i] in window_set:
                return True
            
            window_set.add(nums[i])
            
        return False

solution : Solution = Solution()
print(solution.containsNearbyDuplicate([1,2,3,1],3)) # True
print(solution.containsNearbyDuplicate([1,0,1,1],1)) # True
print(solution.containsNearbyDuplicate([1,2,3,1,2,3],2)) # False