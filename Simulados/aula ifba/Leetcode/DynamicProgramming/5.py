class Solution(object):
    def longestPalindrome(self, s):
        maxPalydrom = ""
        for i in range(len(s)):
            for j in range(len(s)):
                if i != j:
                    if s[i] == s[j]:
                        substring = s[i:j+1]
                        if substring == substring[::-1]:
                            if len(substring) > len(maxPalydrom):
                                maxPalydrom = substring
        if maxPalydrom == "": return s[0]
        return maxPalydrom