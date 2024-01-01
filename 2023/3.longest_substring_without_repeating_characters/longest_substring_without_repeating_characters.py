class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        counter : int = 0
        left : int = 0
        right : int = 0
        log : dict = {}
        test : str = s[0:len(s)]

        while right < len(s):
            if right < left: 
                right += 1
                continue
            subString : str = s[left:right]
            # counter = max(counter,len(subString))
            if s[right] in subString:
                log[subString] = 1
                left += 1
                counter = max(counter,len(s[left:right]))
                continue
            if subString not in log:
                log[subString] = 1
                right += 1
                counter = max(counter,len(s[left:right]))
            else:
                log[subString] += 1
                right += 1
                counter = max(counter,len(s[left:right]))
                # left += 1
        return counter




solution : Solution = Solution()
print(solution.lengthOfLongestSubstring("abcabcbb"))#3
print(solution.lengthOfLongestSubstring("bbbbb"))#1
print(solution.lengthOfLongestSubstring("pwwkew"))#3
print(solution.lengthOfLongestSubstring("dvdf"))#3