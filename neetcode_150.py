#(Arrays&Hashing)

#Contains Duplicates (Completed)
# Runtime: 455 ms
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_set = set()

        for x in nums:
            if x in num_set:
                return True
            else:
                num_set.add(x)
        return False