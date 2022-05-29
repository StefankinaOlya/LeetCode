class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        first_union, second_union = "", ""
        for i in word1:
            first_union += i
        for i in word2:
            second_union += i
        return first_union == second_union
