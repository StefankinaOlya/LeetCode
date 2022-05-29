class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        ans1 = ""
        prob_list = [0]
        for i in range(len(s)):
            if s[i] == ' ':
                prob_list.append(i + 1)
        for i in range(len(prob_list) - 1):
            ans += s[prob_list[i]:prob_list[i + 1]][::-1]
        
        ans += " " + s[prob_list[len(prob_list) - 1]: len(s)][::-1]
        for i in range(1, len(ans)):
            ans1 += ans[i]
        return ans1
