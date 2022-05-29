class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        proz_max = []
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    proz_max.append( (nums[i]-1)*(nums[j]-1)) 
        return max(proz_max)
