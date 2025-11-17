class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res =[]
        index =0
        for i in words:
            if x in i:
                res.append(index)
            index+=1
        return res
