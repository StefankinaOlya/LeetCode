class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        result = 1
        for i in range(len(sentences)):
            if result < len(sentences[i].split()):
                result = len(sentences[i].split())
        return result
