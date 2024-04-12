#(Arrays&Hashing)

# Contains Duplicates (Completed)
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


# Valid Anagram (In Progress)
# Runtime: 31 ms
# Time Complexity: O(1)
# Space Complexity:

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sorted_s = sorted(s)
        sorted_t = sorted(t)

        if sorted_s == sorted_t:
            return True
        else:
            return False