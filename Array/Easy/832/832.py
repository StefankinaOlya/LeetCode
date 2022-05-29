class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        answ = []
        answ1 = []
        for i in range(len(image)):
            for j in range(len(image[i][::-1])):
                if image[i][::-1][j] == 0:
                    answ1.append(1)
                else:
                    answ1.append(0)
            answ.append(answ1)
            answ1 = []
        return answ
