class Solution:
    #takes in two lists of strings and returns the combinations of them
    def combination(self, list1: list[str], list2: list[str],ans: list[str]) -> list[str]:
        for i in range(len(list1)):
            for j in range(len(list2)):
                ans.append(list1[i]+list2[j])
        return ans
    
    def letterCombinations(self, digits: str) -> list[str]:
        length = len(digits)
        
        #return empty if empty string is passed
        if length == 0:
            return []
        
        #possible numbers are 2-9 inclusive. 1 and 0 do not map to anything in old texting method
        #create map
        numMap = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        #if only 1 letter, no need to compute
        if length == 1:
            return numMap[digits[0]]
        
        #create an array with the first character of the phone number string, pull from map
        lst: list[str] = numMap[digits[0]]
        
        #loop for each number in the string
        for i in range(len(digits) - 1):
            #each loop lst updates and passes itself as well as the next number in the string back until all combos are generated
            lst = Solution.combination((),lst,numMap[digits[i+1]],[])
        
        return lst
    
#test case
print("Combinations: ")
print(Solution.letterCombinations((), '2'))
print(type(Solution.letterCombinations((), '2')))