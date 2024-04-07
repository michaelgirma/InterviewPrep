# Two Sum 
# Runtime: 22ms
# Complexity: O(n^2)
# Space Complexity: O(1)

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
# Runtime: 59ms
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        for x in nums[1:]:
            if x != nums[k - 1]:
                nums[k] = x 
                k += 1
        return k 
                
# Remove Element
# In Progress, gonna come back to it
