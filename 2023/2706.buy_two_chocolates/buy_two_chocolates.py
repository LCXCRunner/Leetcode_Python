class Solution:
    def buyChoco(self, prices: list[int], money: int) -> int:
        tempPrices : list[int] = prices
        minimum : int = min(tempPrices)
        tempPrices.remove(minimum)
        nextMin : int = min(tempPrices)
        sum : int = minimum + nextMin
        if sum % money != 0 and sum <= money:
            return money - sum % money
        if sum % money == 0 and sum <= money:
            return 0
        return money
        
solution : Solution = Solution()
print(solution.buyChoco([1,2,2],3))#0
print(solution.buyChoco([3,2,3],3))#3
print(solution.buyChoco([98,54,6,34,66,63,52,39],62))#22