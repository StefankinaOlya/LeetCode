class Solution:
    def numberOfSteps(self, num: int) -> int:
        z = 0
        while num >= 1:
            if num % 2 == 0:
                num = num // 2
                z += 1
            else:
                num -= 1
                z += 1
        return z
            
