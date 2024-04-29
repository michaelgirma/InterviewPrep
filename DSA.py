# Video Link: https://www.youtube.com/watch?v=8hly31xKli0

# Introduction To Algorithms
# CS defintion: A set of steps a program takes to finish a task.

#Alogrithmic Thinking
# 1. choose steps for a problem
# 2. Pick most efficent Alogrithm to use
# 3. Clearly define what the problem set is and clarify what values count as input

# Choosing Algorithm Process
# 1. find the clear problem statement, understanding what the input is and what the output looks like once the algorithm does its job
# 2. must have a set of instructions in a specific order
# 3. each step needs to be a distinct one
# 4. need to produce a result
# 5. should complete and not take an infinite amount of time

# Efficency
# 1. Measured by time complexity and space complexity
# 2. Time Complexity: How long it takes to complete a job
# 3. Space Complexity: Amount of space taken up in the memory of a computer

# Big O
# 1. a notation used to describe a complexity, measures complexity as input size grows, measures how alogrithm performs in worst case scenario(Upper bounds)
# 2. can only compare complexity among algorithms that solve the same problem
# 3. O(1) --> Constant Time 
# 4. O(log n) --> Logarithmic Time, Sometimes called Sublinear
# 5. O(n) --> Linear Time
# 6. O(n^2) --> Quadratic Time
# 7. O(n^3) --> Cubic Time
# 8. Quasilinear Runtime --> O(n log n)
# 9. Polynomial run times are algorithms that use worst case Quadratic or lower runtime, these are considered efficent and used in the real world
# 10. Exponential run times are algorithms with complexity higher than O(n^2), these are not considered efficent and not used in the real world


# Search Algorithms

# 1. Linear Search/ Sequential Search
# Time Complexity: O(n)
# look for your target value sequentially until you get it
# input is a series of values, output is a value matching the one we are looking for

# 2. Binary Search
# Time Complexity: O(log n)
# start in middle of range of values, check middle value to tagert then cut lower half or higher half, then goes in the middle of that new range and repeats the same process
# returns index of target value in the list
# input should be sorted because you can accidently cut of your target


# Video link: https://www.youtube.com/watch?v=RcZsTI5h0kg
#Hashmaps in Python

# stores data in key:value pairs

# What makes them useful?
# 1. Custom Keys are easier for software engineers to work with
# 2. Haspmaps allow for search in O(1), whereas arrays/linked lists are O(n)

#Hash Functions
# 1. Turns an array into a Hashmap
# 2. Assign the value of a key to an index from an array

# Efficency Compared to Array
# 1. Array has to iterating through every index to search
# 2. Hashmaps just need key and has function takes the key and outputs the index pf the value you are looking for

# Syntax
city_map = {} # empty hashmap

cities = ["Calgary", "Vancouver", "Toronto"] #array of cities in Canada
city_map["Canada"] = [] # creates the key Canada and makes its value an empty array
city_map["Canada"] += cities # appends the cities to the key Canada 

# a way to create a hashmap so that you do not have to manually declare the value type for every key you make, like line 71
# called defaultdict

from collections import defaultdict
state_map = defaultdict(list) #creates a hashmap, every new key is automatically paired with an empty array/list
states = ["Marland", "New York", "Denver"]
state_map["America"] += states
print(state_map)

# Retrieving Data from Hashmaps, 3 methods
city_map = {}
print(city_map)

cities = ["Calgary", "Vancouver", "Toronto"] 
city_map["Canada"] = [] 
city_map["Canada"] += cities 

states = ["Marland", "New York", "Denver"]
city_map["America"] = []
city_map["America"] += states

cities_1 = ["London", "Manchester"]
city_map["England"] = []
city_map["England"] += cities_1

country_list = city_map.keys() #returns all keys from hashmap in the form of a list
print(country_list)
city_list = city_map.values() # returning all values of hashmap in the form of a list
print(city_list)
city_country_pairs = city_map.items() # returns all key value pairs as tuples
print(city_country_pairs)

# Video Link: https://www.youtube.com/watch?v=t9j8lCUGZXo
# Data Structure: Set
# Time Complexity
# 1. Insertion, Deletion, Lookup: O(1)
# Space Complexity
# 1. O(n)
numbers = [1, 1, 1, 2, 2, 3, 5 ,6, 5, 10, 8] # array of numbers
uniques_set = set(numbers) # create set Data structure
print(uniques_set) # prints set, puts numbers in increasing order and removes duplicates

my_set = set()
for nums in numbers:
    my_set.add(nums)
print(my_set)



