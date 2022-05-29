class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answ = []
        cand_extra = [candies[0]]
        max_cand = candies[0]
        for i in range(len(candies)):
            if candies[i] + extraCandies >= max(candies):
                answ.append(True)
            else:
                answ.append(False)
        return answ
