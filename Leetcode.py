# Two Sum 
# Runtime: 2300ms
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
        for x in range(len(nums)):
            for r in range(x+1, len(nums)):
                if nums[x] + nums[r] == target:
                    return [x,r]

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
    
# Problem 392: Is Subsequence
# Runtime: 36ms
# TIme Complexity: O(n)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target = 0
        if s == "":
            return True
        elif t == "":
            return False
        else:
            for x in t:
                if target < len(s):
                    if x == s[target]:
                        target += 1
            if target == len(s):
                return True
            else:
                return False
            
# Problem 242: Is Anagram
# Runtime: 36ms
# Time Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
            if len(s) != len(t):
                return False 
            sDict = {}
            tDict = {}
            for letter in s:
                if letter not in sDict:
                    sDict[letter] = 1
                else:
                    sDict[letter] += 1

            for letter in t:
                if letter not in tDict:
                    tDict[letter] = 1
                else:
                    tDict[letter] += 1

            for key, value in sDict.items():
                if key not in tDict:
                    return False
                if sDict[key] != tDict[key]:
                    return False
            return True
    
# Palindrome Number
# Runtime: 49ms
# Time Complexity: O(n)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        x = str(x)
        l, r = 0, len(x) - 1

        while l < r:
            if x[l] != x[r]:
                return False
            l += 1
            r -= 1
            
        return True

# Top K Frequent Elements
# Runtime: 130ms
# Time Complexity: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        res = []
        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1

        for i in range(k):
            max_value = max(num_map, key=num_map.get)
            res.append(max_value)
            del num_map[max_value]
        
        return res

