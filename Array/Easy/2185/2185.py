class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answ = 0
        for i in range(len(words)):
            if words[i].startswith(pref):
                answ += 1
        return answ
