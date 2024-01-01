class Solution:
    def moveZeros(self, nums : list[int]) -> None:
        front : int = 0
        back : int = len(nums) - 1

        while front < back:
            if nums[front] == 0:
                #send it to the back
                self.sendIndexToBackOfArray(nums, front, back)
                back -= 1
            else:
                front += 1

    def sendIndexToBackOfArray(self, array : list, index : int, back : int) -> None:
        #modifys in place
        temp : int = 0
        for i in range(index,back):
            temp = array[i]
            array[i] = array[i+1]
            array[i+1] = temp

solution : Solution = Solution()
tester : list[int] = [0,1,0,3,12]
solution.moveZeros(tester)
print(tester)
