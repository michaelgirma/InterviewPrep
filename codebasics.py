# Excercise 1 Solution: Arrays
# Date: 04/29/2024

# A
# Create an array for expense per month
expenses = [2200, 2350, 2600, 2130, 2190]

# 1. In Feb, how many dollars you spent extra compare to January?
print( expenses[1] - expenses[0] ) # result is 150 more dollars, feburary price minus january price

# 2. Find out your total expense in first quarter (first three months) of the year.
print( expenses[0] + expenses[1] + expenses[2]) # adding up the first three values of array, represent first three months

# 3. Find out if you spent exactly 2000 dollars in any month
expenses = [2200, 2350, 2600, 2130, 2190] 
print("Did I spent 2000$ in any month? ", 2000 in expenses)

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.insert(5, 1980) #inserts 1980 at index 5 which is the end of array
print(expenses)

expenses.append(1980) # append puts a value at the end of an array by default, june is the last month in our array
print(expenses)

# 5. You returned an item that you bought in a month of April and
# got a refund of 200$. Make a correction to your monthly expense list
# based on this
expenses[3] = expenses[3] - 200
print(expenses)

# B
heroes=['spider man','thor','hulk','iron man','captain america']

# 1. Length of the list
print(len(heroes))

# 2. Add 'black panther' at the end of this list
heroes.append('black panther')
print(heroes)

# 3. You realize that you need to add 'black panther' after 'hulk',
# so remove it from the list first and then add it after 'hulk'
heroes.remove('black panther')
heroes.insert(3, 'black panther')
print(heroes)

# 4. Now you don't like thor and hulk because they get angry easily :)
# So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
# Do that with one line of code.
heroes[1:3] = ['Doctor Strange']
print(heroes)

# 5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
heroes.sort()
print(heroes)

# C
# Create a list of all odd numbers between 1 and a max number. 
# Max number is something you need to take from a user using input() function

max_num = int(input("Provide a number greater than 1: "))
counter = 0
list = []

while counter < max_num:
    if counter % 2 != 0:
        list.append(counter)
        counter += 1
    else:
        counter += 1
print(list)
# Time Complexity: O(n)

#Better way to do it
max = int(input("Enter max number: "))
odd_numbers = []

for i in range(1, max):
    if i % 2 == 1:
        odd_numbers.append(i)

print("Odd numbers: ", odd_numbers)

