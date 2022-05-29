class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        ans = False
        for i in range(len(arr)):
            for j in range(len(arr)):
                if 2 * arr[j] == arr[i] and i != j:
                    print(arr[i], arr[j])
                    ans = True
        return ans
            
