class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        z = original
        for i in nums:
            if z in nums:
                z *= 2
        return z
