class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answ = ""
        for i in words:
            if i == i[::-1]:
                answ = i
                break
        return answ
