class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        answ = []
        list1 = nums[:n]
        list2 = nums[n:]
        for i in range(len(list1)):
            answ.append(list1[i])
            answ.append(list2[i])
        return answ
