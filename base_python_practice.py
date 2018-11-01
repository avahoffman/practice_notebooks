#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 07:53:00 2018

@author: whitneyreiner
"""

##############################################################################
##############################################################################
##############################################################################
##################################List basics#################################
##############################################################################
##############################################################################
##############################################################################

# make a list
myList = [1,2,3,4]

# make the list 3 times as big by repeating it three times
A = [myList]*3
print(A)

# replace the second indexed item with 45
myList[2]=45
print(A)

# lists can have different types of data
myList = [1024, 3, True, 6.5]
# adding (appending) a boolean term to the list
myList.append(False)
print(myList)

# insert 4.5 two times into this list
# list.insert(how many times you want to insert it, what do youw ant to insert?)
myList.insert(2,4.5)
print(myList)

# The pop() method removes and returns the element at the given index 
# (passed as an argument) from the list. If no index is given, it will return 
# the last element
print(myList.pop())
print(myList)
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)

# sort, ascending by default
myList.sort()
print(myList)

# reverse the list!
myList.reverse()
print(myList)

# How many times is X in my list?
print(myList.count(6.5))

# At what spot is this thing in my list?
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)


# How to build a list
mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

# prints out 1,2,3
for x in mylist:
    print(x)
    
# =============================================================================
# ##############################################################################
# ##############################################################################
# ##############################################################################
# ###############################String formatting##############################
# ##############################################################################
# ##############################################################################
# ##############################################################################
# =============================================================================
# This prints out "Hello, John!"
name = "John"
print("Hello, %s!" % name)

# Two or more arg specifiers require a tuple (parentheses)
# This prints out "John is 23 years old."
name = "John"
age = 23
print("%s is %d years old." % (name, age))

# You can do this with non-strings too
# This prints out: A list: [1, 2, 3]
mylist = [1,2,3]
print("A list: %s" % mylist)

# =============================================================================
# # %s - String (or any object with a string representation, like numbers)
# 
# # %d - Integers
# 
# # %f - Floating point numbers
# 
# # %.<number of digits>f - Floating point numbers with a fixed amount of digits
# # to the right of the dot.
# 
# # %x/%X - Integers in hex representation (lowercase/uppercase)
# # You will need to write a format string which prints out the data using the 
# =============================================================================

# following syntax: Hello John Doe. Your current balance is $53.44.
data = ("John", "Doe", 53.44)
format_string = "Hello %s %s. Your current balance is $%s."

print(format_string % data)
# 
# 
# 
######WHY ISN'T the last %s %f?#######
# 
# 
# 

# make a string, prints length of string incl. the spaces
astring = "Hello world!"
print("single quotes are ' '")

print(len(astring))

# print position of a letter or something within a string
astring = "Hello world!"
print(astring.index("o"))

# count number of l in string
astring = "Hello world!"
print(astring.count("l"))

# pring slice of string
astring = "Hello world!"
print(astring[3:7])

# =============================================================================
# # If you just have one number in the brackets, it will give you the single 
# # character at that index. If you leave out the first number but keep the colon,
# # it will give you a slice from the start to the number you left in. If you 
# # leave out the second number, if will give you a slice from the first number
# # to the end.
# 
# # You can even put negative numbers inside the brackets.
# # They are an easy way of starting at the end of the string instead of the
# # beginning. This way, -3 means "3rd character from the end".
# 
# =============================================================================
# This is extended slice syntax. The general form is [start:stop:step].
# This prints the characters of string from 3 to 7 skipping one character.
astring = "Hello world!"
print(astring[3:7:2])

# pring reverse of string
astring = "Hello world!"
print(astring[::-1])

# lower or all upper case
astring = "Hello world!"
print(astring.upper())
print(astring.lower())

# determine whether the string starts with something or ends with something.
astring = "Hello world!"
print(astring.startswith("Hello"))
print(astring.endswith("asdfasdfasdf"))

# splits the string into a bunch of strings grouped together in a list.
# This example splits at a space.
astring = "Hello world!"
afewwords = astring.split(" ")
afewwords
# Boolean operators
name = "John"
age = 23
if name == "John" and age == 23:
    print("Your name is John, and you are also 23 years old.")

if name == "John" or name == "Rick":
    print("Your name is either John or Rick.")
    
# The "in" operator could be used to check if a specified object exists within 
# an iterable object container, such as a list:



# interactivepython.org 
# using a dict (unordered)
    capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
print(capitals['Iowa'])
capitals['Utah']='SaltLakeCity'
print(capitals)
capitals['California']='Sacramento'
print(len(capitals))
for k in capitals:
   print(capitals[k]," is the capital of ", k)

phoneext={'david':1410,'brad':1137}
phoneext

phoneext.keys()

list(phoneext.keys())

phoneext.values()

list(phoneext.values())

phoneext.items()

list(phoneext.items())

phoneext.get("kent")
phoneext.get("kent","NO ENTRY")


# =============================================================================
# # user input
# # Python’s input function takes a single parameter that is a string.
# # This string is often called the prompt because it contains some helpful text
# # prompting the user to enter something. For example, you might call input as
# # follows:
# 
# =============================================================================
aName = input("Please enter your name ")
print("Your name in all capitals is",aName.upper(),
      "and has length", len(aName))

# the value returned from the input function will be a string representing the
# exact characters that were entered after the prompt.
# If you want this string interpreted as another type, you must provide the
# type conversion explicitly.

sradius = input("Please enter the radius of the circle ")
radius = float(sradius)
diameter = 2 * radius


# string formatting
print("Hello")

print("Hello","World")

print("Hello","World", sep="***")

print("Hello","World", end="***")


# formatted strings
# not good because you would have to reassign is and years old every time
print(aName, "is", age, "years old.")

# now it will change depending on aName and age
print("%s is %d years old." % (aName, age))

# =============================================================================
# # % operator is a string operator called the format operator.
# # The number of values in the collection on the right side corresponds with the
# # number of % characters in the format string. Values are taken—in order, left
# # to right—from the collection and inserted into the format string.
# 
# # The format string may contain one or more conversion specifications.
# # A conversion character tells the format operator what type of value is going
# # to be inserted into that position in the string. In the example above,
# # the %s specifies a string, while the %d specifies an integer.
# 
# =============================================================================

#####################
# =============================================================================
#The right side of the format operator is a collection of values that will be 
#inserted into the format string. The collection will be either a tuple or a 
#dictionary. If the collection is a tuple, the values are inserted in order of
# position. That is, the first element in the tuple corresponds to the first
# format character in the format string. If the collection is a dictionary, the
# values are inserted according to their keys. In this case all format
# characters must use the (name) modifier to specify the name of the key.
# =============================================================================


# =============================================================================
#  price = 24
#  item = "banana"
#  print("The %s costs %d cents"%(item,price))
# The banana costs 24 cents
#  print("The %+10s costs %5.2f cents"%(item,price))
# The     banana costs 24.00 cents
#  print("The %+10s costs %10.2f cents"%(item,price))
# The     banana costs      24.00 cents
#  itemdict = {"item":"banana","cost":24}
#  print("The %(item)s costs %(cost)7.1f cents"%itemdict)
# The banana costs    24.0 cents
# =============================================================================

# while statement repeats a body of code as long as a condition is true.
counter = 1
while counter <= 5:
    print("Hello, world")
    counter = counter + 1

# =============================================================================
# The for statement can be used to iterate over the members of a collection,
#  so long as the collection is a sequence.
# =============================================================================
for item in [1,3,6,2,5]:
    print(item)

#iterate over a range of values
for item in range(5):
    print((item**2))



# Processing Each Character in a List of Strings
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        letterlist.append(aletter)
print(letterlist)


# selection constructs
score=[]
if score >= 90:
   print('A')
else:
   if score >=80:
      print('B')
   else:
      if score >= 70:
         print('C')
      else:
         if score >= 60:
            print('D')
         else:
            print('F')

# alternative syntax for this type of nested selection uses the elif keyword
if score >= 90:
   print('A')
elif score >=80:
   print('B')
elif score >= 70:
   print('C')
elif score >= 60:
   print('D')
else:
   print('F')

# =============================================================================
# Python also has a single way selection construct, the if statement.
#  With this statement, if the condition is true, an action is performed.
#  In the case where the condition is false, processing simply continues on to
#  the next statement after the if. For example, the following fragment will
#  first check to see if the value of a variable n is negative. If it is, then
#  it is modified by the absolute value function. Regardless, the next action is
#  to compute the square root.
# 
# =============================================================================

if n<0:
   n = abs(n)
print(math.sqrt(n))



# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']
# the answer is: ['c', 'a', 't', 'd', 'o', 'g', 'r', 'b', 'i']

            
wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        if aletter in letterlist:
            pass
        else:
            letterlist.append(aletter)
#before append make sure is not already in list
# or remove duplicates before print or 
print(letterlist)


wordlist = ['cat','dog','rabbit']
letterlist = [ ]
for aword in wordlist:
    for aletter in aword:
        if aletter not in letterlist:
            letterlist.append(aletter)
#before append make sure is not already in list
# or remove duplicates before print or 
print(letterlist)

# list comprehension
#you could do this:
sqlist=[]
for x in range(1,11):
    sqlist.append(x*x)
sqlist
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# =============================================================================
# #But using a list comprehension, we can do this in one step:
# =============================================================================
sqlist=[x*x for x in range(1,11)]
sqlist
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# =============================================================================
# The general syntax for a list comprehension also allows a selection criteria 
# to be added so that only certain items get added.
# =============================================================================

sqlist=[x*x for x in range(1,11) if x%2 != 0]
sqlist
#[1, 9, 25, 49, 81]

[ch.upper() for ch in 'comprehension' if ch not in 'aeiou']
#['C', 'M', 'P', 'R', 'H', 'N', 'S', 'N']

# space separated integers
# if you're doing it with an array, easy way is print(*array)

wordlist=['cat','dog', 'rabbit']
#both methods will print each character
print([word for word in "" .join(wordlist)])
print([word[i] for word in wordlist for i in range(len(word))])

#takes out duplicates because you made it a set
print(set([word[i] for word in wordlist for i in range(len(word))]))




# THESE DO THE SAME THING

def sumOfN(n):
   theSum = 0
   for i in range(1,n+1):
       theSum = theSum + i

   return theSum

print(sumOfN(10))

def foo(tom):
    fred = 0
    for bill in range(1,tom+1):
       barney = bill
       fred = fred + barney

    return fred

print(foo(10))

#hackerrank

def gradingStudents(grades):
    n= int(input().strip())
    for a0 in range(n):
        x=int(input().strip()) #greater than failing grade = no rounding
    if x>=38:
#if diff between grade and next multiple of 5 is less than 3 round up           to the next multiple of 5. % is modulus, not divide- it returns the            remainder
        if x % 5 > 2:
#while the grade is not divisible by 5 add 1 until the grade is                 divisible by 5
            while x % 5 !=0: x +=1
        print(x)
        
        
        
print(*range(1, int(input())+1), sep='')
        
def fun(*args):
    total = 0
    for i in args:
        total += i
    return total

print(fun())
print(fun(1))
print(fun(1, 2, 3))

# * means "everything in this set"


For short operator '*' allows you to pass an array. Example:
name="steve"
password="qwerty"
captcha="h3g2"
user = [name, password, captcha]

def login(n,p,c):
    print(n+p+c)

login(*user)


# =============================================================================
# In general, you pass in arguments like so:
# 
# function(arg1,arg2,arg3)
# But, if you put them in a list such as:
# 
# function([arg1,arg2,arg3])
# then it's like you're only passing in 1 argument (the list) and you'll get an error saying function was expecting 3 arguments and only got 1.
# 
# On the other hand if you were to include * it would "unpack" the list (imagine the list is a suitcase and the elements are pieces of clothing you want to put on the bed to look at individually. you can't do that without unpacking the suitcase, right?) so that it would still work:
# 
# function(*[arg1,arg2,arg3])
# becomes
# 
# function(arg1,arg2,arg3)
# So *user changes from a list:
# 
# user = [name, password, captcha]
# =============================================================================
# =============================================================================
# to arguments:
# 
# *user = name, password, captcha
# So now log_in will work without errors because it was passed 3 arguments instead of 1!
# 
# n = int(input()) *range (1, n+1) = range is from 1 to n, exclusive of n. 
# so if your input is 3 then it prints 1 2. So input to the range function is 1 to n+1
# 
# if you don't give sep='' in print statement then each value is seperated by a space
# 
# * Explanation
# Python's Print Function defines the input as *objects, not as iterable like it does for Map.
# 
# An example of an iterable is a list because we can keep stepping through the elements one at a time.
# 
# print instead needs multiple arguments for each object you want to print. 
# =============================================================================
# * is a way to "unpack" a list so that it becomes arguments instead of a list. f(*[1,2,3]) converts to f(1,2,3).
# # 
# =============================================================================
# Example using print (from future in py2):
# 
# print([1,2,3])
# #[1, 2, 3]
# 
# print(*[1,2,3])
# #1 2 3
# 
# print(1,2,3)
# #1 2 3
# The last two exhibit the desired result, you just need to set sep='' to get 123 (w/o spaces).
# =============================================================================



n = int(input()) *range (1, n+1)
# =============================================================================
# # = range is from 1 to n, exclusive of n. 
# so if your input is 3 then it prints 1 2. So input to the range function is 1 to n+1
# =============================================================================
# =============================================================================
# 
# if you don't give sep='' in print statement then each value is seperated by a space
# =============================================================================
# import calendar
#Calendar module
print(list(calendar.day_name)[calendar.weekday(y, m, d)].upper())


#Doomsday algorithm???
weekdays = ['SUNDAY','MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY']
def dayofweek(month, day, yr):
    """dayOfWeek() takes a Gregorian date as (month, day, yr), and finds the day of the week for that date.
        Source: http://hackerpublicradio.org/eps/hpr1240/doomsday.py"""
    centuryAnchor = (16 - 2 * (yr // 100 % 4)) % 7 # Find the Doomsday Century Anchor
    yr = yr % 100 # Calculate Doomsday number for year within century
    yrs_12 = yr % 12
    offset = yr // 12 + yrs_12 + yrs_12 // 4 + centuryAnchor
    monpos = [0, 3, 0, 7, 4, 9, 6, 11, 8, 12, 10, 14, 12][month] # MonthPosLookUp
    if month < 3 and (yr or centuryAnchor == 2) and not yr % 4: # January and February need leap year adjustment
        monpos += 1 # 1: If on a 4N year and year is not a Century boundary (i.e., not 0) or Century Anchor is Tuesday
    return weekdays[(35 + day - monpos + offset) % 7] # Make adjustments from Doomsday setting for the month
print(dayofweek(*map(int, input().split())))


This is the Python's slice syntax of string, list, or tuple. s[::-1] returns s as reversed order like this:

s = 'abcde'
print(s[::-1]) # => 'edcba'


word='caturday'
word[-1::-1]
def front_back(str):
  front=str[:1]
  back=str[:-1]
  middle= str[1:-1]
  return back+middle+front



# =============================================================================
# Printing the number of even numbers in an array
# 
# Return the number of even ints in the given array.
# Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
# def count_evens(nums):
# =============================================================================
  count=0
  for n in nums:
    count -= n%2-1
  return count

# =============================================================================
# Given an array length 1 or more of ints, return the difference between the 
# largest and smallest values in the array. Note: the built-in min(v1, v2) 
# and max(v1, v2) functions return the smaller or larger of two values.
# =============================================================================

def big_diff(nums):
  for num in nums:
    nummax= max(nums)
    nummin=min(nums)
    return nummax-nummin


# =============================================================================
# Return the "centered" average of an array of ints, which we'll say is the mean 
# average of the values, except ignoring the largest and smallest values in the 
# array. If there are multiple copies of the smallest value, ignore just one 
# copy, and likewise for the largest value. Use int division to produce the final
#  average. You may assume that the array is length 3 or more.
# =============================================================================
def centered_average(nums):
  nums.sort()
  return sum(nums[1:-1])/(len(nums)-2)

# Takes the array and sorts it (asc by default)
# Then returns the sum of all the ints in the array except for the first and 
# the last one and divides it by the length -2 of the array (-2 because removed
# two of the values).
  
# =============================================================================
# Return the sum of the numbers in the array, returning 0 for an empty array.
# Except the number 13 is very unlucky, so it does not count and numbers that 
# come immediately after a 13 also do not count.
# =============================================================================

nums = ([1, 2, 2, 1, 13, 1]) 


def sum13(nums):
    while 13 in nums:
      if nums.index(13) < len(nums)-1: 
        nums.pop(nums.index(13)+1)
      nums.pop(nums.index(13))
    return sum(nums)

print(sum13(nums))



# %% Return the sum of the numbers in the array, except ignore sections of numbers 
# starting with a 6 and extending to the next 7 (every 6 will be followed by at 
# least one 7). Return 0 for no numbers.
# =============================================================================


# =============================================================================
# Given an array of ints, return True if 6 appears as either the first or last 
# element in the array. The array will be length 1 or more.
# =============================================================================
def first_last6(nums):
  return nums[0] == 6 or nums[-1] == 6

# =============================================================================
# Given an array of ints, return True if the array is length 1 or more, and the 
# first element and the last element are equal.
# =============================================================================
def same_first_last(nums):
  return len(nums) >= 1 and nums[0] == nums[-1]

# =============================================================================
# Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
# =============================================================================

def make_pi():
  return [3,1,4]

# =============================================================================
# Given 2 arrays of ints, a and b, return True if they have the same first 
# element or they have the same last element. Both arrays will be length 1 or 
# more.
# =============================================================================
def common_end(a, b):
  return a[0]==b[0] or a[-1]==b[-1]

# =============================================================================
# Given an array of ints length 3, return the sum of all the elements.
# =============================================================================
def sum3(nums):
  for num in nums:
    return sum(nums)

#could also just
def sum3(nums):
    return sum(nums)

# =============================================================================
# Given an array of ints length 3, return an array with the elements 
# "rotated left" so {1, 2, 3} yields {2, 3, 1}.
# =============================================================================
nums=([1, 2, 3])

def rotate_left3(nums):
  nums.append(nums[0]) #append the first element to the end
  nums.pop(0) #it is still at the beginning so remove the first element
  return nums #return the new array

rotate_left3(nums)

# =============================================================================
# Given an array of ints length 3, return a new array with the elements in 
# reverse order, so {1, 2, 3} becomes {3, 2, 1}.
# =============================================================================
nums=([1,2,3])
def reverse3(nums):
    return(nums[::-1]) #reverses order in a list

reverse3(nums)

# =============================================================================
# Given an array of ints length 3, figure out which is larger, the first or last 
# element in the array, and set all the other elements to be that value.
# Return the changed array.
# =============================================================================
def max_end3(nums):
  for num in nums:
    if nums[0] >= nums[-1]: #>= in case the first and last are equal
      nums[1]=nums[0]
      nums[2]=nums[1]
    elif nums[-1]>=nums[0]:
      nums[0]=nums[2]
      nums[1]=nums[2]
   
    return nums

#Alt. solution:
def max_end3(nums):
  big = max(nums[0], nums[2])
  nums[0] = big
  nums[1] = big
  nums[2] = big
  return nums

# =============================================================================
# Given an array of ints, return the sum of the first 2 elements in the array.
#  If the array length is less than 2, just sum up the elements that exist, 
#  returning 0 if the array is length 0.
# =============================================================================

def sum2(nums):
  if len(nums) >= 2:
    return nums[0] + nums[1]
  elif len(nums) ==1:
    return nums[0]
  else:
    return 0

# %%
# Given 2 int arrays, a and b, each length 3, return a new array length 2 
# containing their middle elements.

a=[(1,2,3])
b=([2,3,4])

def middle_way(a, b):
  c= [a[1],b[1]] #c needs to be an array so must wrap it in [] c=a[1],b[1] will
  #return (2,3) but you need c to return an array, not a tuple
  return c

#%% Given an array of ints, return a new array length 2 containing the first 
# and last elements from the original array. The original array will be length
# 1 or more.

def make_ends(nums):
  if len(nums) >1:
    return [nums[0],nums[-1]] #again, need it to be an array not a tuple so wrap in []
  else: #if array only has one int
    return [nums[0],nums[0]]

#%% Given an int array length 2, return True if it contains a 2 or a 3.
#just need true or false so can just ask it to return if contains 2 or 3
    
def has23(nums):
  return 2 in nums or 3 in nums

# %% Given a string and a non-negative int n, return a larger string that is
#  n copies of the original string.

def string_times(str, n):
  return n*str

#Alt solution:
def string_times(str, n):
    result = ""
    for i in range(n):  # range(n) is [0, 1, 2, .... n-1]
        result = result + str  # could use += here
    return result

# %% Given a string and a non-negative int n, we'll say that the front of the 
# string is the first 3 chars, or whatever is there if the string is less than
#  length 3. Return n copies of the front;

def front_times(str, n):
  return n*str[0:3]
# %% Given a string, return a new string made of every other char starting with
# the first, so "Hello" yields "Hlo".

def string_bits(str):
    return str[::2]  #slices str getting every letter from index 0 to end and 
#takes every other letter (because of the 2). str[::-2] would reverse the order
# of the characters

# %% Given a non-empty string like "Code" return a string like "CCoCodCode".

def string_splosion(str):
  result = ""
  # On each iteration, add the substring of the chars 0..i
  for i in range(len(str)):
    result = result + str[:i+1]
  return result
# %% Given a string, return the count of the number of times that a substring
# length 2 appears in the string and also as the last 2 chars of the string,
# so "hixxxhi" yields 1 (we won't count the end substring).

def last2(str):
  # Screen out too-short string case.
  if len(str) < 2:
    return 0
  # last 2 chars, can be written as str[-2:]
  last2 = str[len(str)-2:]
  count = 0
  # Check each substring length 2 starting at i
  for i in range(len(str)-2):
    sub = str[i:i+2]
    if sub == last2:
      count = count + 1

  return count

# %% Given an array of ints, return the number of 9's in the array.

def array_count9(nums):
  count = 0 #initialize count
  # Check each array for 9 
  for num in nums:
    if num == 9:
      count = count + 1 #add 1 to count for every 9 in array

  return count

# %% Given an array of ints, return True if one of the first 4 elements in the
# array is a 9. The array length may be less than 4.

def array_front9(nums):
  if len(nums) == 0:
    return False #check len so return false if empty array
  frontnums= nums[0:4] #check the front
  for num in nums:
    if 9 in frontnums: #if 9 is in first 4 slots
      return True #return true
    else:
      return False #otherwise, return false

# alt. solution
def array_front9(nums):
  # First figure the end for the loop
  end = len(nums)
  if end > 4:
    end = 4
  
  for i in range(end):  # loop over index [0, 1, 2, 3]
    if nums[i] == 9:
      return True
  return False

# %% Given an array of ints, return True if the sequence of numbers 1, 2, 3 
# appears in the array somewhere.

def array123(nums):
  seq = [1, 2, 3]
  if str(seq)[1:-1] in str(nums): #change to a str to see if sequ IN array
      return True
  else:
    return False

# alternate solution

def array123(nums):
  # Note: iterate with length-2, so can use i+1 and i+2 in the loop
  for i in range(len(nums)-2):
    if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
      return True
  return False

def last2(str):
  return len([i for i in range(len(str) - 2) if str[i:i+2] == str[-2:]])


# %% 
Given 2 strings, a and b, return the number of the positions where they contain
# the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the
# "xx", "aa", and "az" substrings appear in the same place in both strings.

def string_match(a, b):
  # Figure which string is shorter.
  shorter = min(len(a), len(b))
  count = 0
  
  # Loop i over every substring starting spot.
  # Use length-1 here, so can use char str[i+1] in the loop
  for i in range(shorter-1):
    a_sub = a[i:i+2]
    b_sub = b[i:i+2]
    if a_sub == b_sub:
      count = count + 1

  return count







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







# %%







