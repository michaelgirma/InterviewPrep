# Two Sum 
# Runtime: 2676ms
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
        for i, x in enumerate(nums):
            for j, y in enumerate(nums[i+1:]):
                j += i + 1
                if x + y == target:
                    output.append(i)
                    output.append(j)
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
# Runtime: 40ms
# Time Complexity: O(n)
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for x in nums:
            if x != val:
                nums[k] = x
                k += 1
        return k


# Problem 66: Plus One
# Runtime: 34ms
# Time Complexity: O(n)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strArr = [str(char) for char in digits]
        string = ''.join(strArr)
        num = int(string)
        total = num + 1
        output = [int(x) for x in str(total)]
        return output

