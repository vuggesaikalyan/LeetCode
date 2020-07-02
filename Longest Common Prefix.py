class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n = len(strs)
        if n == 0:
            return ""

        res = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        limit = min(len(first), len(last))
        for i in range(limit):
            if first[i] == last[i]:
                res += first[i]
            else:
                break
        return res