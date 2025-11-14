class Solution:
    def compress(self, chars: list[str]) -> int:
        count : int = 0
        s : str = ""
        curr : str = chars[0]

        for i in chars:
            if i == curr:
                count += 1
                continue
            else:
                if count == 1:
                    s = s + curr
                else:
                    s = s + curr + str(count)
            count = 1
            curr = i

        if count == 1:
            s = s + curr
        else:
            s = s + curr + str(count)

        chars[:] = list(s)
        return len(chars)

solution : Solution = Solution()
print(solution.compress(["a","a","b","b","c","c","c"])) # ["a","2","b","2","c","3"]
print(solution.compress(["a"])) # ["a"]
print(solution.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])) # ["a","b","1","2"]