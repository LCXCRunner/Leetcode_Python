class Solution:
    #takes in two lists of strings and returns the combinations of them
    def combination(self, list1: list[str], list2: list[str]) -> list[str]:
        result = []
        result.append(list1)
        result.append(list2)
        return result
    
    def letterCombinations(self, digits: str) -> list[str]:
        length = len(digits)
        
        #return empty if empty string is passed
        if length == 0:
            return []
        
        #possible numbers are 2-9 inclusive. 1 and 0 do not mapt to anything in old texting method
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
        
        if length == 1:
            return [numMap[digits[0]]]
        
        return Solution.combination((),numMap[digits[0]],numMap[digits[1]])
        
    
        
        
        
        
        
    
#test case
print("Combinations: ")
print(Solution.letterCombinations((), '23'))
print(type(Solution.letterCombinations((), '2')))