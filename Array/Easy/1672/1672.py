class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_sum = 0
        for i in range(len(accounts)):
            if max_sum < sum(accounts[i]):
                max_sum = sum(accounts[i])
        return max_sum
