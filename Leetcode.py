# Two Sum 
# Runtime: 22ms
# Complexity: O(n^2)

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        output = []
        for yindex, y in enumerate(nums):
            for xindex, x in enumerate(nums[yindex+1:]):
                xindex += yindex + 1
                temp = y + x
                if temp == target:
                    output.append(yindex)
                    output.append(xindex)
                    return output

# Remove Duplicates From Sorted Array
# In Progress, gonna come back to it
                
# Remove Element
# In Progress, gonna come back to it
