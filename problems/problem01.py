class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx1, val1 in enumerate(nums):
            for idx2, val2 in enumerate(nums):
                if idx2 > idx1:
                    if val1 + val2 == target:
                        return [idx1, idx2]
