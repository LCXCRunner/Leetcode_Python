class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        wealth : list = []
        for i in range(len(accounts)):
            wealth.append(sum(accounts[i]))
        return max(wealth)
    
solution : Solution = Solution()
print(solution.maximumWealth([[1,5],[7,3],[3,5]]))