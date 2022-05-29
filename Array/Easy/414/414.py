class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums1 = list(set(nums))
        if len(nums1) < 3:
            return sorted(nums1)[-1:][0]
        return sorted(nums1, reverse=True)[2]
