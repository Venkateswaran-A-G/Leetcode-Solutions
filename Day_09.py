class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s1 = s.strip()
        s1 = s1[::-1]
        count =0
        for i in range(len(s1)):
            if s1[i] == " ":
                break
            else:
                count+=1
        return count