class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answ = ""
        res = {}
        for i in range(len(indices)):
            res[indices[i]] = s[i]
        for key in sorted(res):
            answ+= res[key]
        return answ
