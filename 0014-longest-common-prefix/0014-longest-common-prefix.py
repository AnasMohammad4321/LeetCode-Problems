class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if (len(strs) == 1):
            return strs[0]
        
        lcp = strs[0]
        for i in range(len(lcp)):
            for string in strs[1:]:
                if i >= len(string) or string[i] != lcp[i]:
                    return lcp[:i]
        return lcp
                