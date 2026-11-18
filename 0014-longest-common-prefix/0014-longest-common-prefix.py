class Solution(object):
    def longestCommonPrefix(self, strs):
        length = list(map(lambda x: len(x),strs)) 
        min_len = min(length)
        prefix = ""
        if min_len == 0:
            return prefix
        for i in range(min_len):
            pre = strs[0][i]
            for j in range(len(strs)):
                if pre != strs[j][i]:
                    return prefix
            prefix += pre
        return prefix