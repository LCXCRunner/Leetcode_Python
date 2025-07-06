class FindSumPairs:

    def __init__(self, nums1: list[int], nums2: list[int]):
        self.nums1 : list[int] = nums1
        self.nums2 : list[int] = nums2

    def add(self, index: int, val: int) -> None:
        self.nums2[index] += val

    def count(self, tot: int) -> int:
        result : int = 0
        self.nums1.sort()
        self.nums2.sort()

        for i in range(len(self.nums2)):
            for j in range(len(self.nums1) - 1, -1, -1):
                sum : int = self.nums2[i] + self.nums1[j]
                if sum < tot:
                    break # need to move nums2 up
                elif sum > tot:
                    continue
                else:
                    result += 1
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