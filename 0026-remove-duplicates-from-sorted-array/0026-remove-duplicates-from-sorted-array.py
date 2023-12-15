class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        
        j = 0
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i]
                j += 1
        
        nums[j] = nums[len(nums)-1]
        
        return j + 1
