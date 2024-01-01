class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        result : int = 0
        s.sort()
        for i in g:
            if i in s:
                result += 1
                s.remove(i)
            else:
                for j in s:
                    if j > i:
                        result += 1
                        s.remove(j)
                        break
        return result

solution : Solution = Solution()
print(solution.findContentChildren([1,2,3],[1,1]))#1
print(solution.findContentChildren([1,2],[1,2,3]))#2
print(solution.findContentChildren([1,2],[3,3,3]))#2
print(solution.findContentChildren([1,2,3],[4,5,6,1]))#3