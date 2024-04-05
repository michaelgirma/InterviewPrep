#(Arrays&Hashing)

#Contains Duplicates (in progress)
# 41/75 testcases passed
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for x in nums:
            for y in nums[x+1:]:
                if x == y:
                    return True
        return False 