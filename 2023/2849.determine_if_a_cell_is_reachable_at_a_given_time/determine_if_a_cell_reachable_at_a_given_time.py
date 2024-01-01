class Solution:
    def isReachableAtTime(self, sx : int, sy : int, fx : int, fy : int, t : int) -> bool:
        vertical : int = abs(sy - fy)
        horizontal : int = abs(sx - fx)
        lowerBound : int = 0

        #case of same tile
        if(vertical == 0 and horizontal == 0):
            if(t == 0):
                return True
            if(t >= 2):
                return True
            else:
                return False
        if(t == 0):
            return False

        #case of perfect square
        if(vertical == horizontal and t >= vertical):
            return True
            
        #case of a line
        if(vertical == 0 and t >= horizontal):
            return True
        if(horizontal == 0 and t >= vertical):
            return True
            
        #case of a thick line
        if(vertical == 1 and t >= horizontal):
            return True
        if(horizontal == 1 and t >= vertical):
            return True

        #case of rectangle
        lowerBound = abs(vertical - horizontal) + min(vertical,horizontal)
        if(t>= lowerBound):
            return True
        
        return False

        
    
solution : Solution = Solution()
print(solution.isReachableAtTime(1,1,1,1,3))#true
print(solution.isReachableAtTime(1,2,1,2,1))#false
print(solution.isReachableAtTime(1,2,4,2,1))#false
print(solution.isReachableAtTime(3,1,7,3,3))#false
print(solution.isReachableAtTime(1,1,3,3,9))#true
print(solution.isReachableAtTime(1,3,1,3,0))#true
print(solution.isReachableAtTime(1,3,5,2,2))#false
print(solution.isReachableAtTime(1,1,2,3,2))#true
print(solution.isReachableAtTime(1,1,2,5,6))#true
print(solution.isReachableAtTime(1,4,5,1,5))#true