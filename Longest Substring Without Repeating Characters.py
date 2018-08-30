class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ptr1 = ptr2 = 0
        res = cur = 0
        dict = {}
        while(ptr2 < len(s)):
            if(s[ptr2] not in dict or dict[s[ptr2]] < ptr1):
                cur += 1
                res = max(cur, res)
            else:
                cur = ptr2 - dict[s[ptr2]]
                ptr1 = dict[s[ptr2]]+1
            dict[s[ptr2]] = ptr2
            ptr2 += 1
        return res


solution = Solution()
res = solution.lengthOfLongestSubstring("bbtablud")
print(res)
