class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        answer : list[int] = []
        localMax : int = temperatures[0]
        counter : int = 0
        for i in range(len(temperatures)):
            localMax = temperatures[i]
            counter = 0
            for j in range(i+1, len(temperatures)):
                counter += 1
                if temperatures[j] > temperatures[i]: 
                    answer.append(counter)
                    break
                if j == len(temperatures) - 1:
                    answer.append(0)
            if i == len(temperatures) - 1:
                answer.append(0)
        return answer

solution : Solution = Solution()
print(solution.dailyTemperatures([73,74,75,71,69,72,76,73]))#[1,1,4,2,1,1,0,0]
print(solution.dailyTemperatures([30,40,50,60]))#[1,1,1,0]
print(solution.dailyTemperatures([30,60,90]))#[1,1,0]