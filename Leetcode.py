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

# Group Anagram
# Runtime: 85ms
# Time Complexity: O(n^2)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for word in strs:
            count = [0] * 26

            for c in word:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(word)
        
        return res.values()
    
#Contains Duplicate
# Runtime: 476ms
# Time Complexity: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for x in nums:
            if x in seen:
                return True
            seen.add(x)
        return False

# Find the index of the first occurance
# Runtime: 23ms
# Time Complexity: O(n)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_length = len(needle)
        haystack_length = len(haystack)

        for hay_index in range(haystack_length - needle_length + 1):
            if haystack[hay_index:hay_index + needle_length] == needle:
                return hay_index

        return -1

# Two Sum Array ll
# Runtime: 104ms
# Time Complexity: O(n)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            total = numbers[l] + numbers[r]
                
            if total > target:
                r -= 1
            elif total < target:
                l += 1
            else:
                return [l + 1, r + 1] 

# Permutation in String
# Runtime: 1164 ms
# Time Compleixty: O(n)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_tracker_s1 = {}

        for c in s1:
            char_tracker_s1[c] = 1 + char_tracker_s1.get(c, 0)

        for i in range(len(s2) - len(s1) + 1):
            sub_list = s2[i:i + len(s1)]
            character_count = Counter(sub_list)

            if character_count == char_tracker_s1:
                return True

        return False

# Container with most water
# Runtime: 540 ms
# Time Compleixty: O(n)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_area = 0

        while l < r:
            width = r - l
            curr_height = min(height[l], height[r])
            curr_area = width * curr_height
            max_area = max(max_area, curr_area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
    
# Permutation in string
# Runtime: 1164 ms
# Time Complexity: O(n)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = {}
        for char in s1:
            s1_dict[char] = 1 + s1_dict.get(char, 0)

        for string in range(len(s2) - len(s1) + 1):
            temp = s2[string: string + len(s1)]
            
            if s1_dict == Counter(temp):
                return True
        
        return False