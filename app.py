import time  # time module
import time
import fractions
import math
print('Hello World')
print('Jose')
print(48)
print(5*6)

# float can be decimal #s

# Variables - store strings or into whatever data types into variables
# stores in a place of memory for us to access later
# write out whatever name we want to give it
#ex. below

# calculation = 2*(5+6)  # 22

# print(calculation * 3)  # 66

age1 = 22
age2 = 25
age3 = 27

# use LIST instead

ages = [22, 25, 27]
ages[0]  # = 22

questions = ['Should I code today?',
             'Favorite type of pet?', 'Love your family?']

answers = ['Yes!', 'Dogs', 'Of course!']


# define a function in Python . Steps
# 1. def stands for define. How you define your own function
# 2. then whatever name you want to use for your function
# 3. put () at the end of the function
# 4. end with :
# hit enter and start defining the body of that function. what function does
# anything after : is actually ran
# run a function by writing function name

# for loop


def joseTrivia():
    score = 0  # initialize a variable called score and set it to zero
    for i in range(len(questions)):
        print(questions[i])
        # allow user to input an answer
        # \n = print a new line
        # whatever user inputs as the answer is going to be saved in this variable
        ans = input('Please answer \n')
        # check whether this answer is equal to the answers list
        # compare to things by ==
        if ans == answers[i]:
            # whatever we run here will only run if this condition is true
            print('Correct!!')
            # if answer is correct, we want to implement this variable by 1
            # reassign it so score is + to whatever score is currently, plus 1
            score = score + 1  # or shortcut: score += 1
        # take out indentation so whatever code we write isn't part of the if statement anymore
        else:
            print('Incorrect buddy!')

    # F String
    # We literally dont want to type score, want to access the score variable & print whatever the value of that variable is
    print(f'Final Score: {score}')


joseTrivia()


print(3+7)
print(3*2)  # =6
# decimal point notation
# when an integer is divided by another, the result is not necessarily an integer.
# The rule in Python is to return a number with a decimal point and a fractional part, even when the result is an integer
# Values without the decimal point are said to be of type integer or simply int.
# Values with decimal points and fractional parts are said to be of type floating point or simply float.
print(5/2)  # = 2.5
print(4/2)  # = 2.0 not 2


# math basically handled using PEMDAS
print(2 * 3 + 1)  # = 7
print((3+1) * 3)  # = 12
print(4.321/3 + 10)  # = 11.440333333333333
print(4.321 / (3+10))  # = 0.3323846153846154


# To compute 2(the 4th power), you need to use the exponentiation operator **
print(2**3)  # = 8
print(2**4)  # = 16

# The // operator in expression a//b returns the integer quotient obtained when integer a is divided by integer b.
print(14//3)  # = 4 . 3 goes into 14, 4 times

# The % operator in expression a%b computes the remainder obtained when integer a is divided by integer b.
print(14 % 3)  # = 2 . 2 is the remainder after 3 goes into 14, 4 times.

# how to write f(x) = x + 1


def f(x):
    return x + 1


f(3)  # =4
f(5)  # = 6

# Absolute value of a number value:
print(abs(-4))  # = 4
print(abs(4))  # = 4
print(abs(-3.2))  # = 3.2

# Min Value
print(min(6, -2, -4, 25))  # = -4
# Max Value
print(max(5, -9, 27, 89))  # = 89

# Practice problems
# A.  The sum of the first five positive integers
print(1+2+3+4+5)  # = 15
# or
a = (1, 2, 3, 4, 5)
sum(a)

# B. The average age of Sara (age 23), Mark (age 19), and Fatima (age 31)
print((23+19+31) / 3)  # = 24.33
# or
age = (23, 19, 31)
average_age = sum(age)/len(age)
print(average_age)

# C.  The number of times 73 goes into 403
print(403//73)  # = 5

# D. The remainder when 403 is divided by 73
print(403 % 73)  # = 38

# E. 2 to the 10th power
print(2**10)  # = 1024

# F. The absolute value of the difference between Sara’s height (54 inches) and Mark’s height (57 inches)
print(abs(54-57))  # = 3

# G. The lowest price among the following prices: $34.99, $29.95, and $31.50
print(min(34.99, 29.95, 31.50))  # = 29.95


# Boolean Expressions-expressions that evaluate to one of two Boolean values: True or False.

print(2 < 3)  # = True
print(3 < 2)  # = False
# algebraic expressions on either side of a comparison operators are evaluated before the comparison is made.
print(5 - 1 > 2 + 1)  # = True


# ==
# In order to check equality between values, the comparison operator == is used.
3 == 3  # = True
3+5 == 4+4  # = True
3 == 5-3  # = False

# There are a few other logical comparison operators:
# <= operator to test whether the expression on the left (3) is less than or equal to the expression of the right (4)
3 <= 4  # = True
# test whether the operand on the left is greater than or equal to the operand on the right
3 >= 4  # = False
# uses the != (not equal) operator to test whether the expressions on the left and right evaluate to different values.
3 != 4  # = True


# Practice problems
# (a) The sum of 2 and 2 is less than 4.
2+2 < 4  # = False
# (b) The value of 7 // 3 is equal to 1 + 1.
7 // 3 == 1+1  # = True 2==2
# (c) The sum of 3 squared and 4 squared is equal to 25.
(3**2) + (4**2) == 25  # = True
# (d) The sum of 2, 4, and 6 is greater than 12.
2+4+6 > 12  # = False
# or
x = (2, 4, 6)
sum(x) > 12
# (e) 1387 is divisible by 19.
1387 % 19 == 0  # = True 3187//19 divides into a whole int.
# (f) 31 is even. (Hint: what does the remainder when you divide by 2 tell you?)
31 % 2 == 0  # = False 31%2 remainder is 1 so false
# (g) The lowest price among $34.99, $29.95, and $31.50 is less than $30.00.
min(34.99, 29.95, 31.50) < 30  # = True 29.95<30

#Boolean expressions can be combined together using Boolean operators and , or , and not to form larger Boolean expressions.#
# AND Operator
# The and operator applied to two Boolean expressions will evaluate to True if both expressions evaluate to True;
# if either expression evaluates to False, then it will evaluate to False:

2 < 3 and 4 > 5  # = False, both not true
2 < 3 and 1 < 4  # = True, both are true

# OR Operator
# The or operator applied to two Boolean expressions evaluates to False only when both expressions are false.
# If either one is true or if both are true, then it evaluates to True.

3 < 4 or 4 < 3  # = True, one of these are true
3 < 2 or 2 < 1  # = False, both are false

# NOT Operator
# The not operator is a unary Boolean operator,
# which means that it is applied to a single Boolean expression (as opposed to the binary Boolean operators and and or).
# It evaluates to False if the expression is true or to True if the expression is false.

not (3 < 4)  # = False
not (3 > 4)  # = True
not (4 < 3)  # = True

# assigning names to values is called Variables
# statement x=3 is called an assignment statement.
# The general format of an assignment statement is:
# <variable> = <expression>
# variable x can be thought of as a name that enables us to retrieve value 3 later on.
x = 3
x  # or print(x)    = 3

4 * x  # = 12

# An expression involving variables may appear on the right side of an assignment
counter = 4 * x
# In statement counter = 4 * x, x is first evaluated to 3,
# Then the expression 4 * 3 is evaluated to 12, and then 12 gets assigned to variable counter:
counter  # or print(counter) = 12

# Practice Problems
# (a) Assign integer value 3 to variable a.
a = 3
# (b) Assign 4 to variable b.
b = 4
# (c) Assign to variable c the value of expression a * a + b * b
c = a*a + b*b

# the value of a variable can change
# variable x is initially 3: print(x) =  3
x = 7
x


# Strings
# a sequence of characters, including blanks, punctuation, and various symbols.
# A string value is represented as a sequence of characters that is enclosed within quotes:
'Hello, World!'
s = "hello"
s  # = 'hello'

# String Operators
s == 'hello'  # = true because we assigned variable s to string 'hello'
t = 'world'
s != t  # = True because s does NOT EQUAL t
s == t  # = false. S='hello' and t='world'

# the comparison operators < and > compare strings using the dictionary(alphabetical) order:
s < t  # = true. S comes b4 t
s > t  # = false. s is before T so not after

# Concatenation
# the joining of the two strings:
s + t  # = 'helloworld'
# ' ' quotes with a space between creates space between strings
s + ' ' + t  # = 'hello world'


# check whether a character appears in a string:
s = 'hello'
'h' in s  # = true. 'h' is in hello
'g' in s  # = false. 'g' is not in hello


# Length of a string
# The length of a string can be computed using the len() function:
len(s)  # = 5 bcus 'hello' is 5 characters long

# Practice Problems
s1 = 'ant'
s2 = 'bat'
s3 = 'cod'
# Write Python expressions using s1, s2, and s3 and operators + and * that evaluate to:

# (a) 'ant bat cod'
s1 + ' ' + s2 + ' ' + s3
# (b) 'ant ant ant ant ant ant ant ant ant ant '
(s1 + ' ') * 10
# (c) 'ant bat bat cod cod cod'
s1 + ' ' + (s2 + ' ') * 2 + ' ' + (s3 + ' ') * 3
# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
(s1 + ' ' + s2 + ' ') * 7
# (e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '
((s2 * 2) + s3 + ' ') * 5    # or (s2+s2+s3+' ') * 5


# Indexing Operator
# The individual characters of a string can be accessed using the indexing operator. Starts from 0 -> on.
s[0]  # = h
s[1]  # = e
s[4]  # = o

# Practice Problem 2.5
z = '0123456789'
# Now write expressions using string s and the indexing operator that evaluate to:
# (a) '0'
z[0]
# (b) '1'
z[1]
# (c) '6'
z[6]
# (d) '8'
z[8]
# (e) '9'
z[9]


# Negative indexes
# may be used to access the characters from the back (right side) of the string.
# The index −1 refers to the last character;
# so s[-1] evaluates to string 'o'. s[-2] evaluates to 'l'.
s  # = hello
s[-1]  # = o
s[-2]  # = l
s[-5]  # = h


#Lists and Tuples
# In Python, lists are usually stored in a type of object called a list.
# A list is a sequence of objects.
# The objects can be of any type: numbers, strings, even other lists.

pets = ['goldfish', 'cat', 'dog']
pets  # = ['goldfish' , 'cat', 'dog']
pets[2]  # = 'dog'

things = ['one', 2, [3, 4]]
# 'one' = string
# 2 = integer
# [3,4] = list
things[0]  # = 'one'
things[2]  # = [3,4]


# List Operators
# items in A list may be accessed individually using the indexing operator,
# just as individual characters can be accessed in a string:

pets[0]  # ='goldfish'
pets[1]  # ='cat'
# Negative Indexes for List operators
pets[-1]  # = 'dog'

# Length of a list
len(pets)  # = 3

# Adding/Concatenating and multiplying lists
# Like strings, lists can be “added,” meaning that they can be concatenated.

pets + pets  # = ['goldfish', 'cat', 'dog', 'goldfish', 'cat', 'dog']
pets * 2  # = ['goldfish', 'cat', 'dog', 'goldfish', 'cat', 'dog']

# Check for an object inside a string
# IN
# you can use the in operator in a Boolean expression that evaluates
'rabbit' in pets  # = false
'dog' in pets  # = true

# Operators used commonly in lists
gas = [2.99, 3.49, 2.79, 3.75]
min(gas)  # = 2.79
max(gas)  # = 3.75
sum(gas)  # = 13.02

# Practice Problem 2.6
# First execute the assignment
words = ['bat', 'ball', 'barn', 'basket', 'badminton']
# Now write two Python expressions that evaluate to the first and last, respectively, word in words, in dictionary(a-z) order.
min(words)  # = 'badminton'
max(words)  # = 'bat'


# Lists Are Mutable, Strings Are Not
# Lists are mutable and the content of a list can be changed.
# ex. want to change the type of cat in the list pets
pets[1] = "Brown cat"
pets  # or print(pets) = ['goldfish' , 'Brown Cat', 'dog']

# Strings aren't mutable. What that means is that we cannot change the individual characters of a string value.
# But..We can simply reassign a brand new value to any variable.
myCat = 'Brown bat'
myCat = 'Brown cat'
print(myCat)  # = 'Brown Cat'


# Tuples/Immutable Lists
# behave like lists except that tuples are immutable.
# A tuple object contains a sequence of values separated by commas and enclosed in parentheses ( ) instead of brackets [ ]:

days = ('Mon', 'Tue', 'Wed')
print(days)  # = ('Mon' , 'Tue', 'Wed')
days = ('Mon', 'Tue', 'Wed', 'Thu')
days  # = ('Mon' , 'Tue', 'Wed', 'Thu')

# All operators work in tuples as well
'Fri' in days  # = false
week = days + ('Fri', 'Sat', 'Sun')
week  # = ('Mon' , 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
len(week)  # = 7
2*week  # = ('Mon' , 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon' , 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')

days[2]  # = 'Wed'

# Create a one element tuple?
# add a comma after the first, and only, item to get a one-item tuple object:
day = ('Mon',)
type(day)  # = tuple

# List and Tuple Methods
# There are also functions that are called on lists.
# Add a string to the list

pets.append('cow')
pets  # = ['goldfish', 'Brown cat', 'dog', 'cow']

pets.append('dog')
print(pets)  # = ['goldfish', 'Brown cat', 'dog', 'cow', 'dog']

# append()
# Append can't be called on it's own, needs to be called on some list.
# List functions like append are known as methods.
# List function: COUNT
pets.count('dog')  # = 2

# remove()
# To remove the first occurrence of 'dog', we can use the list method remove():
pets.remove('dog')
pets  # = ['goldfish', 'Brown cat', 'cow', 'dog']

# reverse()
# The list method reverse() reverses the order of the objects:
pets.reverse()
pets  # = ['dog', 'cow', 'Brown cat', 'goldfish']

# sort()
# The sort() method sorts the items in the list in increasing order,
# using the ordering that “naturally” applies to the objects in the list.
# If the list contains string objects, the order will be lexicographical(i.e., dictionary order(a-z)):
pets.sort()
pets  # = ['Brown cat', 'cow', 'dog' , 'goldfish']

nums = [4, 2, 8, 5]
nums.sort()  # =[2, 4 , 5, 8]

# Practice Problem 2.7
grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]
# (a) An expression that evaluates to the number of 7 grades
grades.count(7)  # = 2
# (b) A statement that changes the last grade to 4
grades[-1] = 4
# or
grades.remove(2)
grades.append(4)
grades  # = [9, 7, 7, 10, 3, 9, 6, 6, 4]
# (c) An expression that evaluates to the maximum grade
max(grades)  # = 10
# (d) A statement that sorts the list grades
grades.sort()
grades  # = [3,4,6,6,7,7,9,9,10]
# (e) An expression that evaluates to the average grade
averageGrades = sum(grades)/len(grades)
print(averageGrades)

# The only tuple methods that can be used are count() & index() since tuples are immutable.


#Objects and Classes
# In Python, every value, whether a simple integer value (such as 3) or a more complex
# value (such as the string 'Hello, World!' or the list ['hello', 4, 5]) is stored in memory as an object.

# Object’s type-indicates what kind of values the object can hold and what kind of operations can be performed on the object.
type(3)  # = int type
type(3.0)  # = Float type
type('Hello World')  # = Str Type
type([1, 2, 3, 4, 5])  # = List Type

# When used on a variable, the type() function will return the type of the object the variable refers to:
p = 3
type(p)  # = int type

# Class-refer to types whose values are stored in objects.
# Because every value in Python is stored in an object, every Python type is a class.

2 - 3 + 1  # = 0
# a good developer would use parentheses to clearly indicate her intent:
(2-3) + 1  # = 0


# Practice Problem 2.8
# In what order are the operators in the following expressions evaluated?
# (a) 2 + 3 == 4 or a >= 5
((2+3) == 4) or (a >= 5)  # = False
# (b) x[1] * -3 < -10 == 0
(((x[1]) * (-3)) < (-10)) == 0
#(c) (x[1] * -3 < -10) in [0, True]
(((x[1]) * (-3)) < (-10)) in [0, True]
# (d) 2 * 3**2
2 * (3**2)
# (e) 4 / 2 in [1, 2, 3]
(4/2) in [1, 2, 3]


# Creating Objects
# To create an integer object with value 3 (and assign it to variable x), we can use this statement:
x = 3
# Python also supports a way to create objects that makes the object type explicit:
x = int(3)
print(x)  # = 3

# The function int() is called a constructor; it is used to explicitly instantiate an integer object.
# The value of the object is determined by the function argument:
# If no argument is given, a default value is given to the object.


x = int()
print(x)  # = 0

y = float()
print(y)  # = 0.0

s = str()
print(s)  # = ' '

z = list()
print(z)  # = []


# Implicit Type Conversions
# If an algebraic or logical expression involves operands of different types,
# Python will convert each operand to the type that contains the others.

True + 5  # = 6
True + 5.0  # = 6.0


# Explicit Type Conversions
# Type conversions can also be done explicitly using the constructor functions.

int(3.4)  # = 3
int(-3.6)  # = -3

float(3)  # = 3.0

str(2.72)  # = '2.72'

# = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
list('hello world')

('hello world'.split())  # = ['hello', 'world']


# Practice Problems 2.9
# (a) False + False
False + False  # = 0 Integer Value
# (b) 2 * 3**2.0
2 * 3**2.0  # = 18.0 Float Value
# (c) 4 // 2 + 4 % 2
4 // 2 + 4 % 2  # = 2 Int Value
# (d) 2 + 3 == 4 or 5 >= 5
2 + 3 == 4 or 5 >= 5  # = True Boolean Value


# Class Methods
# Pets = Object which is a list
# Append = Method
# Pig = 'String'
pets.append('pig')


# Python Standard Library
# The Standard Library includes modules to support, among others:
# Network programming
# Web application programming
# Graphical user interface (GUI) development
# Database programming
# Mathematical functions
# Pseudorandom number generators
# Module Math


# Module Math
# The math module is a library of mathematical constants and functions.
# To use a math module function, the module must first be explicitly imported:
# import math

math.sqrt(9)

# Practice Problem 2.10
# Write Python expressions corresponding to the following:
# (a) The length of the hypotenuse in a right triangle whose other two sides have lengths a and b
math.sqrt((a**2) + (b**2))
# (b) The value of the expression that evaluates whether the length of the above hypotenuse is 5
math.sqrt((a**2) + (b**2)) == (5)
# (c) The area of a disk of radius a
math.pi * (a**2)
# (d) The value of the Boolean expression that checks whether a point with coordinates x
# and y is inside a circle with center (a, b) and radius r
(x - a)**2 + (y - b)**2 < r ** 2


# Module fractions
# The fractions module makes available a new type of number: the Fraction type.


a = fractions.Fraction(3, 4)
b = fractions.Fraction(1, 2)

print(a)  # = 3/4

a+b

c = a + b
print(c)
c  # = Fraction (5,4)


# Exercises
# 2.11 Write Python expressions corresponding to these statements:
# (a) The sum of negative integers −7 through −1
sum([-7 + -6 + -5 + -4 + -3 + -2 + -1])  # = -28
# or
x = (-7 + -6 + -5 + -4 + -3 + -2 + -1)
x

# (b) The average age of a group of kids at a summer camp given than 17 are 9 years old, 24 are 10 years old,
# 21 are 11 years old, and 27 are 12 years old.

campersAge = (17 * 9) + (24 * 10) + (21 * 11) + (27 * 12)
amountOfCampers = (17 + 24 + 21 + 27)
campersAge / amountOfCampers  # = 10.65

# (c) 2 to the power −20
2**-20  # = 9.5367431640625e-07
# (d) The number of times 61 goes into 4356
4356 // 61  # = 71
# (e) The remainder when 4365 is divided by 61
4356 % 61  # = 25


# 2.12 Start by evaluating, in the interactive shell, the assignment:
s1 = '-'
s2 = '+'
# Now write string expressions involving s1 and s2 and string operators + and * that evaluate to:
# (a) '- +'
s1 + s2
# (b) '- + -'
s1 + s2 + s1
# (c) '+ – –'
s2 + s1 + s1
# (d) '+ – – + – –'
s2 + s1 + s1 + s2 + s1 + s1
# (e) '+ – – + – – + – – + – – + – – + – – + – – + – – + – – + – – +'
((s2 + (s1*2)) * 10) + s2
# (f) '+ – + + + – – + – + + + – – + – + + + – – + – + + + – – + – + + + – –'
(s2 + s1 + (s2 * 3) + (s1 * 2)) * 5
# Try to make your string expressions as succinct as you can.


# 2.13 Start by running, in the shell, the following assignment statement:
s = 'abcdefghijklmnopqrstuvwxyz'
# Now write expressions using string s and the indexing operator that evaluate to 'a', 'c', 'z', 'y', and 'q'.
s[0]  # = a
s[2]  # = c
s[25]  # = z or [-1]
s[24]  # = y or [-2]
s[16]  # = q or [-10]


# 2.14 Start by executing
s = 'goodbye'
# Then write a Boolean expression that checks whether:
# (a) The first character of string s is 'g'
s[0] == 'g'  # true
# (b) The seventh character of s is 'g'
s[6] == 'g'  # false
# (c) The first two characters of s are 'g' and 'a'
s[0] == 'g' and s[1] == 'a'  # false
# (d) The next to last character of s is 'x'
s[-2] == 'x'  # = false
# (e) The middle character of s is 'd'
s[3] == 'd'  # = true
# (f) The first and last characters of string s are equal
s[0] == s[-1]  # false
# (g) The last four characters of string s match the string 'tion'
s[-4:] == 'tion'  # false
# Note: These seven statements should evaluate to True, False, False, False, True, False, and False, respectively.


# 2.15 Write Python expressions corresponding to these statements:
# (a) The number of characters in the word "anachronistically" is 1 more than the number
# of characters in the word "counterintuitive."
a = 'anachronistically'
c = 'counterintuitive'
len(a)  # = 17
len(c)  # = 16
len(a) == len(c) + 1  # = true
# (b) The word "misinterpretation" appears earlier in the dictionary than the word "misrepresentation."
b = ['misrepresentation', 'misinterpretation']
b.sort()
print(b)  # = ['misinterpretation', 'misrepresentation']
# (c) The letter "e" does not appear in the word "floccinaucinihilipilification."
f = 'floccinaucinihilipilification'
'e' not in f  # = true     or 'e' in f = false
# (d) The number of characters in the word "counterrevolution" is equal to the sum of the
# number of characters in words "counter" and "resolution."
c1 = 'counterrevolution'
c2 = 'counter'
c3 = 'resolution'
len(c1)  # = 17
len(c2)  # = 7
len(c3)  # = 10
# or len(counterrevolution) == (len(counter) + len(resolution))
len(c1) == (len(c2) + len(c3))


# 2.16 Write the corresponding Python assignment statements:
# (a) Assign 6 to variable a and 7 to variable b.
a = 6
b = 7
# (b) Assign to variable c the average of variables a and b.
c = (a+b) / 2
c  # = 6.5
print('average:', c)
# (c) Assign to variable inventory the list containing strings 'paper', 'staples', and 'pencils'.
inventory = ['paper', 'staples', 'pencils']
print(inventory)
# (d) Assign to variables first, middle and last the strings 'John', 'Fitzgerald', and 'Kennedy'.
first = 'John'
middle = "Fitzgerald"
last = 'Kennedy'
print(first, middle, last)
# (e) Assign to variable fullname the concatenation of string variables first, middle,
# and last. Make sure you incorporate blank spaces appropriately.
fullName = (first + ' ' + middle + ' ' + last)
print(fullName)


# 2.17 Using variables defined in Exercise 2.16, write Boolean expressions corresponding to
# the following logical statements and evaluate the expressions:
# (a) The sum of 17 and −9 is less than 10.
(17 + -9) < 10  # = True
d = 17
e = -9
f = (d + e) < 10  # = True
print(f)
# (b) The length of list inventory is more than five times the length of string fullname.
len(inventory)  # = 3
len(fullName)  # = 23
len(fullName) * 5  # = 115
len(inventory) > (len(fullName) * 5)  # = false
# (c) c is no more than 24.
c <= 24
# (d) 6.75 is between the values of integers a and b.
(a < 6.75) and (6.75 < b)  # or (a < 6.75) and (b > 6.75)
a < 6.75 < b  # = true or
b > 6.75 > a
# (e) The length of string middle is larger than the length of string first and smaller than the length string last.
len(first) < len(middle) < len(last)  # = False or
len(last) > len(middle) > len(first)
# (f) Either the list inventory is empty or it has more than 10 objects in it.
len(inventory) == 0 or len(inventory) > 10


# 2.18 Write Python statements corresponding to the following:
# (a) Assign to variable flowers a list containing strings 'rose', 'bougainvillea',
# 'yucca', 'marigold', 'daylily', and 'lily of the valley'.
flowers = ['rose', 'bougainvillea', 'yucca',
           'marigold', 'daylily', 'lily of the valley']
# (b) Write a Boolean expression that evaluates to True if string 'potato' is in list flowers, and evaluate the expression.
'potato' in flowers  # = false
# (c) Assign to list thorny the sublist consisting of the first three objects in list flowers.
#thorny = ['rose', 'bougainvillea', 'yucca']
thorny = [flowers[0], flowers[1], flowers[2]]  # or
thorny = flowers[0:3]
print(thorny)  # = ['rose', 'bougainvillea', 'yucca']
# (d) Assign to list poisonous the sublist consisting of just the last object of list flowers.
poisonous = flowers[-1:]
print(poisonous)  # = lilly of the valley
# (e) Assign to list dangerous the concatenation of lists thorny and poisonous.
dangerous = thorny + poisonous
print(dangerous)  # = ['rose', 'bougainvillea', 'yucca', 'lily of the valley']


# 2.19 Start by assigning to variable answers a list containing an arbitrary sequence of strings 'Y' and 'N'. For example:
answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']
# Write Python statements corresponding to the following:
# (a) Assign to variable numYes the number of occurrences of 'Y' in list answers.
numYes = answers.count('Y')
print(numYes)
# (b) Assign to variable numNo the number of occurrences of 'N' in list answers.
numNo = answers.count('N')
print(numNo)
# (c) Assign to variable percentYes the percentage of strings in answers that are 'Y'.
#percentYes = (numYes/len(answers)) * 100
# print(percentYes)
# or to get actual %:
percentYes = (numYes/len(answers))
print("{0:.0%}".format(percentYes))
# (d) Sort the list answers.
answers.sort()
print(answers)
# (e) Assign to variable f the index of the first occurrence of 'Y' in sorted list answers.
f = answers.index('Y')
print(f)


# 2.20 Write an expression involving a three-letter string s that evaluates to a string whose
# characters are the characters of s in reverse order. If s is 'top', the expression should evaluate to 'pot'.
s = 'top'
s[::-1]
print(s)  # = pot or
print(s[-1]+s[-2]+s[-3])


# 2.21 Write an expression involving strings s and t containing the last name and the first
# name, respectively, of a person that evaluates to the person’s initials. If the two strings con-
# tained the first and last name of this book’s author, the expression would evaluate to 'LP'.

s = 'Jose'
t = 'Armas'

initials = s[0] + t[0]
print(initials)


# 2.22 The range of a list of numbers is the largest difference between any two numbers in the
# list. Write a Python expression that computes the range of a list of numbers lst. If the list
# lst is, say, [3, 7, -2, 12], the expression should evaluate to 14 (the difference between
# 12 and −2).

numList = [2, 5, 7, 10]
differenceOfNum = max(numList) - min(numList)
print(differenceOfNum)


# 2.23 Start by assigning to variables monthsL and monthsT a list and a tuple, respectively,
# both containing strings 'Jan', 'Feb', 'Mar', and 'May', in that order. Then attempt the
# following with both containers:

monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

# (a) Insert string 'Apr' between 'Mar' and 'May'.
monthsL.insert(3, 'Apr')
print(monthsL)  # = ['Jan', 'Feb', 'Mar', 'Apr', 'May']

# (b) Append string 'Jun'.
monthsL.append('Jun')
print(monthsL)  # = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']

# (c) Pop the container.
monthsL.pop()
print(monthsL)  # = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
# (d) Remove the second item in the container.
monthsL.remove('Feb')
print(monthsL)  # = ['Jan', 'Mar', 'Apr', 'May']
# (e) Reverse the order of items in the container.
monthsL.reverse()
print(monthsL)  # = ['May', 'Apr', 'Mar', 'Jan']
# (f) Sort the container.
monthsL.sort()
print(monthsL)  # = ['Apr', 'Jan', 'Mar', 'May']
# Note: when attempting these on tuple monthsT you should expect errors.


# 2.24 Start by assigning to variable grades a list containing an arbitrary sequence of grades
# (strings) 'A', 'B', 'C', 'D', and 'F'.

# Write a sequence of Python statements that ultimately produce a list count that contains
# the numbers of occurrences of each grade in list grades in alphabetic order.

grades = ['B', 'B', 'F', 'C', 'B', 'A', 'A', 'D', 'C', 'D', 'A', 'A', 'B']

count = [grades.count('A'), grades.count('B'), grades.count(
    'C'), grades.count('D'), grades.count('F')]

print(count)  # = [4, 4, 2, 2, 1]


# 2.25Repeat Problem 2.24 with the following modification: variable grades is defined to be of type tuple rather than of type list:
gradesTwo = ('B', 'B', 'F', 'C', 'B', 'A', 'A', 'D', 'C', 'D', 'A', 'A', 'B')
# Variable count should still refer to a list.

countTwo = (gradesTwo.count('A'), gradesTwo.count('B'), gradesTwo.count(
    'C'), gradesTwo.count('D'), gradesTwo.count('F'))

print(countTwo)  # = (4, 4, 2, 2, 1)


# 2.26 #A dartboard of radius 10 and the wall it is hanging on are represented using the two-
# dimensional coordinate system, with the board’s center at coordinate (0, 0). Variables x and
# y store the x- and y-coordinate of a dart hit. Write an expression using variables x and y
# that evaluates to True if the dart hits (is within) the dartboard, and evaluate the expression
# for these dart coordinates:
r = 10
#(a) (0, 0)
(x, y) = (0, 0)

(x - a)**2 + (y - b)**2 < (r ** 2)
#(b) (10, 10)
r = 10
(x, y) = (10, 10)
landed = ((x-a)**2) + ((y - b)**2) < (r ** 2)
print(landed)
# (c) (6, −6)
# (d) (−7, 8)


# 2.27 A ladder put up right against a wall will fall over unless put up at a certain angle less
# than 90 degrees. Given variables length and angle storing the length of the ladder and the
# angle that it forms with the ground as it leans against the wall, write a Python expression
# involving length and angle that computes the height reached by the ladder. Evaluate the
# expression for these values of length and angle:

# (a) 16 feet and 75 degrees
length = 16
angle = 75


degree = math.pi * angle/180
height = length * math.sin(degree)
print(height)  # = 15.45

# (b) 20 feet and 0 degrees
length = 20
angle = 0

degree = math.pi * angle/180
height = length * math.sin(degree)
print(height)  # = 0.0


# (c) 24 feet and 45 degrees
length = 24
angle = 45

degree = math.pi * angle/180
height = length * math.sin(degree)
print(height)  # = 16.97

# (d) 24 feet and 80 degrees
length = 24
angle = 80

degree = math.pi * angle/180
height = length * math.sin(degree)
print(height)  # = 23.64

# Note: You will need to use the trig formula:

# height = length ∗ sin(angle)

# The math module sin() function takes its input in radians. You will thus need to convert
# the angle given in degrees to the angle given in radians using:

# radians = π ∗ degrees / 180


# 2.28 Write the relevant Python expression or statement, involving a list of numbers lst
# and using list operators and methods for these specifications:

lst = [1, 2, 3, 4, 5, 6]
lstTwo = [1, 2, 3, 4, 5]


# (a) An expression that evaluates to the index of the middle element of lst
middleElement = (len(lst)) // 2
# = [3] which is #4 because middle element is rightmost of the 2 middle elements
print(middleElement)  # = 3

middleElementTwo = (len(lstTwo)) // 2
print(middleElementTwo)  # = 2 because #3 is the middle element

# (b) An expression that evaluates to the middle element of lst
(lst[middleElement])  # = 4
(lst[middleElementTwo])  # = 3
# (c) A statement that sorts the list lst in descending order
lst.reverse()
print(lst)

lstTwo.reverse()
print(lstTwo)

# another example
aLost = [2, 5, 0, 3]
aLost.sort()
print(aLost)
aLost.reverse()
print(aLost)


aLost.sort(reverse=True)
print(aLost)


# (d) A statement that removes the first number of list lst and puts it at the end
lst.remove(1)  # = 1
print(lst)  # = [2,3,4,5,6]
lst.append(1)
print(lst)  # = [2,3,4,5,6,1]
# or faster way
lst.append(lst.pop(0))
print(lst)  # = [2,3,4,5,6,1]

# Note: If a list has even length, then the middle element is defined to be the rightmost of the
# two elements in the middle of the list.


# 2.29 Add one or more pairs of parentheses to each expression so that it evaluates to True.
# For each expression, explain in what order the operators were evaluated.
# (a) 0 == 1 == 2
(0) == (1 == 2)  # = true
(0) == (1 == 25)
# (b) 2 + 3 == 4 + 5 == 7
((2) + (3 == 4) + 5) == 7  # = true
# (c) 1 < -1 == 3 > 4
(1 < -1) == (3 > 4)  # = true


# 2.30 Using an example of your own, explicitly convert some string to a list. Describe, in
# your own words, the behavior of the list constructor on a string input.

someString = 'Spider'

# = List of Characters =['S', 'p', 'i', 'd', 'e', 'r']
print(f'List of Characters ={list(someString)}')

secondString = 'Man'
print(list(secondString))  # = ['M', 'a', 'n']

anotherList = 'Spider Man'
print(f'List of Words ={anotherList.split()}')
# List of Words =['Spider', 'Man']

secondList = 'Bat Man'
print((secondList.split()))  # = ['Bat', 'Man']


# 2.31 In this chapter we have covered some, but not all, methods of class list. Using the
# following interactive session as an aid, explain in your own words what the list methods extend(), copy(), and clear() do.

# The extend() method adds the specified list elements (or any iterable) to the end of the current list.
list2 = [2, 3, 4]
list2.extend([5, 6])
print(list2)  # = [2, 3, 4, 5, 6]

carList = ['BMW', 'Jeep']
otherCars = ['Mazda', 'KIA']
carList.extend(otherCars)
print(carList)  # = ['BMW', 'Jeep', 'Mazda', 'KIA']


# The copy() method returns a copy of the specified list.
list3 = list2.copy()
print(list3)  # = [2, 3, 4, 5, 6]

cars = carList.copy()
print(cars)  # = ['BMW', 'Jeep', 'Mazda', 'KIA']


# The clear() method removes all the elements from a list.
list2.clear()
print(list2)  # = []

# Still keeps any copy of original list even if it was cleared
print(list3)  # = [2, 3, 4, 5, 6]

carList.clear()
print(carList)  # - []

print(cars)  # = ['BMW', 'Jeep', 'Mazda', 'KIA']


# Chapter 3
# Python program is a sequence of Python statements that are executed in order.

line1 = 'Hello Python developer'  # assignment statements
line2 = 'Welcome to the world of python'
print(line1)
print(line2)

# A module is simply a file containing Python code. Every file containing Python code
# and whose file name ends in .py is a Python module.

# print()
# This function prints, within the interactive shell, whatever argument is given to it.
# each print() statement "printed" its argument on a separate line.

print(0)  # = 0
print([0, 0, 0])  # = [0,0,0]
# A string argument is printed without the quotes:
print('zero')  # = zero
# If the input argument contains an expression, the expression is evaluated and the result is printed:
x = 0
print(x)  # = 0


# Interactive Input with input()
# Often an executing program needs to interact with the user.
# The input() function is used or that purpose. It is always used on the right side of an assignment statement, as in:
x = input('Enter your first name: ')
# 1. it will first print its input argument (string 'Enter your first name: ') in the shell:
# 2. then it will interrupt the execution and wait for the user to type something at the key-board.
# 3. user types something and hits the Enter/Return key on her keyboard, the execution will resume
# and whatever the user has typed will be assigned to variable name:
print(x)

first = input('Enter your first name: ')
last = input('Enter your last name: ')
line1 = 'Hello ' + first + ' ' + last + '...'
print(line1)  # = Hello Jose Armas...
print('Welcome to the world of Python!')


# The input() function will always treat whatever the user types as a string.

h = input('Enter a value for x: ')  # we entered in 5

# The Python interpreter treats the value entered as a string '5', not integer 5.
h == 5  # = false
h == '5'  # = true


# Function eval()
# If you expect the user to enter a value that is not a string, you need to explicitly ask Python
# to evaluate what the user types as a Python expression using the eval() function.

# The function eval() takes a string as input and evaluates the string as if it were a Python expression.

eval('3')  # = 3
eval('3 + 4')  # = 7
eval('len([3,5,7,9])')  # = 4


# The function eval() can be used together with the function input() when we expect the
# user to type an expression (a number, a list, etc.) when requested.
# All we need to do is wrap the eval() function around the input() function:
# The effect is that whatever the user types will be evaluated as an expression.

x = eval(input('Enter a value for x: '))  # enter 5

x == 5  # = True
x == '5'  # = False


# Practice Problem 3.1
# Implement a program that requests the current temperature in degrees Fahrenheit from the
# user and prints the temperature in degrees Celsius using the formula

# celsius = 5/9(fahrenheit − 32)


# entered in 50
fahr = eval(input('Enter the temperature in degrees Fahrenheit: '))

cels = fractions.Fraction(5, 9) * (fahr - 32)
print('The temperature in degrees Celsius is', cels)


# 3.2 Execution Control Structures

# If Statement-is used to implement conditional execution.

# prints 2 statements only if > 86
# print 'Goodbye!' before terminating, whether or not the temperature input by the user is > 86

temp = eval(input('Enter the current temperature: '))
if temp > 86:
    print('It is hot!')
    print('Drink water!')
print('Goodbye')


# In general, the format of an if statement is:

# The first line of an if statement consists of the if keyword, followed by Boolean expression
# Below the first line and indented with respect to
# the if keyword will be the block of code that is executed if condition evaluates to True.
# Whether the indented code has been executed, the execution continues
# with the Python statement <non-indented statement> directly below, and with the same
# indentation as, the first line of the if statement.

# if <condition>:
#   <indented code block>
# <non-indented statement>


# Translate these conditional statements into Python if statements:
# (a) If age is greater 62, print 'You can get your pension benefits'.
age = eval(input('How old are you?: '))
if age > 62:
    print('You can get your pension benefits')


# (b) If name is in list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'], print 'One of the top 5 baseball players, ever!'.

name = input('Your name?: ')
if name in ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']:
    print('One of the top 5 baseball players, ever!')


# (c) If hits is greater than 10 and shield is 0, print 'You are dead...'.

hits = eval(input('How many hits do you have?: '))
shield = eval(input('Your shield level?: '))
if hits > 10 and shield == 0:
    print('You are dead...')

# (d) If at least one of the Boolean variables north, south, east, and west is True, print 'I can escape.'.

direction = input('Which direction are you heading?: ')
if direction in 'North' or 'South' or 'East' or 'West':
    print('I can escape.')


# Two-Way Decisions
# We may need to perform one action when the condition is true and another if the condition is false.

temp2 = eval(input('Enter the current temperature: '))

if temp2 > 86:
    print('It is hot!')
    print('Drink water!')
else:
    print('Not too hot.')
    print('Might need a jacket!')
print('Goodbye.')


# if <condition>:
#   <indented code block 1>
# else:
#   <indented code block 2>
# <non-indented statement>


# Practice Problem 3.3
# Translate these into Python if/else statements:
# (a) If year is divisible by 4, print 'Could be a leap year.'; otherwise print 'Definitely not a leap year.'

year = eval(input('What year is it?: '))
if year % 4 == 0:
    print('Could be a leap year.')
else:
    print('Definitely not a leap year.')


# (b) If list ticket is equal to list lottery, print 'You won!'; else print 'Better luck next time...'
ticket = [12, 1, 13, 14]
lottery = [12, 1, 13, 14]

if ticket == lottery:
    print('You won!')
else:
    print('Better luck next time!')


# Practice Problem 3.4
# Implement a program that starts by asking the user to enter a login id (i.e., a string). The
# program then checks whether the id entered by the user is in the list ['joe', 'sue',
# 'hanna', 'sophie'] of valid users. Depending on the outcome, an appropriate message
# should be printed. Regardless of the outcome, your function should print 'Done.' before
# terminating.

loginID = input('Please enter your login ID: ')
logins = ['joe', 'sue', 'hanna', 'sophie']

if loginID in logins:
    print('You are in!')
else:
    print('User unknown')
print('Done.')


# Iteration Structures
# For Loop Statement
# Can print every character in a string or every object in a list
# char is a variable name.
# The for loop statement will repeatedly assign characters of string name to variable char.

myName = input('Enter a name: ')
print('The name spelled out: ')

for char in myName:
    print(char)

# =
# J
# o
# s
# e


# The for loop can also be used to iterate over the items of a list.
# The for loop executes the indented section print(animal) three times, once for each
# value of animal; the value of animal is first 'fish', then 'cat', and finally 'dog',
# animal is a variable name

animals = ['fish', 'cat', 'dog']
for animal in animals:
    print(animal)


# =
# fish
# cat
# dog


# In general, the for loop statement has this format:
# for <variable> in <sequence>:
#   <indented code block >
# <non-indented code block>


# Nesting Control Flow Structures

phrase = input('Enter a phrase: ')  # Hello world

for vowels in phrase:
    if vowels in 'aeoiuAEIOU':
        print(vowels)


# e
# o
# o


# Practice Problem 3.5
# Implement a program that requests from the user a list of words (i.e., strings) and then prints
# on the screen, one per line, all four-letter strings in the list.


wordList = eval(input('Enter a word list: '))
# Enter a word list: ['stop', 'desktop', 'top', 'post']


for fourLetterWords in wordList:
    if len(fourLetterWords) == 4:
        print(fourLetterWords)

# =
# stop
# post


# Function Range
# It is often necessary to iterate over a sequence of numbers in a given range, even if the list of numbers is not explicitly given.
# range() can be used together with the for loop to iterate over a sequence of numbers in a given range.

for igloo in range(5):
    print(igloo)

# =
# 0
# 1
# 2
# 3
# 4


# Practice Problem 3.6
# Write the for loop that will print these sequences of numbers, one per line, in the interactive shell.
# (a) Integers from 0 to 9 (i.e., 0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

for i in range(10):
    print(i)


# =
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9

# (b) Integers from 0 to 1 (i.e., 0, 1)

for i in range(2):
    print(i)


# =
# 0
# 1

# function call range(start,end)
# If we would like the sequence to start at a nonzero number start and end before number end, we make the function call range(start,end).

for i in range(2, 5):
    print(i)

# =
# 2
# 3
# 4


# function call range(start, end, step)
# In order to generate sequences that use a step size other than 1, a third argument can be used.
# The function call range(start, end, step) can be used to iterate over the sequence of
# integers starting at start, using a step size of step and ending before end.

for i in range(1, 14, 3):
    print(i)

# =
# 0
# 3
# 6
# 9
# 12
# The sequence printed by the for loop starts at 1, uses a step size of 3, and ends before 14. Therefore it will print 1, 4, 7, 10, and 13.


# Write the for loop that will print the following sequences of numbers, one per line.
# (a) Integers from 3 up to and including 12
for i in range(3, 13):
    print(i)

# =
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12

# (b) Integers from 0 up to but not including 9, but with a step of 2 instead of the default of 1 (i.e., 0, 2, 4, 6, 8)
for i in range(0, 10, 2):
    print(i)

# =
# 0
# 2
# 4
# 6
# 8

# (c) Integers from 0 up to but not including 24 with a step of 3
for i in range(0, 24, 3):
    print(i)

# =
# 0
# 3
# 6
# 9
# 12
# 15
# 18
# 21

# (d) Integers from 3 up to but not including 12 with a step of 5
for i in range(3, 12, 5):
    print(i)

# =
# 3
# 8


# def() function
# After the function definition statement has been executed, function f() can be used.

def f(x):
    result = (x**2) + 1
    return result


f(9)
# = 82


def funkyFunc(x):
    res = 3 * f(3) + 4
    return res


funkyFunc(3)
# = 34


# The Python function definition statement has this general format:

# def <function name> (<0 or more variables>):
#   <indented function body>


# *****    If a function is to return a value, then the return statement is used to specify the value to be returned.  ****


# Practice Problem 3.8
# Define, directly in the interactive shell, function perimeter() that takes, as input,
# the radius of a circle (a nonnegative number) and returns the perimeter of the circle. A sample usage is:
# perimeter(1)
# = 6.283185307179586


def perimeter(radius):
    return 2 * math.pi * radius


perimeter(1)  # = 6.283185307179586


# More than one argument?
# we need to have a distinct variable name for every input argument.

def squareSum(xAxis, yAxis):
    return (xAxis**2) + (yAxis**2)


squareSum(2, 2)
# = 8


# Practice Problem 3.9
# Implement function average() that takes two numbers as input and returns the average of
# the numbers. You should write your implementation in a module you will name average.py.
# A sample usage is:
# >>> average(1,3)
# 2.0

def average(firstNum, secondNum):
    return (firstNum + secondNum) / 2


average(1, 3)  # = 2


# Practice Problem 3.10
# Implement function noVowel() that takes a string s as input and returns True if no character
# in s is a vowel, and False otherwise (i.e., some character in s is a vowel).

def noVowel(s):
    for vowels in s:
        if vowels in 'aeiouAEIOU':
            return False
    return True


noVowel('crypt')  # true
noVowel('cwm')  # true
noVowel('car')  # false


# Practice Problem 3.11
# Implement function allEven() that takes a list of integers and returns True if all integers in the list are even, and False otherwise.

def allEven(numbers):
    for evenIntegers in numbers:
        if evenIntegers % 2 != 0:
            return False
    return True


allEven([8, 0, -2, 4, -6, 10])  # true
allEven([8, 0, -1, 4, -6, 10])  # false


def hello(name):
    print('Hello, ' + name + '!')


hello('Jose')  # Hello, Jose!


def f(x):
    return (x**2 + 1)


f(2)

3 * f(2) + 1


# Practice Problem 3.12
# Write function negatives() that takes a list as input and prints, one per line, the negative
# values in the list. The function should not return anything.

def negatives(negList):
    for negativeNums in negList:
        if negativeNums < 0:
            print(negativeNums)  # = [-1,-3,-9]


negatives([4, 0, -1, -3, 6, -9])


# Function Definitions Are “Assignment” Statements

question = input('Enter square or cube: ')

if question == 'square':
    def inputtedNum(number):
        return number * number
else:
    def inputtedNum(number):
        return number * number * number

inputtedNum(3)  # = 27

# First Define the Function, Then Use It
# Python does not allow calling a function before it is defined, just as a variable cannot be used in an expression before it is assigned.


# Docstrings
# a string that should describe what the function does and must be placed directly below the first line of a function definition.

def f(x):
    'returns x**2 +1'
    res = x**2 + 1
    return res


f(5)  # = 26

help(f)  # = returns x**2 +1


def hello(name):
    'a personalized name function'
    print('Hello, ' + name + '!')


hello('Jose Armas')  # = Hello, Jose Armas!

help(hello)


# Practice Problem 3.13
# Add appropriate docstrings to functions average() and negatives() from Practice Problems 3.9 and 3.12.
# Check your work using the help() documentation tool.

def average(firstNum, secondNum):
    'returns average of x and y'
    return (firstNum + secondNum) / 2


average(1, 3)  # = 2

help(average)  # returns average of x and y


def negatives(negList):
    'Returns negative #s from function negativeNums inside function negList'
    for negativeNums in negList:
        if negativeNums < 0:
            print(negativeNums)


negatives([4, 0, -1, -3, 6, -9])

# 'Returns negative #s from function negativeNums inside function negList'
help(negatives)


#Assignments and Mutability
# We often have the situation when multiple variables refer to the same object.

a = 3
b = a
print(b)  # = 3
a = 6
print(b)

a = [3, 4, 5]
b = a
print(b)  # = [3, 4, 5]

a[1] = 8
print(a)
print(b)  # = [3, 8, 5]

c = [1, 2, 3]
d = c

c.append(17)
print(c)  # = [1, 2, 3, 17]
print(d)  # = [1, 2, 3, 17]


# Practice Problem 3.14
# Draw a diagram representing the state of names and objects after this execution:

a = [5, 6, 7]
b = a
print(b)
a = 3
# = still is equal to [5, 6, 7] because we switched from a list to an int. Instead of modifying the list, so b doesn't change
print(b)


# multiple assignment statement:
e = 6
g = 3

e, g = g, e
print(e)  # = 3
print(g)  # = 6

i = j = k = 0
print(j)  # = 0
print(i)  # = 0
print(k)  # = 0


# Practice Problem 3.15
# Suppose a nonempty list team has been assigned. Write a Python statement or statements that swap the first and last value of the list.
# then the resulting list should be:
#['Sarah', 'Eleanor', 'Clare', 'Ava']

womensTeam = ['Ava', 'Eleanor', 'Clare', 'Sarah']

womensTeam[0], womensTeam[-1] = womensTeam[-1], womensTeam[0]
print(womensTeam)  # = ['Sarah', 'Eleanor', 'Clare', 'Ava']


# Immutable Parameter Passing
# Calling program-Functions are either called from within the interactive shell or by another program.
# names-The input arguments in a function of objects created in the calling program.

# We use the function g() to discuss the effect of passing a reference to an immutable object in a function call.


def g(x):
    x = 5


a = 3

g(a)


# The function g() did not, and cannot, modify the value of a in the interactive shell.
# when calling and executing a function, the function will not modify the value of any variable passed as a function argument
# if the variable refers to an immutable object.


# Mutable Parameter Passing
def h(list):
    list[0] = 5


myList = [3, 6, 9, 12]


h(myList)

print(myList)  # = [5, 6, 9, 12]


# Practice Problem 3.16
# Implement function swapFL() that takes a list as input and swaps the first and last elements of the list.
# You may assume the list will be nonempty. The function should not return anything.


def swapFlour(applePie):
    applePie[0], applePie[-1] = applePie[-1], applePie[0]


ingredients = ['flour', 'sugar', 'butter', 'apples']

swapFlour(ingredients)

print(ingredients)  # = ['apples', 'sugar', 'butter', 'flour']


# Exercises
# 3.17 Use the eval() function to evaluate these strings as Python expressions:
# (a) '2 * 3 + 1'
eval('2*3+1')  # = 7

# (b) 'hello'
eval(input('hello'))  # = hello

# (c) "'hello' + ' ' + 'world!'"
eval(input('hello' + ' ' + 'world!'))  # = hello world!

# (d) "'ASCII'.count('I')"
eval("'ASCII'.count('I')")  # = 2


# (e) 'x = 5'
eval(input('x=5'))  # =   x = 5


# 3.18 Assume a, b, and c have been defined in the interactive shell as shown:
# a, b, c = 3, 4, 5

a = 3
b = 4
c = 5

# Within the interactive shell, write if statements that print 'OK' if:
# (a) a is less than b.
if a < b:
    print('Ok')  # = OK

# (b) c is less than b.
if c < b:
    print('Ok')  # = .....(nothing printed)

# (c) The sum of a and b is equal to c.
if (a+b) == c:
    print('Ok')  # = .....(nothing printed)
# (d) The sum of the squares a and b is equal to c squared.
if (a**2) + (b**2) == c**2:
    print('OK')  # = OK


# 3.19 Repeat the previous problem with the additional requirement that 'NOT OK' is printed if the condition is false.
if a < b:
    print('OK')
else:
    print('NOT OK')  # OK


if c < b:
    print('Ok')
else:
    print('NOT OK')  # OK


if (a+b) == c:
    print('Ok')
else:
    print('NOT OK')  # NOT OK


if (a**2) + (b**2) == c**2:
    print('OK')
else:
    print('NOT OK')  # OK


# 3.20 Write a for loop that iterates over a list of strings months and prints the first three characters of every word.
# If months is the list ['January', 'February', 'March'] then the following should be printed:
# Jan
# Feb
# Mar

months = ['January', 'February', 'March']

for threeLetters in months:
    print(threeLetters[:3])

# =
# Jan
# Feb
# Mar


# 3.21 Write a for loop that iterates over a list of numbers lst and prints the even numbers in the list.
# For example, if lst is [2, 3, 4, 5, 6, 7, 8, 9], then the numbers 2, 4, 6, and 8 should be printed.

numbersList = [2, 3, 4, 5, 6, 7, 8, 9]

for evenNumbers in numbersList:
    if evenNumbers % 2 == 0:
        print(evenNumbers)


# =
# 2
# 4
# 6
# 8


# 3.22 Write a for loop that iterates over a list of numbers lst and prints the numbers in the
# list whose square is divisible by 8. For example, if lst is [2, 3, 4, 5, 6, 7, 8, 9],
# then the numbers 4 and 8 should be printed.

listOfNums = [2, 3, 4, 5, 6, 7, 8, 9]

for NumsDivByFour in listOfNums:
    if (NumsDivByFour ** 2) % 8 == 0:
        print(NumsDivByFour)


# =
# 4
# 8


# 3.23 Write for loops that use the function range() and print the following sequences:
# (a) 0 1
for i in range(0, 2):
    print(i)

# =
# 0
# 1

# (b) 0
for i in range(0, 1):
    print(i)

# = 0

# (c) 3 4 5 6
for i in range(3, 7):
    print(i)

# =
# 3
# 4
# 5
# 6

# (d) 1
for i in range(1, 2):
    print(i)

# = 1

# (e) 0 3
for i in range(0, 4, 3):
    print(i)

# =
# 0
# 3

# (f) 5 9 13 17 21
for i in range(5, 22, 4):
    print(i)

# =
# 5
# 9
# 13
# 17
# 21


# 3.24 Implement a program that requests a list of words from the user and then prints each word in the list that is not 'secret'.
#words: ['cia','secret','mi6','isi','secret']
secret = eval(input('Enter list of words: '))

for nonSecretWords in secret:
    if nonSecretWords != 'secret':
        print(nonSecretWords)


# =
# cia
# mi6
# isi


# 3.25 Implement a program that requests a list of student names from the user and prints those names that start with letters A through M.
# Enter list: ['Ellie', 'Steve', 'Sam', 'Owen', 'Gavin']

studentNames = eval(input('Enter Student List: '))

for studentsAToM in studentNames:
    if studentsAToM[0] < 'M':
        print(studentsAToM)


# =
# Ellie
# Gavin


# 3.26 Implement a program that requests a nonempty list from the user and prints on the screen a message giving the first and last element of the list.
# Enter a list: [3, 5, 7, 9]

numberList = eval(input('Enter a list: '))

print("The first list element is", numberList[0])
print("The last list element is", numberList[-1])

# or can solve


for firstAndLastNumbers in numberList:
    if firstAndLastNumbers == numberList[0]:
        print('The first list element is ' + str(numberList[0]))
    if firstAndLastNumbers == numberList[-1]:
        print('The last list element is ' + str(numberList[-1]))


# =
# The first list element is  3
# The last list element is  9


# 3.27 Implement a program that requests a positive integer n from the user and prints the first four multiples of n.
# Enter n: 5 and should get 0,5,10,15


nInteger = eval(input('Enter n: '))

for i in range(0, 4):
    'evaluates from 0 up to 4 and gives multiplies i from(0-3) by the nInteger which is 5'
    print(i * nInteger)


# =
# 0
# 5
# 10
# 15


# 3.28 Implement a program that requests an integer n from the user and prints on the screen the squares of all numbers from 0 up to, but not including, n.
# Enter n: 3 and should get 0,1,4

integer = eval(input('Enter n: '))

for i in range(0, integer):
    'evaluates from 0 up to but not including integer and i is squared from (0-2)'
    print(i ** 2)


# =
# 0
# 1
# 4


# 3.29 Implement a program that requests a positive integer n and prints on the screen all the
# positive divisors of n. Note: 0 is not a divisor of any integer, and n divides itself.
# Enter n: 49 ex: 1,7,49

aInteger = eval(input('Enter n: '))

for i in range(1, aInteger + 1):
    if aInteger % i == 0:  # no remainder, divdes perfectly
        print(i)


# =
# 1
# 7
# 49


# 3.30 Implement a program that requests four numbers (integer or floating-point) from the
# user. Your program should compute the average of the first three numbers and compare the
# average to the fourth number. If they are equal, your program should print 'Equal' on the
# screen.

# Enter first number: 4.5
# Enter second number: 3
# Enter third number: 3
# Enter last number: 3.5
# Equal

firstNum = eval(input('Enter first number: '))
secondNum = eval(input('Enter second number: '))
thirdNum = eval(input('Enter third number: '))
fourthNum = eval(input('Enter last number: '))


if (firstNum + secondNum + thirdNum) / 3 == fourthNum:
    print('Equal')


# = Equal


# 3.31 Implement a program that requests the user to enter the x and y coordinates (each
# between −10 and 10) of a dart and computes whether the dart has hit the dartboard, a circle
# with center (0, 0) and radius 8. If so, string It is in! should be printed on the screen.

# Enter x: 2.5
# Enter y: 4
# It is in!

x = eval(input('Enter x: '))
y = eval(input('Enter y: '))


r = 8
if ((x-a)**2) + ((y - b)**2) < (r ** 2):
    print('It is in!')  # = It is in!


# 3.32 Write a program that requests a positive four-digit integer from the user and prints its
# digits. You are not allowed to use the string data type operations to do this task. Your pro-
# gram should simply read the input as an integer and process it as an integer, using standard
# arithmetic operations (+, *, -, /, %, etc).

# Enter n: 1234
# 1
# 2
# 3
# 4

fourDigitInt = eval(input('Enter n: '))


x = 10
while (fourDigitInt/(10 * x) != 0):
    x = x * 10
    while (fourDigitInt > 0):
        print(int(fourDigitInt / x))
        fourDigitInt = fourDigitInt % x
        x = x / 10


# 3.33 Implement function reverse_string() that takes as input a three-letter string and
# returns the string with its characters reversed.
# reverse_string('abc')
# 'cba'
# reverse_string('dna')
# 'and'


def reverse_string(threeLettString):
    return threeLettString[::-1]


reverse_string('abc')  # = 'cba'
reverse_string('dna')  # = 'and'


# 3.34 Implement function pay() that takes as input two arguments: an hourly wage and the
# number of hours an employee worked in the last week. Your function should compute and
# return the employee’s pay. Any hours worked beyond 40 is overtime and should be paid at
# 1.5 times the regular hourly wage.
#pay(10, 35)
# 350
#pay(10, 45)
# 475.0


def pay(wage, hours):
    if hours <= 40:
        return wage * hours
    else:
        return (wage * hours) + ((hours - 40) * (wage * .5))


pay(10, 35)  # = 350
pay(10, 45)  # = 475.0


# 3.35 The probability of getting n heads in a row when tossing a fair coin n times is 2−n.
# Implement function prob() that takes a nonnegative integer n as input and returns the
# probability of n heads in a row when tossing a fair coin n times.
# prob(1)
# 0.5
# prob(2)
# 0.25

def prob(n):
    return 2 ** -abs(n)


prob(1)  # = 0.5
prob(2)  # = 0.25


# 3.36 Implement function reverse_int() that takes a three-digit integer as input and re-
# turns the integer obtained by reversing its digits. For example, if the input is 123, your
# function should return 321. You are not allowed to use the string data type operations to
# do this task. Your program should simply read the input as an integer and process it as an
# integer using operators such as // and %. You may assume that the input integer does not end with the 0 digit.
# reverse_int(123)
# 321
# reverse_int(908)
# 809


def reverse_int(num):
    rev = 0
    for i in range(3):
        rev *= 10
        rev += num % 10
        num //= 10
        return rev


reverse_int(123)


# 3.37 Implement function points() that takes as input four numbers x1, y1, x2, y2 that
# are the coordinates of two points (x1, y1) and (x2, y2) in the plane. Your function should compute:
# • The slope of the line going through the points, unless the line is vertical
# • The distance between the two points
# Your function should print the computed slope and distance in the following format. If the
# line is vertical, the value of the slope should be string 'infinity'. Note: Make sure you
# convert the slope and distance values to a string before printing them.


# using math.dist method

def points(x1, y1, x2, y2):
    firstPoint = (x1, y1)
    secondPoint = (x2, y2)
    if x1 != x2:
        slope = (y2-y1)/(x2-x1)
    else:
        slope = 'infinity'
        print('The slope is ' + str(slope) + ' and the distance is ' +
              str((math.dist(firstPoint, secondPoint))))


points(0, 0, 1, 1)
# = The slope is 1.0 and the distance is 1.4142135623730951
points(0, 0, 0, 1)
# = The slope is infinity and the distance is 1.0


# using math.sqrt method


def points(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if x1 != x2:
        slope = (y2 - y1) / (x2 - x1)
    else:
        slope = 'infinity'
    print("The slope is " + str(slope) +
          " and the distance is " + str(distance))


points(0, 0, 1, 1)
# = The slope is 1.0 and the distance is 1.4142135623730951
points(0, 0, 0, 1)
# = The slope is infinity and the distance is 1.0


# 3.38 Implement function abbreviation() that takes a day of the week as input and returns
# its two-letter abbreviation.
# abbreviation('Tuesday')
# 'Tu'

def abbreviation(Day):
    return Day[0:2]


abbreviation('Tuesday')


# 3.40 Implement function partition() that splits a list of soccer players into two groups.
# More precisely, it takes a list of first names (strings) as input and prints the names of those
# soccer players whose first name starts with a letter between and including A and M.
#partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])


def partition(soccer):
    for soccerAToM in soccer:
        if soccerAToM[0] >= 'A' and soccerAToM[0] <= 'M':
            print(soccerAToM)


partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])

# =
# Eleanor
# Evelyn
# Gavin


# 3.41 Write function lastF() that takes as input two strings of the form 'FirstName' and
# 'LastName', respectively, and returns a string of the form 'LastName, F.'. (Only the
# initial should be output for the first name.)


def lastF(FirstName, LastName):
    return LastName + ',' + ' ' + FirstName[0] + '.'


lastF('Albert', 'Camus')  # = 'Camus, A.'


# Implement function avg() that takes as input a list that contains lists of numbers. Each
# number list represents the grades a particular student received for a course. For example,
# here is an input list for a class of four students: [[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]


def avg(grades):
    for studentGradeSets in grades:
        print(sum(studentGradeSets) / len(studentGradeSets))


avg([[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]])


# =
# 90.0
# 60.0
# 87.0
# 11.0


# If the text contains both type of quotes, then the escape sequence \' or \" is used to indicate
# that a quote is not the string delimiter but is part of the string value. So, if we want to create
# the string value: I'm "sick".


fact = "I'm sick"
print(fact)  # = I'm sick


excuse = 'I\'m "sick"'
excuse  # = 'I\'m "sick"'
# need to use print function
# the print() function will interpret any escape sequence in the string and omit the string delimiters:
print(excuse)  # = I'm "sick"


# If the string is to represent multiline text, we have two choices. One is to use triple quotes,


poem = '''
To make a prairie it takes a clover and one bee, 
One clover, and a bee,
And revery.
The revery alone will do
If bees are few.
'''

print(poem)

# To make a prairie it takes a clover and one bee,
# One clover, and a bee,
# And revery.
# The revery alone will do
# f bees are few.


# \n stands in for a new line character.

poem2 = '\n To make a prairie it takes a clover and one bee, \n One clover, and a bee'

print(poem2)

# To make a prairie it takes a clover and one bee,
# One clover, and a bee


# Slicing Strings-1st number starts at and includes that index and ends before 2nd number in the slice

s = 'hello'
s[0]  # = 'h

s[0:2]  # = 'he'

s[3:4]  # = 'l'

s[-3:-1]  # = 'll' starts at index -3 and ends before index -1

s[-4:]


# If the slice we want starts at the first character of a string, we can drop the first index:

s[:3]  # = 'hel'
s[:-3]  # = 'he' starts at 0, never starts at -1. Can't begin a slice w/ a smaller neg # 1st and bigger neg # 2nd

# In order to obtain a slice that ends at the last character of a string, we must drop the second index:

s[-3:]  # = 'llo'
s[3:]  # = 'lo'


# Practice Problem 4.1
# Start by executing the assignment:
t = '0123456789'
# Now write expressions using string t and the indexing operator that evaluate to:
# (a) '234'
t[2:5]  # = '234'

# (b) '78'
t[7:9]  # = '78'

# (c) '1234567'
t[1:8]  # = '1234567'

# (d) '0123'
t[:4]  # = '0123'

# (e) '789'
t[7:]  # = '789'


# Slicing Lists
# A slice of a list is a list.
# when the indexing operator is applied to a list with two or more arguments, it will return a list.

pets = ['goldfish', 'cat', 'dog']

pets[:2]  # = ['goldfish', 'cat']
pets[-3:-1]  # = ['goldfish', 'cat']
pets[1:]  # = ['cat', 'dog']


# String Methods

#method: find()
# checks whether target is a substring of a variable. If so, it returns the
# index (of the first character) of the first occurrence of string target; otherwise, it returns -1.


message = '''This message is top secret and should not
be divulged to anyone without top secret clearance '''

message.find('top secret')  # = 16 index 16
message.find('message')  # = 5


#method: count()
# with string input argument target, returns the number of times target appears as a substring of a variable.

message.count('top secret')  # = 2
message.count('message')  # = 1


# method: replace(,)
# takes two string inputs, old and new, and outputs a copy of string with every occurrence of substring old replaced by string new.

message.replace('top', 'no')
# ='This message is no secret and should not\nbe divulged to anyone without no secret clearance '

# THIS IS A COPY ONLY.
# Instead, a copy of message, with appropriate substring replacements, got returned.
# Original string has not changed
# This string cannot be used later on because we have not assigned it a variable name.

print(message)
# = This message is top secret and should not
# be divulged to anyone without top secret clearance.


# Typically, the replace() method would be used in an assignment statement
#s.replace(old, new)
# A copy of string s in which every occurrence of substring old, when string s is scanned from left to
# right, is replaced by substring new

public = message.replace('top', 'no')
print(public)
# = This message is no secret and should not
# be divulged to anyone without no secret clearance


# Method capitalize()

message = 'top secret'
message.capitalize()  # = 'Top secret' --copy
print(message)  # = top secret


capitalMessage = message.capitalize()
print(capitalMessage)  # = Top secret


#Method: upper()

upperMessage = message.upper()
print(upperMessage)  # = TOP SECRET


# Method Split()
# called on a string in order to obtain a list of words in the string:
# Can use the blank spaces in the string to create word substrings that are put into a list and returned.

text = 'this is the text'.split()
print(text)  # = ['this', 'is', 'the', 'text']


# The method split() can also be called with a delimiter string as input: The delimiter string can be used in place of
# the blank space to break up the string.

x = '2;3;5;7;11;13'

xx = x.split(';')
print(xx)  # = ['2', '3', '5', '7', '11', '13']


#Method: translate()
# It is used to replace certain characters in a string with others based on a mapping of characters to characters.
# Such a mapping is constructed using a special type of string method that is called not by a string object but
# by the string class str itself:


table = str.maketrans('abcdef', 'uvwxyz')

'fad'.translate(table)  # = 'zux'

'desktop'.translate(table)  # = 'xysktop'


# 4.2
# Assuming that variable forecast has been assigned string

forecast = 'It will be a sunny day today'

# write Python statements corresponding to these assignments:
# (a) To variable count, the number of occurrences of string 'day' in string forecast.
count = forecast.count('day')
print(count)  # = 2

# (b) To variable weather, the index where substring 'sunny' starts.
weather = forecast.find('sunny')
print(weather)  # = 13

# (c) To variable change, a copy of forecast in which every occurrence of substring 'sunny' is replaced by 'cloudy'.
change = forecast.replace('sunny', 'cloudy')
print(change)  # = It will be a cloudy day today


# Function print() can take an arbitrary number of input objects, not necessarily of the same type.
# The values of the objects will be printed in the same line, and blank spaces (i.e., characters ' ') will be inserted between them:
n = 5

r = 5/3

print(n, r)  # = 5 1.6666666666666667

name = 'ida'
print(n, r, name)  # = 5 1.6666666666666667 ida

# If we want to insert semicolons between values instead of blank spaces, we can do that too. The print()
# function takes an optional separation argument sep, in addition to the objects to be printed:

print(n, r, name, sep=';')  # = 5;1.6666666666666667;ida

print(n, r, name, sep=', ')  # = 5,1.6666666666666667,ida

print(n, r, name, sep='\n')
# 5
# 1.6666666666666667
# ida

# 4.3
# Write a statement that prints the values of variables last, first, and middle in one line, separated by a horizontal tab character.
# the output should be: Smith John Paul
last = 'Smith'
first = 'John'
middle = 'Paul'

print(last, first, middle, sep='\t')  # = Smith   John    Paul


for name in ['Joe', 'Sam', 'Tim', 'Ann']:
    print(name)

# Joe
# Sam
# Tim
# Ann

# end= print() function
# is printed after all the arguments have been printed.
# the default string '\n', the new line character, is printed instead if argument end= is not there.

for name in ['Joe', 'Sam', 'Tim', 'Ann']:
    print(name, end='! ')

# Joe! Sam! Tim! Ann! >>>


# 4.4
# Write function even() that takes a positive integer n as input and prints on the screen all
# numbers between, and including, 2 and n divisible by 2 or by 3, using this output format:

def even(n):
    for numbers in range(2, n+1):
        if numbers % 2 == 0 or numbers % 3 == 0:
            print(numbers, end=' , ')


even(17)
# = 2 , 3 , 4 , 6 , 8 , 9 , 10 , 12 , 14 , 15 , 16 , >>>


# String Method Format

weekday = 'Wednesday'
month = 'March'
day = 10
year = 2010
hour = 11
minute = 45
second = 33


# Wednesday, March 10, 2010 at 11:45:33


# Too tedious and error prone.

print(weekday + ', ' + month + ' ' + str(day) + ', ' + str(year) +
      ' at ' + str(hour) + ':' + str(minute) + ':' + str(second))
# = Wednesday, March 10, 2010 at 11:45:33


# The format() string method is invoked on a string that represents the format of the output.
# The arguments of the format() function are the objects to be printed.

'{0}:{1}:{2}'.format(hour, minute, second)  # = '11:45:33'

# The objects to be printed (hour, minute, and second) are arguments of the format() method.
# The string invoking the format() function—that is, the string '{0}:{1}:{2}'— is the format string
# All the characters outside the curly braces—that is, the two colons (':')—are going to be printed as is.
# The curly braces {0}, {1}, and {2} are placeholders where the objects will be printed.


# The default, when no explicit number is given inside the curly braces, is to assign the
# placeholder (from left to right) from 1st-last argument of the format() function.

'{}:{}:{}'.format(hour, minute, second)  # = '11:45:33'


# = Wednesday, March 10, 2010 at 11:45:33


print('{}, {} {}, {} at {}:{}:{}'.format(
    weekday, month, day, year, hour, minute, second))


# 4.5
# Assume variables first, last, street, number, city, state, zipcode have already been assigned. Write a print statement that creates a mailing label:

# John Doe
# 123 Main Street
# AnyCity, AS 09876


first = 'John'
last = 'Doe'
street = 'Main Street'
number = 123
city = 'AnyCity'
state = 'AS'
zipcode = '09876'

print('{} {} \n{} {} \n{}, {} {}'.format(
    first, last, number, street, city, state, zipcode))


# =John Doe
# 123 Main Street
# AnyCity, AS 09876


# Lining Up Data in Columns

for i in range(1, 13):
    print(i, i**2, i**3, 2**i, sep='    ')


# The problem is that a fixed-size separator pushes entries farther to the right as the number of digits in the entry increases.
# =
# 1    1    1    2
# 2    4    8    4
# 3    9    27    8
# 4    16    64    16
# 5    25    125    32
# 6    36    216    64
# 7    49    343    128
# 8    64    512    256
# 9    81    729    512
# 10    100    1000    1024
# 11    121    1331    2048
# 12    144    1728    4096


# We can specify the (minimum) field width with a decimal integer defining the number of character positions reserved for the value.

'{0:3},{1:5}'.format(12, 354)
# =
#' 12,  354'

# first # before : is the argument
# Everything after the ':' specifies the formatting of the value.
# In this case, 3 indicates that the width of the placeholder should be 3.
# Since 12 is a two-digit number, an extra blank space is added in front.

# When the field width is larger than the number of digits, the default is to right-justify—that is, push the number value to the right.
# Strings are left-justified.

first = 'Bill'
last = 'Gates'
'{:10}{:10}'.format(first, last)
'Bill      Gates     '


# Type Explanation
# b Outputs the number in binary
# c Outputs the Unicode character corresponding to the integer value
# d Outputs the number in decimal notation (default)
# o Outputs the number in base 8
# x Outputs the number in base 16, using lowercase letters for the digits above 9
# X Outputs the number in base 16, using uppercase letters for the digits above 9


# The precision is a decimal number that specifies how many digits should be displayed
# before and after the decimal point of a floating-point value.
# It follows the field width and a period separates them.

'{:8.4}'.format(1000/3)
# = '   333.3'


'{:15.6}'.format(1000/3)
# = '        333.333'

# Before . is for how much width is for the placeholder
# After . is for how many #'s you want


# Type Explanation
# b Outputs the number in binary
# c Outputs the Unicode character corresponding to the integer value
# d Outputs the number in decimal notation (default)
# o Outputs the number in base 8
# x Outputs the number in base 16, using lowercase letters for the digits above 9
# X Outputs the number in base 16, using uppercase letters for the digits above 9


n = 10

'{:b}'.format(n)  # = '1010'
'{:c}'.format(n)  # = '\n'
'{:d}'.format(n)  # = '10'
'{:x}'.format(n)  # = 'a'


# f and e are options for floating-point values
# reserves a minimum width of 6 with exactly two digits past the decimal point for a floating-point value represented as a fixed-point number.

'{:6.2f}'.format(5/3)  # = '  1.67'


def growthRates(n):
    print('i i**2 i**3 2**i')
    formatStr = '{0:2d} {1:6d} {2:6d} {3:6d}'
    for i in range(1, n+1):
        print(formatStr.format(i, i**2, i**3, 2**i))


growthRates(12)


# i i**2 i**3 2**i
# 1      1      1      2
# 2      4      8      4
# 3      9     27      8
# 4     16     64     16
# 5     25    125     32
# 6     36    216     64
# 7     49    343    128
# 8     64    512    256
# 9     81    729    512
# 10    100   1000   1024
# 11    121   1331   2048
# 12    144   1728   4096


# 4.6
# Implement function roster() that takes a list containing student information and prints
# out a roster, as shown below. The student information, consisting of the student’s last name,
# first name, class, and average course grade, will be stored in that order in a list. Therefore,
# the input list is a list of lists. Make sure the roster printed out has 10 slots for every string
# value and 8 for the grade, including 2 slots for the decimal part.


students = []
students.append(['DeMoines', 'Jim', 'Sophomore', 3.45])
students.append(['Pierre', 'Sophie', 'Sophomore', 4.0])
students.append(['Columbus', 'Maria', 'Senior', 2.5])
students.append(['Phoenix', 'River', 'Junior', 2.45])
students.append(['Olympis', 'Edgar', 'Junior', 3.99])


def roster(students):
    print('this is the roster ')

    for student in students:
        print('{0:10} {1:10} {2:10} {3:8.2}'.format(
            student[0], student[1], student[2], student[3]))


roster(students)


# = lastName firstName class GPA
# DeMoines   Jim        Sophomore       3.5
# Pierre     Sophie     Sophomore       4.0
# Columbus   Maria      Senior          2.5
# Phoenix    River      Junior          2.5
# Olympis    Edgar      Junior          4.0


# Getting and Formatting the Date and Time


# time()
# The time() function returns the time in seconds


time.time()


# You can check the epoch for your computer system using another function that returns
# the time in a format very different from time():

time.gmtime(0)
# = time.struct_time(tm_year=1970, tm_mon=1, tm_mday=1, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=3, tm_yday=1, tm_isdst=0)


# The type, time.struct_time, of the object returned by function gmtime() is a tuple-like type.


# If no argument is given to the function gmtime(), it will return the current UTC time.
time.gmtime()
# = time.struct_time(tm_year=2023, tm_mon=3, tm_mday=9, tm_hour=3, tm_min=55, tm_sec=57, tm_wday=3, tm_yday=68, tm_isdst=0)


# The related function localtime() returns the local time zone current time instead:
time.localtime()
# = time.struct_time(tm_year=2023, tm_mon=3, tm_mday=8, tm_hour=21, tm_min=58, tm_sec=23, tm_wday=2, tm_yday=67, tm_isdst=0)


# Module time provides a formatting function strftime() that outputs time in the desired format.
#   This function takes a format string and the time returned by gmtime() or localtime() and outputs the
#   time in a format described by the format string.


# Directive Output
# %a Abbreviated weekday name
# %A Full weekday name
# %b Abbreviated month name
# %B Full month name
# %d The day of the month as a decimal number between 01 and 31
# %H The hours as a number between 00 and 23
# %I The hours as a number between 01 and 12
# %M The minutes as a number between 00 and 59
# %p AM or PM
# %S Seconds as a number between 00 and 61
# %y Year without century as a number between 00 and 99
# %Y Year as a decimal number
# %Z Time zone name


time.strftime('%A %b/%d/%y %I:%M %p', time.localtime())
# = 'Wednesday Mar/08/23 10:21 PM'


# 4.7
# Start by setting t to be the local time 1, 500, 000, 000 seconds from the start of January 1, 1970 UTC:
t = time.localtime(1500000000)


# Construct the next strings by using the string time format function strftime():
# (a) 'Thursday, July 13 2017'

time.strftime('%A, %B %d %Y', t)
# = 'Thursday, July 13 2017'

# (b) '09:40 PM Central Daylight Time on 07/13/2017'

time.strftime('%I:%M %p Central Daylight Time on %m/%d/%Y', t)

# (c) 'I will meet you on Thu July 13 at 09:40 PM.'

time.strftime('I will meet you on %a %B %d at %I:%M %p.', t)


# Files
# is a sequence of bytes stored on a secondary memory device, such as a disk drive.

# Text files like a text document or spreadsheet, an HTML file, or a Python module.
# Such contain a sequence of characters that are encoded using some encoding (ASCII, utf-8, etc.).

# binary files-they are just a sequence of bytes and there is no encoding like an executable application (like
# python.exe), an image, or an audio file.

# All files are managed by the file system.

# File system-is the component of a computer system that organizes files and provides
# ways to create, access, and modify files.


# Opening and Closing a File
# Processing a file consists of these three steps:
# 1. Opening a file for reading or writing
# 2. Reading from the file and/or writing to the file
# 3. Closing the file


# The built-in function open() is used to open a file

# The function open() takes three string arguments: a file name and, optionally, a mode and an encoding;


# The mode is a string that specifies how we will interact with the opened file.

infile = open('README.MD', 'r')

# If mode is missing, the default is r.

infile = open('README.md')

infile.read(1)  # = 'T'
# the cursor will move and point to the next character,
infile.read(5)  # = 'he 3 '


# The function readline() will read characters from the file up to the end of the line (i.e.,
infile.readline()  # = 'lines in this file end with the new line character.\n'

# Finally, we use the read() function without arguments to read the remainder of the file:
infile.read()  # = '\nThere is a blank line above this line.\n'


# To close the opened file that infile refers to, you just do:
infile.close()


# function numChars(), which takes the name of a file as input and returns the number of characters in the file. We use the read() function
# to read the file content into a string:


def numChars(fileName):
    'returns the # of characters in the file filename'
    infile = open(fileName, 'r')
    content = infile.read()
    infile.close

    return len(content)


numChars('README.MD')
# = 98


# 4.8
# Write function stringCount() that takes two string inputs—a file name and a target string—
# and returns the number of occurrences of the target string in the file.

def stringCount(fileName, target):
    infile = open(fileName)
    content = infile.read()
    infile.close
    return content.count(target)


stringCount('README.MD', 'line')  # = 4


def numWords(fileName):
    'returns the number of words in file fileName'
    infile = open(fileName, 'r')
    content = infile.read()  # read the file into a string
    infile.close()

    wordList = content.split()  # split file into list of words
    print(wordList)
    return len(wordList)


numWords('README.MD')

# =
# ['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with', 'the', 'new', 'line', 'character.',
#   'There', 'is', 'a', 'blank', 'line', 'above', 'this', 'line.']
# 20

# 4.9
# Write function words() that takes one input argument—a file name—and returns the list
# of actual words (without punctuation symbols !,.:;?) in the file.


def words(fileName):
    'returns the number of words in file fileName'
    infile = open(fileName, 'r')
    content = infile.read()  # read the file into a string
    infile.close()

    'or you can have 6 spaces in between('      ')the first 2 maketrans arguments must have equal length'
    wOutPuncSymbols = str.maketrans('!,.:;?', 6*' ')
    content = content.translate(wOutPuncSymbols)
    return content.split()


words('README.MD')


# =
# ['The', '3', 'lines', 'in', 'this', 'file', 'end', 'with', 'the', 'new', 'line', 'character',
# 'There', 'is', 'a', 'blank', 'line', 'above', 'this', 'line']


# Sometimes a text file needs to be processed line by line.

def numLines(fileName):
    'returns the number of lines in file fileName'
    infile = open(fileName, 'r')   # open the file and read it
    lineList = infile.readlines()  # into a list of lines
    infile.close()

    print(lineList)  # print list of lines
    return len(lineList)


numLines('README.MD')

# =
# ['The 3 lines in this file end with the new line character.\n',
# '\n', 'There is a blank line above this line.\n']
# 3


# If the file is large, a better approach would be to process the file line by line; that way we avoid having the
# whole file in main memory. Python supports iteration over lines of a file object.


infile = open('README.MD')
for lines in infile:
    print(lines, end='')


# In every iteration of the for loop, the variable line will refer to the next line of the file.

# =
# The 3 lines in this file end with the new line character.
#
# 3 There is a blank line above this line.


# 4.10
# Implement function myGrep() that takes as input two strings, a file name and a target string,
# and prints every line of the file that contains the target string as a substring.

def myGrep(fileName, target):
    'prints every line of file fileName containing string target'
    infile = open(fileName, 'r')
    for line in infile:
        if target in line:
            print(line, end='')


myGrep('README.MD', 'line')


# In order to write to a text file, the file must be opened for writing:

outfile = open('test.txt', 'w')

# If there is no file test.txt in the current working directory, the open() function will create it.
# If a file text.txt exists, its content will be erased.
# In both cases, the cursor will point to the beginning of the (empty) file.
# (If we wanted to add more content to the (existing) file, we would use the mode 'a' instead of 'w'.)


# Once a file is opened for writing, function write() is used to write strings to it.
# It will write the string starting at the cursor position.


# The value returned is the number of characters written/added to the file.

outfile.write('T')
# = 1

outfile.write('his is the first line.')
# = 22


outfile.write(' Still the first line...\n')
# = 25

# New line?

outfile.write('Now we are in the second line. \n')
# = 32
