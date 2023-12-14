class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mydict = {}
        for i in range(len(nums)):
            difference = target - nums[i]
            if (difference in mydict):
                return [i, mydict[difference]]
            mydict[nums[i]] = i