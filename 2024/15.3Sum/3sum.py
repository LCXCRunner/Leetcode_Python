class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result : set = set()
        negative : list = []
        positive : list = []
        zeros : list = []
        
        # split into postives and negatives in O(n)
        for i in nums:
            if i > 0:
                positive.append(i)
            elif i < 0:
                negative.append(i)
            else:
                zeros.append(i)

        # create sets of positive and negative to help with lookup times
        pSet : set = set(positive)
        nSet : set = set(negative)

        # check if there are counter parts in the list if there is at least 1 zero O(n)
        if len(zeros) > 0:
            for i in pSet:
                if -1 * i in nSet:
                    result.add((i * -1, 0, i))
            # check if there are at least 3 zeros       
            if len(zeros) >= 3:
                result.add((0,0,0))

        # check if all pairs of negative numbers could have a positive counter part
        for i in range(len(negative)):
            for j in range(i+1,len(negative)):
                target : int = -1 * (negative[i] + negative[j])
                if target in pSet:
                    result.add(tuple(sorted([negative[i],negative[j],target])))
                
        # check if all paris of positive numbers could have a negative counter part
        for i in range(len(positive)):
            for j in range(i+1,len(positive)):
                target : int = -1 * (positive[i] + positive[j])
                if target in nSet:
                    result.add(tuple(sorted([positive[i],positive[j],target])))

        return result

solution : Solution = Solution()
print(solution.threeSum([-1,0,1,2,-1,-4])) #[[-1,-1,2],[-1,0,1]]
print(solution.threeSum([0,1,1])) # []
print(solution.threeSum([0,0,0])) # [[0,0,0]]
print(solution.threeSum([-1,0,1,0])) # [[-1,0,1]]
print(solution.threeSum([-2,0,1,1,2])) # [[-2,0,2],[-2,1,1]]