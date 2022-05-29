class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        index_key = -1
        answ = 0
        if ruleKey == "type":
            index_key = 0
        if ruleKey =="color":
            index_key = 1
        if ruleKey == "name":
            index_key = 2
        for i in range(len(items)):
            if items[i][index_key] == ruleValue:
                answ += 1
        return answ
