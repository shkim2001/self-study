class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        while left <= right:
            mid = (left + right) // 2
            
            if mid ** 2 == num:
                return True
            elif mid **2 < num:
                left = mid + 1
            else:
                right = mid - 1
        return False
    