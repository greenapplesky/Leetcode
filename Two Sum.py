class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        mydict = {}
        for i in range(len(nums)):
            if nums[i] in mydict:
                return [mydict[nums[i]], i]
            else:
                mydict[target - nums[i]] = i


a = Solution()
ans = a.twoSum([1, 2, 3], 5)
print(ans)
