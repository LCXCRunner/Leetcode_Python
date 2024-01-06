import bisect

class Solution:
    def jobScheduling(self, startTime: list[int], endTime: list[int], profit: list[int]) -> int:
        n,ans=len(startTime),0
        state=[]
        for i in range(n):
            state.append([endTime[i],startTime[i],profit[i]])
        state=sorted(state)
        dp=[0 for i in range(n)]
        dp[0]=state[0][2]
        for i in range(1,n):
            prevIndex=bisect.bisect_left(state,[state[i][1]+1])
            if prevIndex==0:
                dp[i]=max(dp[i-1],state[i][2])
            else:
                dp[i]=max(dp[i-1],dp[prevIndex-1]+state[i][2])
            ans=max(ans,dp[i])
        return ans
                


solution : Solution = Solution()
print(solution.jobScheduling([1,2,3,3], [3,4,5,6], [50,10,40,70]))#120
print(solution.jobScheduling([1,2,3,4,6], [3,5,10,6,9], [20,20,100,70,60]))#150
print(solution.jobScheduling([1,1,1], [2,3,4], [5,6,4]))#6