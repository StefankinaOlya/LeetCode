class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        my_dict = {}
        l = []
        for i in range(len(nums) - 1):
            if i % 2 == 0:
                print(i, nums[i], nums[i+1])
                my_dict[nums[i]] = nums[i + 1]
                l.extend(repeat(nums[i + 1], nums[i]))
        return l
        
