class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        z = []
        for i in set(arr):
            z.append(arr.count(i))
        return sorted(list(set(z))) ==  sorted(z)
