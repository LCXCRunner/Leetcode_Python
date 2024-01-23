class Solution:
    def maxLength(self, arr: list[str]) -> int:
        l=[set()]
        for i in arr:
            if len(set(i)) < len(i):
                continue
            i = set(i)
            for j in l:
                if i.intersection(j):
                    continue
                l.append(i.union(j))
        m = 0
        for i in l:
            if m < len(i):
                m = len(i)
        return m

solution : Solution = Solution()
print(solution.maxLength(["un","iq","ue"]))#4
print(solution.maxLength(["cha","r","act","ers"]))#6
print(solution.maxLength(["abcdefghijklmnopqrstuvwxyz"]))#26
print(solution.maxLength(["aa","bb"]))#0
print(solution.maxLength(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]))#16
print(solution.maxLength(["a", "abc", "d", "de", "def"]))#6