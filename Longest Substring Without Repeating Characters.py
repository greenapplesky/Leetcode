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
            if(s[ptr2] < 'a' or s[ptr2] > 'z'):
                ptr2 += 1
                continue
            index = ord(s[ptr2])-97
            if(dict[index] is None or dict[index] < ptr1):
                cur += 1
                res = max(cur, res)
            else:
                cur -= dict[index]
                ptr1 = dict[index]+1
            dict[index] = ptr2
            ptr2 += 1
        return res


solution = Solution()
res = solution.lengthOfLongestSubstring(" ")
print(res)
