class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s:
            subarray = ""
            maxLen = 0
            for l in s:
                if l in subarray:
                    ind = subarray.index(l)
                    subarray = subarray[ind + 1:]
                subarray += l
                maxLen = max(maxLen, len(subarray))
            return maxLen
        return 0