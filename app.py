#Day 1

#Declaring Variables with different Data types
age = 20 #Number
price = 19.95 #Float
first_name = 'Michael' #String
is_online = False #Boolean
print(age, price, first_name, is_online)

#Excercise
patient_name = "John Smith"
patient_age = 20
new_patient = True

#Built In Function: input 
name = input("What is your name? ")
print("Hello " + name)

#Data Type: Int
birth_year = input("Enter your birth year: ")
age = 2020 - int(birth_year)  #built in function that turns any data type to integer
print(age)

#Data Type: Float
19.82 #float datatype because it is a number with a decimal point
float() #built in function that converts any data type to a float

#Data Type: Boolean
True, False # boolean can be either true or false
bool() #built in function that converts any data type to boolean

#Data Type: String
"Michael" # anything with "" surrounding it is a string
str() #built in function that ocnverts any data type to a string

#Excercise 2
first_num = input("Enter first number: ")
second_num = input("Enter second number: ")
solution = float(first_num) + float(second_num)
print("The solution is: " + str(solution))

#Strings

course = "python for beginners"
print(course.upper()) #makes all characters in a string capital
print(course.find("f")) #returns the index of the character
print(course.find("for")) #returns the index of the first character from the string being searched for
print(course.replace("for", "4")) #replaces whatever is before the come with whatever is after the coma
print("python" in course) #boolean statement, returns True

#Arithmetic Operators
print(10 + 3) #addition
print(10 - 3) #subtraction
print(10 * 3) # multiplication
print(10 / 3) #division, gives you float answer
print(10 // 3) #division rounds to the nearest whole number and gives you int answer
print(10 % 3) #gives you remainder of the division between two numbers
print(10 ** 3) #exponent operator, 10 to the power of 3 in this case

x = 10
x += 3 #efficent wax of doing it, called augmented assigned operator, applicabale with -, *, /
print(x)

#Operator Precedence
y = 10 + 3 * 2 
print(y)
#just like in math, coding does operations in a certain order
# PEMDAS: parentheses, exponents, multiplication and division from left to right, and addition and subtraction from left to right.

#Comparison Operators
x = 3 > 2 #boolean expression
print(x) #you can use, < > <= >= == != 

#Logical Operators
price = 25
print(price > 10 and price < 30) # everything has to be true when using and
print(price < 20 or price > 5) # only one condition has to be true when using or
print(not price < 10) # inverses any condition given

#if statements

temp = 35

if temp > 30:
    print("It is a hot day outside!")
    print("Drink plenty of water!")
    temp -= 10
elif temp > 20:
    print("It is a nice day!")
    temp -= 10
elif temp > 10:
    print("It is a bit cold")
else:
    print("It is a cold day!")

#Exercise
weight = float(input("Weight: "))
unit = input("(k)g or (l)bs: ").lower()

if unit == "k":
    weight *= 2.2
    print("Weight in lbs: " + str(weight))
elif unit == "l":
    weight //= 2.2
    print("Weight in kg: " + str(weight))
else:
    print("Please provide k or l for your weight type")

# While loops

i = 1
while i <= 1_000: #underscore makes number more readable
    print(i)
    i += 1

t = 1
while t <= 10:
    print(t * "$") #the string repeats its self as many times as the number it is multiplied by
    # if t is 1, $ prints 1 time, so on and so on
    t += 1  

#Lists
    
#used to represent a list of objects
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
#Indexes start at: 0 till the last item so in this case 4
# You can also go from -1 to the beginning of the list, this would be going through the list backwards

print(names) #prints the list
print(names[0]) #prints the item in the list at index 0
print(names[-1]) #prints the last item on the list

names[0] = "Jon" #changes index 0 values to Jon
print(names)

print(names[0:3]) # will return indexes 0 to 2 excluding 3 but you still have to mention 3 to include 0 through 2, returns a new list does not modify the original

#List Methods

numbers = [1, 2, 3, 4, 5]

numbers.append(6) #adds an item to end of list
print(numbers)

numbers.insert(1, -5) #provide index, then item, insert will insert a value into a specific index
print(numbers)

numbers.remove(3) #gets rid of a specified value
print(numbers)

numbers.clear() #clears everything in a list
print(numbers)

print(1 in numbers) #checks if 1 is in list

print(len(numbers)) #returns the number of elements in a list

# For loops
numbers = [1, 2, 3, 4, 5, 6]

for item in numbers: # a for loop, each iteration item will equal a value from the list, we iterate through the whole list
    print(item)

# Using the range() function
range(5) #an object that can store a sequence of numbers

for num in range(10): # ranges from 0 or specified start point until minus 1 of the end point, in this case 0 to 9
    print(num)

for num in range(5, 10): # ranges from 5 to 9
    print(num)

for num in range(5, 10, 2): #ranges from 5 to 10, counting by 2
    print(num)

#Tuples
#immutable, cannot change once created

numbers = (1, 2, 3, 3)
print(numbers)
print(numbers.count(3)) #returns the count of a value in a tuple 

