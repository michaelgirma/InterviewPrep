# https://www.youtube.com/watch?v=BgLTDT03QtU

# Big O notation is the way we analyze the time it takes for our algorithm to run as input size grows

# O(1)

# flat line on complexity graph because the time it takes to complete is always the same, most efficent complexity 
# Examples 
nums =[1, 2, 3]
nums.append(4) # push to end
nums.pop(1) # pop from end
nums[0] #look up value

hashMap = {}
hashMap["key"] = 10 # inserting value
print("key" in hashMap) #lookup value
print(hashMap["key"]) #lookup value
hashMap.pop("key") # remove value

# O(logn)
# how many times can we divide an array in half until we get n
# Used for binary search, and binary search on BST

# O(nlogn)
# used for sorting

# as input size grows, time grow porportinally
# O(n) always mean worst case 
# Examples
nums = [1, 2, 3]
sum(nums) # sum of array

for n in nums: #looping
    print(n)

nums.insert(1, 100) #insert middle
nums.remove(100) #remove middle
print(100 in nums) #searching

#O(n^2)

# Examples
nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i][j])

nums = [1, 2, 3]
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        print(nums[i], nums[j])
