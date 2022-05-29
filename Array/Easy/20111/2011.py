class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        z = 0
        for i in range(len(operations)):
            if operations[i].find("--") != -1:
                z -= 1
            else:
                z += 1
        return z
