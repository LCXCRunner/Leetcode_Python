from collections import Counter

class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 : list[int] = nums1
        self.nums2 : list[int] = nums2
        self.nums2Count : Counter = Counter(self.nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2Count[self.nums2[index]] -= 1 # decriment count of changed number
        self.nums2[index] += val
        self.nums2Count[self.nums2[index]] += 1 # add new one if needed or update currnet

    def count(self, tot: int) -> int:
        # Count frequency of each number in nums1, Counter follows hash map complexity
        self.nums1Counter = Counter(self.nums1)
        result = 0
        
        for num1 in self.nums1:
            target = tot - num1  
            # Add the count of how many times target appears in nums1
            result += self.nums2Count[target]
        
        return result
    
solution : FindSumPairs = FindSumPairs([1,1,2,2,2,3], [1,4,5,2,5,4])
print(solution.count(7)) #8
    
    # notes:
    # 1 <= nums1.length <= 1000
    # 1 <= nums2.length <= 10^5
    # 1 <= nums1[i] <= 10^9
    # 1 <= nums2[i] <= 10^5
    # 0 <= index < nums2.length
    # 1 <= val <= 10^5
    # 1 <= tot <= 10^9
    # At most 1000 calls are made to add and count each.

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)