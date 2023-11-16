class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # n : int = 0
        # beginningPointer : int = 0
        # longest : int = 0
        # dct : dict = {}
        # for i in range(len(s)):
        #     if(s[i] in dct.values()):
        #         beginningPointer = beginningPointer + 1 
        #         dct.update({i:s[i]})
        #     else:
        #         n = n + 1
        #         dct.update({i:s[i]})
        #         longest = max(longest, i - beginningPointer +1)
        # return longest
        n = len(s)
        maxLength = 0
        charMap = {}
        left = 0
        
        for right in range(n):
            if s[right] not in charMap or charMap[s[right]] < left:
                charMap[s[right]] = right
                maxLength = max(maxLength, right - left + 1)
            else:
                left = charMap[s[right]] + 1
                charMap[s[right]] = right
        
        return maxLength




solution : Solution = Solution()
# print(solution.lengthOfLongestSubstring("abcabcbb"))#3
# print(solution.lengthOfLongestSubstring("bbbbb"))#1
print(solution.lengthOfLongestSubstring("pwwkew"))#3
print(solution.lengthOfLongestSubstring("dvdf"))#3