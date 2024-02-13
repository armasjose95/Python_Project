"""import time  # time module
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
# 1
# 4
# 7
# 10
# 13
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


# To write something other than a string, it needs to be converted to a string first:
outfile.write('Non sting value like '+str(5)+' must be converted first. \n')
# 50

# Here is where the string format() function is helpful. To illustrate the benefit of using
# string formatting, we print an exact copy of the previous line using string formatting:

outfile.write('Non string value like {} must be converted first. \n'.format(5))
# 50


# When a file is opened for writing, a buffer is created in memory. All writes to the file
# are really writes to this buffer; nothing is written onto the disk, at least not just yet.
# no file is created in the file system until the file and the writes are flushed.
# The close() function will flush writes from the buffer to the file on disk before closing,
# so it is critical not to forget to close the file. You can also flush the writes without
# closing the file using the .flush() function:


outfile.close()


# 4.11
# (3+4)
# if x == 5:
# print('hello')
# lst=[4,5,6]
# print(lst)
# for i in range(0,100,10):
# print(i)

# 0
# 10
# 20
# 30
# 40
# 50
# 60
# 70
# 80
# 90


# Syntax errors are errors that are due to the incorrect format of a Python statement.
# These errors occur while the statement or program is being translated to machine language and before it is being executed.


# Built-In Exceptions
# Errors occurs because the statement execution got into an invalid state.
# When this happens, we say that the Python interpreter raises an exception.
# What this means is that an object gets created, and this object contains all the information relevant to the error.


# Users typically hit Ctrl - C to interrupt a program


# 4.12 Start by running, in the interactive shell, this assignment statement:
# >>> s = 'abcdefghijklmnopqrstuvwxyz'
# Now write expressions using string s and the indexing operator that evaluate to 'bcd',
# 'abc', 'defghijklmnopqrstuvwx', 'wxy', and 'wxyz'.

s = 'abcdefghijklmnopqrstuvwxyz'

s[1:4]  # = 'bcd'
s[:3]  # = 'abc'
s[3:24]  # = 'defghijklmnopqrstuvwx'
s[22:25]  # = 'wxy'
s[22:]  # = 'wxyz'


# 4.13 Let string s be defined as:
s = 'abcdefghijklmnopqrstuvwxyz'

# Write Python Boolean expressions that correspond to these propositions:
# (a) The slice consisting of the second and third character of s is 'bc'.

s[1:3]  # = 'bc'

# (b) The slice consisting of the first 14 characters of s is 'abcdefghijklmn'.

s[:14]  # = 'abcdefghijklmn'

# (c) The slice of s excluding the first 14 characters is 'opqrstuvwxyz'.

s[14:]  # = 'opqrstuvwxyz'

# (d) The slice of s excluding the first and last characters is 'bcdefghijklmnopqrstuvw'.
s[1:23]  # = 'bcdefghijklmnopqrstuvw'


# 4.14 Translate each part into a Python statement:
# (a) Assign to variable log the next string, which happens to be a fragment of a log of a request
# for a text file from a web server: 128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"


log = "128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "
log += "GET /docs/test.txt HTTP/1.0"
print(log)
# = 128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] GET /docs/test.txt HTTP/1.0


# (b) Assign to variable address the substring of log that ends before the first blank space in log,
# using the string method split() and the indexing operator.

address = log.split()[0]
print(address)
# = 128.0.0.1


# (c) Assign to variable date the splice of string log containing the date (12/Feb ... -6000), using the indexing operator on string log.

date = log[15:41]
print(date)

# = 12/Feb/2011:10:31:08 -0600


# 4.15 For each of the below string values of s, write the expression involving s and the string methods split() that evaluates
# to list: ['10', '20', '30', '40', '50', '60']
# (a) s = '10 20 30 40 50 60'

s = '10 20 30 40 50 60'
s.split()
# = ['10', '20', '30', '40', '50', '60']

# (b) s = '10,20,30,40,50,60'

s = '10,20,30,40,50,60'
s.split(',')
# = ['10', '20', '30', '40', '50', '60']


# (c) s = '10&20&30&40&50&60'

s = '10&20&30&40&50&60'
s.split('&')
# = ['10', '20', '30', '40', '50', '60']

# (d) s = '10 - 20 - 30 - 40 - 50 - 60'

s = '10 - 20 - 30 - 40 - 50 - 60'
s.split(' - ')
# = ['10', '20', '30', '40', '50', '60']


# 4.16 Implement a program that requests three words (strings) from the user. Your program
# should print Boolean value True if the words were entered in dictionary order; otherwise nothing is printed.

# Enter first word: bass
# Enter second word: salmon
# Enter third word: whitefish
# True


first = input("Enter first word: ")
second = input("Enter second word: ")
last = input("Enter third word: ")

if first < second < last:
    print("True")

# = True



#4.17 Translate each part into a Python statement using appropriate string methods:
#(a) Assign to variable message the string 'The secret of this message is that it is secret.'

message = 'The secret of this message is that it is secret.'
print(message)

#(b) Assign to variable length the length of string message, using operator len().

length = len(message)
print(length)
# = 48

#(c) Assign to variable count the number of times the substring 'secret' appears in string message, using string method count().

count = message.count('secret')
print(count) 
# = 2

#(d)Assign to variable censored a copy of string message with every occurrence of substring 'secret' replaced by 'xxxxxx', using string method replace().

censored = message.replace('secret', 'xxxxxx')
print(censored)
# = The xxxxxx of this message is that it is xxxxxx.



#4.18 Suppose variable s has been assigned in this way:

s = '''It was the best of times, it was the worst of times; it
was the age of wisdom, it was the age of foolishness; it was the
epoch of belief, it was the epoch of incredulity; it was ... '''

#(The beginning of A Tale of Two Cities by Charles Dickens.) Then do the following, in order:

#(a) Write a sequence of statements that produce a copy of s, named newS, in which characters ., ,, ;, and \n have been replaced by blank spaces.

newS = s.replace('.', ' ')
newS = newS.replace(',', ' ')
newS = newS.replace(';', ' ')
print(newS)
# = It was the best of times  it was the worst of times  it
#was the age of wisdom  it was the age of foolishness  it was the
#epoch of belief  it was the epoch of incredulity  it was  


#(b) Remove leading and trailing blank spaces in newS (and name the new string newS).

newS = newS.strip()
#newS = newS.replace(' ', '') -- other way to solve this
print(newS)

#(c) Make all the characters in newS lowercase (and name the new string newS).

newS = newS.lower()
print(newS)

#(d) Compute the number of occurrences in newS of string 'it was'.

newS.count('it was')
# = 6

#(e) Change every occurrence of was to is (and name the new string newS).

newS = newS.replace('was','is')
print(newS)

#(f) Split newS into a list of words and name the list listS.

listS = newS.split()
print(listS)

# = ['it', 'is', 'the', 'best', 'of', 'times', 'it', 'is', 'the', 'worst', 'of', 'times', 'it', 'is', 'the', 'age', 'of', 'wisdom', 'it', 'is', 
# 'the', 'age', 'of', 'foolishness', 'it', 'is', 'the', 'epoch', 'of', 'belief', 'it', 'is', 'the', 'epoch', 'of', 'incredulity', 'it', 'is']"""

""" 
# 4.19 Write Python statements that print the next formatted outputs using the already assigned variables first, middle, and last:

first = 'Marlena'
last = 'Sigel'
middle = 'Mae'


# (a) Sigel, Marlena Mae


# print(last, first, middle, sep='\t')  # = Smith   John    Paul

print(last + "," + " " + first + " " + middle)
# or the more proper way to write:

print("{}, {} {}".format(last, first, middle))
# = Sigel, Marlena Mae


# (b) Sigel, Marlena M.

print(last + "," + " " + first + " " + middle[0] + ".")
# or the more proper way to write:

print("{}, {} {}".format(last, first, middle[0]))
# = Sigel, Marlena M

# (c) Marlena M. Sigel

print(first + " " + middle[0] + "." + " " + last)
# or the more proper way to write:

print("{} {}. {}".format(first, middle[0], last))
# = Marlena M. Sigel

# (d) M. M. Sigel

print(first[0] + "." + " " + middle[0] + "." + " " + last)
# or the more proper way to write:

print("{}. {}. {}".format(first[0], middle[0], last))
# = M. M. Sigel

# (e) Sigel, M.

print(last + "," + " " + first[0] + ".")
# or the more proper way to write:

print("{}, {}.".format(last, first[0]))
# = Sigel, M.
"""
"""

# 4.20 Given string values for the sender, recipient, and subject of an email, write a string
# format expression that uses variables sender, recipient, and subject and that prints as shown here:
# >>> sender = 'tim@abc.com'
# >>> recipient = 'tom@xyz.org'
# >>> subject = 'Hello!'
# >>> print(???) #fill in
#From: tim@abc.com
#To: tom@xyz.org
# Subject: Hello!

sender = 'tim@abc.com'
recipient = 'tom@xyz.org'
subject = 'Hello!'

print("From: {}\nTo: {}\nSubject: {}".format(sender, recipient, subject))

# =
#From: tim@abc.com
#To: tom@xyz.org
# Subject: Hello!


# 4.22 Write a function month() that takes a number between 1 and 12 as input and returns
# the three-character abbreviation of the corresponding month. Do this without using an if
# statement, just string operations. Hint: Use a string to store the abbreviations in order.

# >>> month(1)
# 'Jan'
# >>> month(11)
# 'Nov'



def month(num):
    months = "JanFebMarAprMayJunJulAugSepOctNovDec"
    return months[(3 * (num - 1)): (3 * num)]


month(1)
# = 'Jan'

month(11)
# =  'Nov'
"""

"""
# 4.23 Write a function average() that takes no input but requests that the user enter a
# sentence. Your function should return the average length of a word in the sentence.
# >>> average()
# Enter a sentence: A sample sentence
# 5.0


def average():
    sentence = input('Enter a sentence: ').split()
    return sum(len(word) for word in sentence) / len(sentence)


average()
# = 5


# 4.24 Implement function cheer() that takes as input a team name (as a string) and prints a cheer as shown:
# >>> cheer('Huskies')
# How do you spell winner?
# I know, I know!
# H U S K I E S !
# And that's how you spell winner!
# Go Huskies!

"""
"""

def cheer(team):
    team = input('Enter a team name: ')
    if team == 'Huskies':
        print('How do you spell winner?\nI know, I know!\nH U S K I E S !\nAnd that\'s how you spell winner!\nGo Huskies!')


cheer('Huskies')


# or can be done this way

def cheer(team_name):
    print("How do you spell winner?")
    print("I know, I know!")
    print(" ".join(team_name.upper()) + " !")
    print("And that's how you spell winner!")
    print("Go {}!".format(team_name))


cheer('Huskies')
"""
"""

# 4.25 Write function vowelCount() that takes a string as input and counts and prints the number of occurrences of vowels in the string.
# >>> vowelCount('Le Tour de France')
# a, e, i, o, and u appear, respectively, 1, 3, 0, 1, 1 times.


def vowelCount(text):
    text = text.upper()
    numA = text.count('A')
    numE = text.count('E')
    numI = text.count('I')
    numO = text.count('O')
    numU = text.count('U')
    print('a, e, i, o, and u appear, respectively, {}, {}, {}, {}, {} times.'.format(
        numA, numE, numI, numO, numU))


vowelCount('Le Tour de France')
# = a, e, i, o, and u appear, respectively, 1, 3, 0, 1, 1 times.


# 4.26 The cryptography function crypto() takes as input a string (i.e., the name of a file in
# the current directory). The function should print the file on the screen with this modification:
# Every occurrence of string 'secret' in the file should be replaced with string 'xxxxxx'.

# File: crypto.txt >>> crypto('crypto.txt')

# I will tell you my xxxxxx. But first, I have to explain
# why it is a xxxxxx.
# And that is all I will tell you about my xxxxxx.


def crypto(filename):
    infile = open(filename, 'r')
    content = infile.read()
    content = content.replace('secret', 'xxxxxx')
    infile.close()
    print(content)


crypto('crypto.txt')


# 4.27 Write a function fcopy() that takes as input two file names (as strings) and copies the content of the first file into the second.
# File: example.txt >>> fcopy('example.txt','output.txt')
# >>> open('output.txt').read()
# 'The 3 lines in this file end with the new line character.\n\n
# There is a blank line above this line.\n'


def fcopy(file1, file2):
    infile = open(file1, 'r')
    outfile = open(file2, 'w')
    content = infile.read()
    outfile.write(content)
    infile.close()
    outfile.close()


fcopy('example.txt', 'output.txt')


# 4.28 Implement function links() that takes as input the name of an HTML file (as a
# string) and returns the number of hyperlinks in that file. To do this you will assume that
# each hyperlink appears in an anchor tag. You also need to know that every anchor tag ends with the substring </a>.
# Test your code on HTML file twolinks.html or any HTML file downloaded from the web into the folder where your program is.
# >>> links('twolinks.html') File: twolinks.html
# 2

def links(htmlFile):
    hyperlink = open(htmlFile, 'r')
    content = hyperlink.read()
    hyperlink.close()
    return hyperlink.count("<\a>")


links('twolinks.html')


# 4.29 Write a function stats() that takes one input argument: the name of a text file. The
# function should print, on the screen, the number of lines, words, and characters in the file;
# your function should open the file only once.


def stats(file):
    infile = open(file, 'r')
    content = infile.read()
    lines = content.count('\n') + 1
    words = len(content.split())
    characters = len(content)
    infile.close

    print(f"line count: {lines}")
    print(f"word count: {words}")
    print(f"character count: {characters}")


stats('example.txt')


# Three-Way (and More!) Decisions
# The most general format of the Python if statement is the multiway (three or more) decision control structure:
# if <condition1>:
#   <indented code block 1>
# elif <condition2>:
#   <indented code block 2>
# elif <condition3>:
#   <indented code block 3>
# else: # there could be more elif statements
#   <indented code block last>
# <non-indented statement>


def temperature(t):
    'prints message based on temperature value t'
    if t > 86:
        print('It is hot!')
    elif t > 32:
        print('It is cool.')
    else:  # t<=32
        print('It is freezing!')


temperature(90)


# 5.2 Implement function myBMI() that takes as input a person’s height (in inches) and weight
# (in pounds) and computes the person’s Body Mass Index (BMI). The BMI formula is:
# bmi = weight ∗ 703 / height^2

def myBMI(height, weight):
    bmi = (weight*703) / (height**2)
    if bmi < 18.5:
        print('Underweight')
    elif bmi < 25:
        print('Normal')
    else:
        print('Overweight')


myBMI(68, 190)


#Iteration loop pattern

l = ['cat', 'dog', 'chicken']

for animal in l:
    print(animal)

# =
#cat
#dog
#chicken

s = 'cupcake'

for c in s:
    if c in 'aeiou':
        print(c)

# = 
#u
#a
#e

#Iteration is over a list but over the lines of the file-like object infile.

infile = open('test.txt', 'r')

for line in infile:
    print(line, end='')



# Loop Pattern: Counter Loop

for i in range(10):
    print(i, end=' ')

# = 0 1 2 3 4 5 6 7 8 9


n = 10
for i in range(n):
    if i % 2 == 0:
        print(i, end=' ')
        
# = 0 2 4 6 8 


# 5.2
# Write a function named powers() that takes a positive integer n as input and prints, on the screen, all the powers of 2 from 2^1 to 2^n


def powers(n):
    for i in range(1, n+1):
        print(2**i, end=' ')


powers(6)
# = 2 4 8 16 32 64


def powers(n):
    for i in range():
        print(2**i, end=' ')


powers(6)


pets = ['cat', 'dog', 'fish', 'bird']

# for animal in pets:
#    print(animal)


# Instead of iterating through the items of list pets, we could also iterate through the indexes of list pets and achieve the same result:


for i in range(len(pets)):
    print(pets[i])


# See if a variable list is sorted in increasing fashion?
# we do not need to compare the last list item with the “next item” in the list. What we need to do is shorten the range over which
# the for loop iterates by 1.


def sorted(lst):
    'returns True if sequence lst is increasing, false otherwise'
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
        return True


sorted([1, 30])  # = true
sorted([5, 1])  # = false


# = 5.3
# = Write function arithmetic() that takes a list of integers as input and returns True if they form an arithmetic sequence.
# (A sequence of integers is an arithmetic sequence if the difference between consecutive items of the list is always the same.)


def arithmetic(sequence):
    '''returns True if list lst contains an arithmetic sequence, False otherwise'''
    if len(sequence) < 2:  # a sequence of length < 2 is arithmetic
        return True
        # checking that difference between successive items is equal to the difference between the first two numbers
    diff = sequence[1] - sequence[0]
    for i in range(1, len(sequence)):
        if sequence[i] - sequence[i - 1] != diff:
            return False
    return True


arithmetic([3, 6, 9, 12, 15])  # true
arithmetic([3, 6, 9, 11, 14])  # false
arithmetic([3])  # true


# Loop Pattern: Accumulator Loop
# A common pattern in loops is to accumulate “something” in every iteration of the loop.

numList = [3, 2, 7, -1, 9]
mySum = 0               # initializing the accumulator
for num in numList:
    mySum = mySum + num  # adding to the accumulator


mySum  # = 20            # the sum of numbers in numList


# shortcut

numList = [3, 2, 7, -1, 9]
mySum = 0
for num in numList:
    mySum += num

mySum  # = 20


numList = [3, 2, 7, -1, 9]
myProd = 1
for num in numList:
    myProd = myProd * num

myProd  # = -378


# 5.4
# Implement function factorial() that takes as input a nonnegative integer and returns its
# factorial. The factorial of a nonnegative integer n, denoted n!, is defined in this way:


def factorial(n):
    'returns n!'
    res = 1
    # start at 2 because 1* any # is just itself, no need to do the last multiplication
    for i in range(2, n+1):
        res *= i
        'same as below'
        #res = res * i
    return res


factorial(0)  # = 1
factorial(3)  # = 6
factorial(5)  # = 120


# Write a function acronym() that takes a phrase (i.e., a string) as input and then returns the
# acronym for that phrase. Note: The acronym should be all uppercase, even if the words in the phrase are not capitalized.

# upper
# [0]+[1]

def acronym(string):
    # add first letter
    myAcr = string[0]
    # iterate over string
    for i in range(1, len(string)):
        if string[i-1] == ' ':
            # add letter next to space and capitalizes
            myAcr = myAcr + string[i].upper()
    #myAcr = myAcr.upper()
    return myAcr


acronym('Random access memory')  # ='RAM'

# OR CAN BE DONE THIS WAY


def acronym(phrase):
    'returns the acronym of the input string phrase'
    # splits phrase into a list of words
    words = phrase.split()
    # accumulate first character, as an uppercase, of every word
    res = ''
    for w in words:
        res = res + w[0].upper()
    return res


acronym('Random access memory')


# 5.6
# Write function divisors() that takes a positive integer n as input and returns the list of all positive divisors of n.


def divisors(n):
    res = []
    for i in range(1, n+1):
        if n % i == 0:
            res.append(i)
    return res


divisors(1)  # = 1
divisors(6)  # = [1,2,6]
divisors(11)  # = [1,11]


# Loop Patterns: Nested Loop
# a loop statement contained inside another loop statement.
# A nested loop pattern may contain more than two nested loops.
# Note that we needed to use a variable name in the outer for loop different from the variable name in the inner for loop (i).

# Goal:
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4

n = 5
for i in range(n):
    print(i, end=' ')

# = 0 1 2 3 4


for j in range(n):              # outer loop iterates 5 times
    for i in range(n):          # inner loop prints 0 1 2 3 4
        print(i, end=' ')

# = 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4 0 1 2 3 4


def nested(n):
    'prints n lines each containing values 0 1 2 ... n-1'
    for j in range(n):              # repeat n times:
        for i in range(n):          # print 0, 1, ..., n-1
            print(i, end=' ')
        print()                     # move cursor to next line


nested(5)
# =
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4
# 0 1 2 3 4

i = 0
for i in range(i, 11):
    if i < 11:
        i = i + 1
    print(i, end=' ')


# 5.7
# Write a function xmult() that takes two lists of integers as input and returns a list containing
# all products of integers from the first list with the integers from the second list.


def xmult(firList, secList):
    res = []
    for j in firList:
        for i in secList:
            res.append(j*i)
    return res


xmult([2], [1, 5])  # = [2, 10]
xmult([2, 3], [1, 5])  # = [2, 10, 3, 15]
xmult([3, 4, 1], [2, 0])  # = [6, 0, 8, 0, 2, 0]


def nested2(n):
    'prints n lines 0 1 2 ... j for j = 0, 1, ..., n-1'
    for j in range(n):          # j = 0, 1, ..., n-1
        for i in range(j+1):    # print 0 1 2 ... j
            print(i, end=' ')
        print()                 # move to next line


nested2(5)

# =
# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4


# 5.8

# One way to sort a list of n different numbers in increasing order is to execute n − 1 passes
# over the numbers in the list. Each pass compares all adjacent numbers in the list and swaps
# them if they are out of order. At the end of the first pass, the largest item will be the last in
# the list (at index n−1). Therefore, the second pass can stop before reaching the last element,
# as it is already in the right position; the second pass will place the second largest item in the
# next to last position. In general, pass i will compare pairs at indexes 0 and 1, 1 and 2, 2 and
# 3, . . . , and i − 1 and i; at the end of the pass, the ith largest item will be at index n − i.
# Therefore, after pass n − 1, the list will be in increasing order.
# Write a function bubbleSort() that takes a list of numbers as input and sorts the list using this approach.


#lst = [3, 1, 7, 4, 9, 2, 5]


def bubbleSort(n):
    for i in range(len(n)):
        for j in range(0, len(n)-i-1):
            if n[j] > n[j+1]:   # need to switch the elements around
                # create temporary variable to store 1st element that is larger than the 2nd compared element
                temp = n[j]
                # set 1st larger element being compared to the place of the next element being compared which is smaller
                n[j] = n[j+1]
                # 2nd element being compared is set to whatever is stored in temp
                n[j+1] = temp
                swapped = True
            if not swapped:
                break


lst = [3, 1, 7, 4, 9, 2, 5]
bubbleSort(lst)
lst
# = [1, 2, 3, 4, 5, 7, 9]


def bubble(list_a):
    for i in range(len(list_a)):
        for j in range(0, len(list_a) - i - 1):
            # comparing the 1st # against the # after it in the list, if 1st # in the list is bigger than the 2nd, it's false
            if list_a[j] > list_a[j + 1]:
                temporary = list_a[j]
                list_a[j] = list_a[j+1]
                list_a[j+1] = temporary
                swappedElements = True
            if not swappedElements:
                break


theList = [6, 4, 1, 3, 2, 5, 7, 8, 9, 7]
bubble(theList)
theList  # = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]
"""
"""

# Two-Dimensional Lists

import myModule
t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]

t[0]  # = [4, 7, 2, 5]
t[1]  # = [5, 1, 9, 2]
t[2][0]  # = 8      the element in row 2, column 0
t[0][0]  # = 4      the element in row 0, column 0
t[1][2]  # = 9       the element in row 1, column 2

# To assign a value to the entry in row i and column j, we simply use the assignment statement.
# For example:

t[2][3] = 7
print(t)  # = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 7]]


# = Two-Dimensional Lists and the Nested Loop Pattern
# Often it is nice to print the content of a two-dimensional list so it looks like a table.

for rows in t:
    print(rows)

# =
# [4, 7, 2, 5]
# [5, 1, 9, 2]
# [8, 3, 6, 7]

# We use the nested loop pattern to implement this function.
# The outer for loop is used to generate the rows,
# while the inner for loop iterates over the items in a row and prints them:


def print2D(t):
    'prints values in 2D list t as a 2D table'
    for rows in t:
        for items in rows:          # print item followed by
            print(items, end=' ')   # a blank space
        print()                     # move to next line


print2D(t)
# =
# 4 7 2 5
# 5 1 9 2
# 8 3 6 7

# Suppose we need to develop function incr2D() that increments the value of every number in a two-dimensional list of numbers:
# Clearly, the function incr2D() will need to execute:
# t[i][j] += 1


def incr2d(t):
    numRows = len(t)
    numCols = len(t[0])
    for i in range(numRows):
        for j in range(numCols):
            t[i][j] = t[i][j] + 1
        print()


t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
incr2d(t)


# 5.9
# Write a function add2D() that takes two two-dimensional lists of same size (i.e., same number of rows and columns)
# as input arguments and increments every entry in the first list with the value of the corresponding entry in the second list.

t = [[4, 7, 2, 5], [5, 1, 9, 2], [8, 3, 6, 6]]
s = [[0, 1, 2, 0], [0, 1, 1, 1], [0, 1, 0, 0]]


def add2D(t, s):
    nrows = len(t)                              # number of rows
    ncols = len(t[0])                           # number of columns
    'add2D increments every item t1[i][j] by t2[i][j]'
    for i in range(nrows):                      # for every row index i
        for j in range(ncols):                  # for every column index j
            t[i][j] = t[i][j] + s[i][j]         # or t[i][j] += s[i][j]


add2D(t, s)
for row in t:
    print(row)


# [4, 8, 4, 5]
# [5, 2, 10, 3]
# [8, 4, 6, 6]


# or


def add2D(t1, t2):
    't1 and t2 are 2D lists with the same number of rows and same number of equal sized columns'
    'add2D increments every item t1[i][j] by t2[i][j]'
    nrows = len(t1)  # number of rows
    ncols = len(t1[0])  # number of columns
    for i in range(nrows):  # for every row index i
        for j in range(ncols):  # for every column index j
            t1[i][j] += t2[i][j]


# while Loops
# perfect for situations in which we need to iterate but we do not know how many times.


# while <condition>:
#   <indented code block>
# <non-indented statement>


# compute the first multiple of 73 that is greater than 3,951.
# The variable multiple needs to be initialized before the while loop. We
goal = 3951
multiple = 73
while multiple <= goal:  # or <= 3951
    multiple += 73

multiple  # 4015

# When the while loop condition evaluates to False, the execution of the loop stops. The
# value of multiple is then greater than bound. Since the previous value of multiple was
# not greater, it will have the value we want: the smallest multiple greater than bound.


# 5.10
# Write a function interest() that takes one input, a floating-point interest rate (e.g., 0.06
# which corresponds to a 6% interest rate). Your function should compute and return how
# long (in years) it will take for an investment to double in value. Note: The number of years
# it takes for an investment to double does not depend on the value of the initial investment.
# >>> interest(0.07) # = 11


def interst(rate):
    investment = 100
    years = 0
    while investment < 200:
        years += 1
        investment += investment * rate
    return years


interst(0.06)  # =12


def fibonacci(bound):
    'returns the smallest Fibonacci number greater than bound '
    previous = 1  # first Fibonacci number
    current = 1  # second Fibonacci number
    while current <= bound:
        current  # becomes previous, and new current is computed
        previous, current = current, previous+current
        return current


fibonacci([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])


def factorial(n):
    'returns n!'
    res = 1
    # start at 2 because 1* any # is just itself, no need to do the last multiplication
    for i in range(2, n+1):
        res *= i
        'same as below'
        #res = res * i
    return res


# factorial(0)  # = 1


def approxE(error):
    'returns approximation of e within error'
    previous = 1
    current = 2
    i = 2
    while current - previous > error:
        previous = current
        current = previous + 1/factorial(i)
        i += 1
    return current


approxE(0.01)
# = 2.7166666666666663
approxE(0.000000001)
# = 2.7182818284467594


# Loop Pattern: Infinite Loop
# The while loop can be used to create an infinite loop, which is a loop that runs “forever”:

# while True:
#   <indented code block>
# Because True is always true, <indented code block> will get executed again and again.

# Infinite loops are useful when the program is meant to provide a service indefinitely.
# A web server (i.e., a program that serves web pages) is an example of a program that provides
# a service. It repeatedly receives web page requests from your—and other people’s—web browser and sends back the requested web page.

def hello2():
    while True:
        name = input('What is your name? ')
        print('Hello {}'.format(name))


hello2()

# CTRL + C can interrupt the program


# Loop Pattern: Loop and a Half
# A while loop should also be used when a program must repeatedly process some input
# values until a flag is reached.
# (A flag is an arbitrary value that is chosen to indicate the end of the input.)


# In function cities(), there are two input() function calls: one before the while
# loop statement and one inside the while loop code block. A way to eliminate one of those
# “redundant” statements and make the code more intuitive is to use an infinite loop and an
# if statement inside the body of the while loop. The if statement would test whether the user entered the flag value:


def cities2():
    '''returns the list of cities that are interactively entered
    by the user; the empty string ends the interactive input '''
    lst = []

    while True:                         # forever repeat:
        city = input('Enter city: ')    # ask user to enter city
        if city == '':                  # if city is the flag value
            return lst                  # return list
        lst.append(city)                # append city to list


cities2()

# = ['Chicago', 'New York', 'Milwuakee', 'Boston', 'Los Angelas', 'San Diego', 'Dallas', 'Paris']

# When executing function cities2(), the last iteration of the while loop is the one during
# which the user enters the empty string. In this iteration, only “half” of the body of the for
# loop is executed; the statement lst.append(city) is skipped. For this reason, the loop
# pattern in cities2() is commonly referred to as the loop-and-a-half pattern.


# break Statement
# When it is executed, the current loop iteration is stopped and the loop is exited.
# Execution then resumes with the statement that follows the loop statement.
# If the break statement appears in the code block of a loop of a nested loop pattern, only the innermost loop containing the break is exited.


def print2D2(table):
    'prints values in 2D list t as a 2D table'
    for rows in table:
        for items in rows:          # print item followed by
            print(items, end=' ')   # a blank space
        print()                     # move to next line


table = [[2, 3, 0, 6], [0, 3, 4, 5], [4, 5, 6, 0]]
print2D2(table)
# =
# 2 3 0 6
# 0 3 4 5
# 4 5 6 0


def before0(table):
    '''prints values in 2D list of numbers t as a 2D table;
    3 only values in row up to first 0 are printed '''
    for rows in table:
        for items in rows:          # inner for loop
            if items == 0:          # if items is 0
                break               # terminate inner for loop
            print(items, end=' ')   # otherwise print num
        print()


before0(table)

# =
# 2 3
#
# 4 5 6

# The break statement does not affect the outer for loop, which will iterate through all the
# rows of the table regardless of whether the break statement has been executed.


# Continue Statement
# The continue statement can be added to the code block of a loop, just like the break statement.
# When the continue statement is executed, the current, innermost loop iteration
# is stopped, and execution resumes with the next iteration of the current, innermost loop statement.
# Unlike the break statement, the continue statement does not terminate the
# innermost loop; it only terminates the current iteration of the innermost loop.


def ignore0(table):
    '''prints values in 2D list of numbers t as a 2D table;
    3 only values in row up to first 0 are printed '''
    for rows in table:
        for items in rows:          # inner for loop
            if items == 0:          # if items is 0
                continue            # current inner loop iteration
            print(items, end=' ')   # otherwise print items
        print()


ignore0(table)


# =
# 2 3 6
# 3 4 5
# 4 5 6


# Pass Statement
# In Python, every function definition def statement, if statement, or for or while loop statement must have a body
# (i.e., a nonempty indented code block).
# A syntax error while parsing the program would occur if the code block is missing.
# In the rare occasion when the code in the blocks really doesn’t have to do anything, we still have to put some code in it.
# For this reason Python provides the pass statement, which does nothing but is still a valid statement.
# The pass statement is also useful when a code body has not yet been implemented.


n = 3
if n % 2 == 0:
    pass        # do nothing for even number n
else:
    print(n)    # print n, only if n is an odd number

# = 3


# 5.12
# Implement function test() that takes as input one integer and prints 'Negative', 'Zero', or 'Positive' depending on its value.

def test(number):
    if number > 1:
        print('Positive')
    elif number == 0:
        print('Zero')
    else:
        print('Negative')


test(-3)
# Negative
test(0)
# = Zero
test(3)
# = Positve


# 5.14
# Write function mult3() that takes as input a list of integers and prints only the multiples of 3, one per line.

def mult3(lst):
    for num in lst:
        if num % 3 == 0:
            print(num)


mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])

# =
# 3
# 6
# 3
# 9
# 9
# for loop running through num


# 5.15
# Implement the function vowels() that takes as input a string and prints the indexes of all vowels in the string.
# Hint: A vowel can be defined as any character in string 'aeiouAEIOU'


def vowels(phrase):
    for i in range(0, len(phrase)):
        if phrase[i] in 'aeiouAEIOU':
            print(i)


vowels('Hello WORLD')


# =
# 1
# 4
# 7
# for loop running through indexes


# 5.16 Implement function indexes() that takes as input a word (as a string) and a one-
# character letter (as a string) and returns a list of indexes at which the letter occurs in the word.

def indexes(phrase, letter):
    index = []
    for i in range(0, len(phrase)):
        if phrase[i] == letter:
            index.append(i)
    return index


indexes('mississippi', 's')
# = [2, 3, 5, 6]
indexes('mississippi', 'i')
# = [1, 4, 7, 10]
indexes('mississippi', 'a')
# = []
# for loop running through indexes


# or


def indexes(phrase, letter):
    return [index for index, match in enumerate(phrase) if match == letter]


indexes('mississippi', 's')
# = [2, 3, 5, 6]
indexes('mississippi', 'i')
# = [1, 4, 7, 10]
indexes('mississippi', 'a')
# = []


# 5.17
# Write function doubles() that takes as input a list of integers and outputs the integers
# in the list that are exactly twice the previous integer in the list, one per line.
#doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5])


def doubles(lst):
    for i in range(0, len(lst)-1):
        if lst[i] * 2 == lst[i + 1]:
            print(lst[i + 1])


doubles([3, 0, 1, 2, 3, 6, 2, 4, 5, 6, 5])
# =
# 2
# 6
# 4


# 5.18
# Implement function four_letter() that takes as input a list of words (i.e., strings) and returns the sublist of all four letter words in the list.


def four_letter(lst):
    result = []
    for word in lst:
        if len(word) == 4:
            result.append(word)
    return result


four_letter(['dog', 'letter', 'stop', 'door', 'bus', 'dust'])
# =
# ['stop', 'door', 'dust']
# for loop running through indexes


# 5.19
# Write a function inBoth() that takes two lists and returns True if there is an item that is common to both lists and False otherwise.

def inBoth(lst1, lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False


inBoth([3, 2, 5, 4, 7], [9, 0, 1, 3])

# = True


# 5.20
# Write a function intersect() that takes two lists, each containing no duplicate values, and returns a list containing values that are present in both
# lists (i.e., the intersection of the two input lists).

def intersect(lst1, lst2):
    duplicate = []
    for i in lst1:
        if i in lst2:
            duplicate.append(i)
    return duplicate


intersect([3, 5, 1, 7, 9], [4, 2, 6, 3, 9])
# =
# [3, 9]
# for loop running through items


# 5.21
# Implement the function pair() that takes as input two lists of integers and one integer n and prints the pairs of integers,
# one from the first input list and the other from the second input list, that add up to n. Each pair should be printed.

def pair(ls1, lst2, n):
    for i in ls1:
        for j in lst2:
            if i + j == n:
                print(i, j)


pair([2, 3, 4], [5, 7, 9, 12], 9)

# =
# 2 7
# 4 5
# Exercise 21 - nested for loops running through items


# 5.22
# Implement the function pairSum() that takes as input a list of distinct integers lst
# and an integer n, and prints the indexes of all pairs of values in lst that sum up to n.

def pairSum(lst, n):
    for i in range(0, len(lst)):
        for j in range(i, len(lst)):
            if lst[i] + lst[j] == n:
                print(i, j)


pairSum([7, 8, 5, 3, 4, 6], 11)

# =
# 0 4
# 1 3
# 2 5
# Exercise 21 - nested for loops running through items


# 5.23
# Write function pay() that takes as input an hourly wage and the number of hours an employee worked in the last week.
# The function should compute and return the employee’s pay.
# Overtime work should be paid in this way: Any hours beyond 40 but less than or equal 60 should be paid at 1.5 times the regular hourly wage.
# Any hours beyond 60 should be paid at 2 times the regular hourly wage.

def pay(wage, hours):
    if hours <= 40:
        payment = wage * hours
    elif hours <= 60:
        payment = wage * 40
        payment = payment + (hours - 40) * (wage * 1.5)
        #payment += wage * (hours - 40) * 1.5
    else:
        payment = wage * 40
        payment = payment + wage * 20 * 1.5
        #payment += wage * 20 * 1.5
        payment = payment + (hours - 60) * (wage * 2)
        #payment += wage * (hours - 60) * 2
    return payment


pay(10, 35)
# = 350
pay(10, 45)
# = 475.0
pay(10, 61)
# = 720.0


# 5.24
# Write function case() that takes a string as input and returns 'capitalized', 'not capitalized', or 'unknown', depending on whether the string starts
# with an uppercase letter, lowercase letter, or something other than a letter in the English alphabet, respectively.

def case(string):
    if string[0] >= 'a' and string[0] <= 'z':
        return 'not capitalized'
    elif string[0] >= 'A' and string[0] <= 'Z':
        return 'capitalized'
    else:
        return 'unknown'


case('Android')
# = 'capitalized'
case('hello')
# = 'not capitalized'
case('3M')
# = 'unknown'


# 5.25
# Implement function leap() that takes one input argument—a year—and returns True
# if the year is a leap year and False otherwise. (A year is a leap year if it is divisible by 4 but
# not by 100, unless it is divisible by 400 in which case it is a leap year. For example, 1700, 1800 and 1900 are not leap years but 1600 and 2000 are.)


def leap(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    return False


leap(2008)
# = True
leap(1900)
# = False
leap(2000)
# = True


# 5.26
# Rock, Paper, Scissors is a two-player game in which each player chooses one of three
# items. If both players choose the same item, the game is tied. Otherwise, the rules that determine the winner are:
# (a) Rock always beats Scissors (Rock crushes Scissors)
# (b) Scissors always beats Paper (Scissors cut Paper)
# (c) Paper always beats Rock (Paper covers Rock)
# Implement function rps() that takes the choice ('R', 'P', or 'S') of player 1 and the
# choice of player 2, and returns −1 if player 1 wins, 1 if player 2 wins, or 0 if there is a tie.


def rps(player1, player2):
    if player1 == player2:
        return 0
    elif player1 == 'R' and player2 == 'S' or player1 == 'S' and player2 == 'P' or player1 == 'P' and player2 == 'R':
        return -1
    else:
        return 1


rps('R', 'P')   # = 1
rps('R', 'S')   # = -1
rps('S', 'S')   # = 0


# 5.27
# Write function letter2number() that takes as input a letter grade (A, B, C, D, F, possibly with a − or +)
# and returns the corresponding number grade. The numeric values
# for A, B, C, D, and F are 4, 3, 2, 1, 0. A + increases the number grade value by 0.3 and a − decreases it by 0.3.

def letter2number(grade):
    officialGrade = 0
    if 'A' in grade:
        officialGrade = 4
    elif 'B' in grade:
        officialGrade = 3
    elif 'C' in grade:
        officialGrade = 2
    elif 'D' in grade:
        officialGrade = 1.0
    elif 'F' in grade:
        officialGrade = 0
    if '-' in grade:
        officialGrade -= 0.3
    if '+' in grade:
        officialGrade += 0.3
    return officialGrade


letter2number('A-')
# = 3.7
letter2number('B+')
# = 3.3
letter2number('D')
# = 1.0


# 5.28
# Write function geometric() that takes a list of integers as input and returns True if
# the integers in the list form a geometric sequence. A sequence a0, a1, a2, a3, a4, . . . , an−2, an − 1
# is a geometric sequence if the ratios a1/a0, a2/a1, a3/a2, a4/a3, . . . , an−1/an−2 are all equal.

def geometric(lst):
    if len(lst) < 3:
        return True
    else:
        for i in range(0, len(lst)-1):
            if lst[i + 1] != lst[i] * 2:
                return False
        return True


geometric([2, 4, 8, 16, 32, 64, 128, 256])      # = True
geometric([1, 2, 4, 8])                         # = True
geometric([2, 4, 6, 8])                         # = False


# 5.29
# Write function lastfirst() that takes one argument—a list of strings of the format
# <LastName, FirstName>—and returns a list consisting two lists:
# (a) A list of all the first names
# (b) A list of all the last names

def lastfirst(lst):
    first, last = [], []
    output_list = []
    for i in lst:
        lName, fName = i.split(', ')
        first.append(fName)
        last.append(lName)
    output_list.append(first)
    output_list.append(last)
    return output_list


lastfirst(['Gerber, Len', 'Fox, Kate', 'Dunn, Bob'])
# = [['Len', 'Kate', 'Bob'], ['Gerber', 'Fox', 'Dunn']]


# 5.30
# Develop the function many() that takes as input the name of a file in the current
# directory (as a string) and outputs the number of words of length 1, 2, 3, and 4. Test your function on file sample.txt.


def many(filename):
    infile = open(filename)
    content = infile.read()
    infile.close()

    # Split content into a list of words
    table = str.maketrans('.,?!', 4*' ')
    content = content.translate(table)
    content = content.split()

    # Find the length of the longest word
    max = 0
    for word in content:
        if len(word) > max:
            max = len(word)

    # Create list with corresponding
    # number of items
    length = []
    for i in range(max):
        length.append(0)

    # Count words by length
    for word in content:
        length[len(word) - 1] += 1

    # Print the messages
    for i in range(len(length)):
        if length[i] != 0:
            print("Words of length {}: {}".format(
                i + 1, length[i]
            ))


many('sample.txt')


# 5.31
# Write a function subsetSum() that takes as input a list of positive numbers and a
# positive number target. Your function should return True if there are three numbers in
# the list that add up to target. For example, if the input list is [5, 4, 10, 20, 15, 19]
# and target is 38, then True should be returned since 4 + 15 + 19 = 38. However, if
# the input list is the same but the target value is 10, then the returned value should be False
# because 10 is not the sum of any three numbers in the given list.

def subsetSum(lst, target):
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            for k in range(j+1, len(lst)):
                if lst[i] + lst[j] + lst[k] == target:
                    return True
    return False


subsetSum([5, 4, 10, 20, 15, 19], 38)   # = True
subsetSum([5, 4, 10, 20, 15, 19], 10)   # = False
subsetSum([5, 4, 10, 20, 15, 19], 110)   # = False


# 5.32
# Implement function fib() that takes a nonnegative integer n as input and returns the nth Fibonacci number.

def fib(n):
    n1 = 1
    n2 = 1
    for i in range(n):
        n2 = n1 + n2
        n1 = n2 - n1
        return n


fib(0)
fib(4)
fib(8)


# 5.33
# Implement a function mystery() that takes as input a positive integer n and answers this question:
# How many times can n be halved (using integer division) before reaching 1?
# This value should returned.

def mystery(n):
    count = 0
    while n > 1:
        n //= 2  # or      n = n //2
        count += 1
    return count


mystery(4)  # = 2
mystery(11)  # = 3
mystery(25)  # = 4


# 5.34
# Write a function statement() that takes as input a list of floating-point numbers, with positive numbers
# representing deposits to and negative numbers representing withdrawals  from a bank account. Your
# function should return a list of two floating-point numbers; the first will be the sum of the deposits
# and the second (a negative number) will be the sum of the withdrawals.

def statement(lst):
    deposits, withdrawls = 0, 0
    for i in lst:
        if i > 0:
            deposits += i
        else:
            withdrawls += i
    return [deposits, withdrawls]


statement([30.95, -15.67, 45.56, -55.00, 43.78])
# = [120.29, -70.67]


# 5.35
# Implement function pixels() that takes as input a
# two-dimensional list of nonnegative integer entries (representing
# the values of pixels of an image) and returns the number of
# entries that are positive (i.e., the number of pixels that are not
# dark). Your function should work on two-dimensional lists of any size.


def pixels(lst):
    counter = 0
    for i in lst:
        for j in i:
            if j > 0:
                counter += 1
    return counter


l = [[0, 156, 0, 0], [34, 0, 0, 0], [23, 123, 0, 34]]
pixels(l)  # = 5

l = [[123, 56, 255], [34, 0, 0], [23, 123, 0], [3, 0, 0]]
pixels(l)  # = 7


# 5.36 Implement function prime() that takes a positive integer as
# input and returns True if it is a prime number and False otherwise.

def prime(n):
    for i in range(2, n//2):
        if n % i == 0:
            return False
    return True


prime(2)
# = True
prime(17)
# = True
prime(21)
# = False


# 5.37
# Write function mssl() (minimum sum sublist) that takes as input a list of integers.
# It then computes and returns the sum of the maximum sum sublist of the input list. The
# maximum sum sublist is a sublist (slice) of the input list whose sum of entries is largest.
# The empty sublist is defined to have sum 0. For example, the maximum sum sublist of the list
#[4, -2, -8, 5, -2, 7, 7, 2, -6, 5]
# is [5, -2, 7, 7, 2] and the sum of its entries is 19.

def mssl(lst):
    max = 0
    for i in range(len(lst)):
        for j in range(i, len(lst) + 1):
            if sum(lst[i: j]) > max:
                max = sum(lst[i: j])
    if max < 0:
        max = 0
    return max


l = [4, -2, -8, 5, -2, 7, 7, 2, -6, 5]
mssl(l)             # = 19
mssl([3, 4, 5])       # = 12
mssl([-2, -3, -5])    # = 0


# 5.38
# Write function collatz() that takes a positive integer x as input and prints the Collatz
# sequence starting at x. A Collatz sequence is obtained by repeatedly applying this rule to the previous number x in the sequence:

def collatz(x):
    # We simply follow steps
    # while we do not reach 1
    while x != 1:
        print(x)

        # If n is odd
        if x & 1:
            x = 3 * x + 1

        # If even
        else:
            x = x // 2

    # Print 1 at the end
    print(x)


# Driver code
collatz(10)


# 10
# 5
# 16
# 8
# 4
# 2
# 1


# 5.39
# Write function exclamation() that takes as input a string and returns it with this modification:
# Every vowel is replaced by four consecutive copies of itself and an exclamation mark (!) is added at the end.


def exclamation(phrase):
    word = ''
    for letters in phrase:
        if letters in 'aeiou':
            word = word + 4 * letters
        else:
            word = word + letters
    word = word + '!'
    return word


exclamation('argh')
# = 'aaaargh!'
exclamation('hello')
# = 'heeeelloooo!'


# 5.42
# Implement function primeFac() that takes as input a positive integer n and returns a
# list containing all the numbers in the prime factorization of n. (The prime factorization of
# a positive integer n is the unique list of prime numbers whose product is n.)


def primeFac(n):
    coef = 2
    prime = []
    while n != 1:
        if n % coef == 0:
            prime.append(coef)
            n /= coef
        else:
            coef += 1
    return prime


primeFac(5)
# = [5]
primeFac(72)
# = [2, 2, 2, 3, 3]


# 5.43
# Implement function evenrow() that takes a two-dimensional list of integers and returns True if each row of the table sums up to an even number and False otherwise (i.e.,if some row sums up to an odd number).


def evenrow(lst):
    for sub_list in lst:
        if sum(sub_list) % 2 != 0:
            return False
    return True


evenrow([[1, 3], [2, 4], [0, 6]])               # = True
evenrow([[1, 3, 2], [3, 4, 7], [0, 6, 2]])      # = True
evenrow([[1, 3, 2], [3, 4, 7], [0, 5, 2]])      # = False


# 5.44
# A substitution cipher for the digits 0, 1, 2, 3, . . . , 9 substitutes each digit in 0, 1, 2,
# 3, . . . , 9 with another digit in 0, 1, 2, 3, . . . , 9. It can be represented as a 10-digit string
# specifying how each digit in 0, 1, 2, 3, . . . , 9 is substituted. For example, the 10-digit string
# '3941068257' specifies a substitution cipher in which digit 0 is substituted with digit 3, 1
# with 9, 2 with 4, and so on. To encrypt a nonnegative integer, substitute each of its digits with the digit specified by the encryption key.
# Implement function cipher() that takes as input a 10-digit string key and a digit string
# (i.e., the clear text to be encrypted) and returns the encryption of the clear text.


def cipher(code, text):
    table = str.maketrans('0123456789', code)
    return text.translate(table)


cipher('3941068257', '134')
# = 910
cipher('3941068257', '132')
# = '914'
cipher('3941068257', '111')
# = '999'


# 5.45
# The function avgavg() takes as input a list whose items are lists of three numbers.
# Each three-number list represents the three grades a particular student received for a course.
# For example, here is an input list for a class of four students:
# [[95,92,86], [66,75,54],[89, 72,100],[34,0,0]]
# The function avgavg() should print, on the screen, two lines. The first line will contain a
# list containing every student’s average grade. The second line will contain just one number:
# the average class grade, defined as the average of all student average grades.


def avgavg(gradesList):
    studentAverages = []
    for sublist in gradesList:
        studentAverage = sum(sublist)/len(sublist)
        studentAverages.append(studentAverage)
        classAverage = sum(studentAverages)/len(studentAverages)
    print([studentAverages])
    print(classAverage)


# or

def avgavg(students):
    studentAverages = []
    for sublist in students:
        studentAverages.append(sum(sublist) / len(sublist))
    print(studentAverages)
    print(sum(studentAverages) / len(studentAverages))


avgavg([[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]])
# = [91.0],[65.0],[87.0],[11.333333333333334]
# = 63.583333333333336


age = (23, 19, 31)
average_age = sum(age)/len(age)
print(average_age)


# 5.46
# An inversion in a sequence is a pair of entries that are out of order. For example, the
# characters F and D form an inversion in string 'ABBFHDL' because F appears before D; so
# do characters H and D. The total number of inversions in a sequence (i.e., the number of
# pairs that are out of order) is a measure of how unsorted the sequence is. The total number
# of inversions in 'ABBFHDL' is 2. Implement function inversions() that takes a sequence
# (i.e., a string) of uppercase characters A through Z and returns the number of inversions in the sequence.

# count
def inversions(letters):
    count = 0
    for i in range(len(letters)):
        for j in range(i, len(letters)):
            if letters[i] > letters[j]:
                count += 1
    return count


inversions('ABBFHDL')   # = 2
inversions('ABCD')      # = 0
inversions('DCBA')      # = 6


# 5.48
# Let list1 and list2 be two lists of integers. We say that list1 is a sublist of list2
# if the elements in list1 appear in list2 in the same order as they appear in list1, but
# not necessarily consecutively. For example, if list1 is defined as
# [15, 1, 100] and list2 is defined as [20, 15, 30, 50, 1, 100]
# then list1 is a sublist of list2 because the numbers in list1 (15, 1, and 100) appear in
# list2 in the same order. However, list [15, 50, 20] is not a sublist of list2
# Implement function sublist() that takes as input lists list1 and list2 and returns True if list1 is a sublist of list2, and False otherwise.


def sublist(list1, list2):
    # This variable will be used to keep track of the position we are checking in list1.
    index = 0
    # It uses a for loop to iterate over the indices of list2 using the range(len(list2)) function.
    for i in range(len(list2)):
        # Inside the loop, it checks if the element at list1[index] (the current element being checked in list1) is equal to the element at list2[i] (the #current element being checked in list2).
        # If the elements are equal, it means we have found a match in list2 for the current element in list1. Therefore, the function increments the #index variable to move on to the next element in list1.
        if list1[index] == list2[i]:
            index += 1
    # The loop continues to iterate over list2, and if all elements of list1 are found in list2 in the same order, the index variable will be equal to the length of list1.
    return index == len(list1)


sublist([15, 1, 100], [20, 15, 30, 50, 1, 100])     # = True
sublist([15, 50, 20], [20, 15, 30, 50, 1, 100])     # = False


# Chapter 6 Containers and Randomness

# Dictionary-a container that stores items that are accessible using “user-specified” indexes.
# built-in container type
# Ddffers from a list in that an item in a dictionary is accessed using a
# user-specified “index” rather than the index representing the items position in the container.


# Dictionary Class Properties
# The Python dictionary type, denoted dict, is a container type, just like list and str. A
# dictionary contains (key, value) pairs. The general format of the expression that evaluates
# to a dictionary object is:

# {<key 1>:<value 1>, <key 2>:<value 2>, ..., <key i>:<value i>}


# This expression defines a dictionary containing i key:value pairs.
# The key and the value are both objects.
# The key is the “index” that is used to access the value.


# The (key, value) pairs in a dictionary expression are separated by commas and enclosed
# in curly braces (as opposed to square brackets, [], used for lists.)
# The key and value in each (key, value) pair are separated by a colon (:) with the key being to the left and the value to the right of the colon.
# Keys can be of any type as long as the type is immutable.
# So string and number objects can be keys, whereas objects of type list cannot.
# The value can be of any type.
# We often say that a key maps to its value or is the index of the value.
# Because dictionaries can be viewed as a mapping from keys to values, they are often referred to as maps.


employee = {
    '864-20-9753': ['Anna', 'Karenina'],
    '987-65-4321': ['Yu', 'Tsun'],
    '100-01-0010': ['Hans', 'Castorp']}


employee['987-65-4321']

# = ['Yu', 'Tsun']


days = {'Mo': 'Monday', 'Tu': 'Tuesday', 'We': 'Wednesday', 'Th': 'Thursday'}


# Values in the dictionary are accessed by key, not index (or offset).
# To access value 'Wednesday' in dictionary days, we use key 'We' .

days['We']
# or
print(days['We'])

# = 'Wednesday'


# The (key, value) pairs in the dictionary are not ordered, and no ordering assumption can be made.

# days[2]->>>>> error!!

d = {'b': 23, 'a': 34, 'c': 12}

# we may not get the (key, value) pairs in the order in which they were defined:

# Dictionaries are mutable, like lists. A dictionary can be modified to contain a new (key,value) pair:

days['Fr'] = 'Friday'
days
# = {'Mo': 'Monday', 'Tu': 'Tuesday', 'We': 'Wednesday', 'Th': 'Thursday', 'Fr': 'Friday'}


# This implies that dictionaries have dynamic size.
# The dictionary can also be modified so that an existing key refers to a new value:

days['Fr'] = 'Fri-DAY!'
days
# = {'Fr': 'Fri-DAY!', 'Mo': 'Monday', 'Tu': 'Tuesday', 'We': 'Wednesday', 'Th': 'Thursday'}


# An empty dictionary can be defined using the default dict() constructor or simply as:
d = {}
print(d)  # = {}


# 6.1
# Write a function birthState() that takes as input the full name of a recent U.S. president
# (as a string) and returns his birth state. You should use this dictionary to store the birth state for each recent president:

def birthState(name):
    presidentStates = {'Barack Hussein Obama II': 'Hawaii',
                       'George Walker Bush': 'Connecticut',
                       'William Jefferson Clinton': 'Arkansas',
                       'George Herbert Walker Bush': 'Massachussetts',
                       'Ronald Wilson Reagan': 'Illinois',
                       'James Earl Carter, Jr': 'Georgia'}
    return presidentStates[name]


birthState('Ronald Wilson Reagan')

# = 'Illinois'


# Dictionary Operators
# The indexing operator ([]) can be used to access a value using the key as the index, just like you can in a list


days['Fr']  # = 'Fri-DAY!'

# The indexing operator can also be used to change the value corresponding to a key or to add a new (key, value) pair to the dictionary:

days['Su'] = 'Sunday'
print(days)
# = {'Mo': 'Monday', 'Tu': 'Tuesday', 'We': 'Wednesday', 'Th': 'Thursday', 'Fr': 'Fri-DAY!', 'Su': 'Sunday'}

# The length of a dictionary (i.e., the number of (key, value) pairs in it) can be obtained using the len function:

len(days)  # = 6

# The in and not in operators are used to check whether an object is a key in the dictionary:
'Fr' in days    # = True
'Su' in days    # = False
'Su' not in days  # = True
'Sunday' in days  # = False


# 6.2
# Implement function rlookup() that provides the reverse lookup feature of a phone book.
# Your function takes, as input, a dictionary representing a phone book. In the dictionary, phone numbers (keys) are mapped to individuals (values).
# Your function should provide a simple user interface through which a user can enter a phone number and obtain the first
# and last name of the individual assigned that number.

rphonebook = {'(123)456-78-90': ['Anna', 'Karenina'],
              '(901)234-56-78': ['Yu', 'Tsun'],
              '(321)908-76-54': ['Hans', 'Castorp']}


def rlookup(phonebook):
    while True:
        number = input('Enter phone number in the format (xxx)xxx-xx-xx: ')
        if number in phonebook:
            print(phonebook[number])
        else:
            print('This number is not in the phonebook')


rlookup(rphonebook)


print(days)
# = {'Mo': 'Monday', 'Tu': 'Tuesday', 'We': 'Wednesday', 'Th': 'Thursday', 'Fr': 'Fri-DAY!', 'Su': 'Sunday'}

days.pop('Tu')  # 'Tuesday'
days.pop('Fr')  # 'Fri-DAY!'
# = {'Mo': 'Monday', 'We': 'Wednesday', 'Th': 'Thursday', 'Su': 'Sunday'}
print(days)


# Update() Method:
# Input argument dictionary of 2nd variable, all the (key, value) pairs of 2nd variable are added to 1st variable, possibly writing over (key, value)
# pairs of 1st variable.
# New (key, value) pairs wil be added to the first variable.
# (key, value) pairs with the same key value replace the original (key, value) pairs.
# Only one copy of (key, value) pair can be in the dictionary.


favorites = {'Th': 'Thursday', 'Fr': 'Friday', 'Su': 'Sun'}
days.update(favorites)
# = {'Mo': 'Monday', 'We': 'Wednesday', 'Th': 'Thursday', 'Su': 'Sun', 'Fr': 'Friday'}
print(days)


days['Su'] = 'Sunday'
# = {'Mo': 'Monday', 'We': 'Wednesday', 'Th': 'Thursday', 'Su': 'Sunday', 'Fr': 'Friday'}
print(days)


# Particularly useful dictionary methods are keys(), values(), and items():

# The method keys() returns the keys of the dictionary:

keys = days.keys()
print(keys)     # = dict_keys(['Mo', 'We', 'Th', 'Su', 'Fr'])


# The container object returned by method keys() is not a list. Let’s check its type:

type(days.keys())  # = <class 'dict_keys'>


# How is the object returned by the keys() method used?
# It is typically used to iterate over the keys of the dictionary, for example:

for key in days.keys():
    print(key, end=' ')
# = Mo We Th Su Fr

for value in days.values():
    print(value, end=' ')
# = Monday Wednesday Thursday Sunday Friday


# Items() Method
# Returns a view of the (key, value) pairs in variable as tuple objects, one for each (key,value) pair:

# = dict_items([('Mo', 'Monday'), ('We', 'Wednesday'), ('Th', 'Thursday'), ('Su', 'Sunday'), ('Fr', 'Friday')])
days.items()

# This method is typically used to iterate over the (key, value) pairs of the dictionary:

for everything in days.items():
    print(everything, end=' ')
# = ('Mo', 'Monday') ('We', 'Wednesday') ('Th', 'Thursday') ('Su', 'Sunday') ('Fr', 'Friday')


# View Objects
# The objects returned by methods keys(), values(), and items() are referred to as view objects.
# View objects provide a dynamic view of the dictionary’s keys, values, and (key, value) pairs, respectively.
# What this means is that when the dictionary changes, the view reflects these changes.

print(days)
# = {'Mo': 'Monday', 'We': 'Wednesday', 'Th': 'Thursday', 'Su': 'Sunday', 'Fr': 'Friday'}

keys = days.keys()
print(keys)  # = dict_keys(['Mo', 'We', 'Th', 'Su', 'Fr'])

# del(days['Mo'])
# print(days)
# = {'Fr': 'Friday', 'We': 'Wednesday', 'Th': 'Thursday', 'Sa': 'Saturday'}

# print(keys)
# = dict_keys(['Fr', 'We', 'Th', 'Sa'])


# A Dictionary as a Substitute for the Multiway if Statement
# TOO LONG!!!!

def complete(abbreviation):
    'returns day of the week corresponding to abbreviation '
    if abbreviation == 'Mo':
        return 'Monday'
    elif abbreviation == 'Tu':
        return 'Tuesday'
    elif ...
    ...
    else:  # abbreviation must be Su
        return 'Sunday'


complete('Tu')
# = 'Tuesday'


def complete(abbreviation):
    'returns day of the week corresponding to abbreviation '
    days = {'Mo': 'Monday', 'Tu': 'Tuesday', 'We': 'Wednesday',
            'Th': 'Thursday', 'Fr': 'Friday', 'Sa': 'Saturday', 'Su': 'Sunday'}

    return days[abbreviation]


complete('Tu')
# = 'Tuesday'


def frequency(students):
    'returns frequency of items in itemList'
    students = ['Cindy', 'John', 'Cindy', 'Adam',
                'Adam', 'Jimmy', 'Joan', 'Cindy', 'Joan']
    counters = {}
    for student in students:
        if student in counters:
            counters[student] += 1
        else:
            counters[student] = 1
    return counters


frequency(students)
# = {'Cindy': 3, 'John': 1, 'Adam': 2, 'Jimmy': 1, 'Joan': 2}


# 6.4
# Implement function wordcount() that takes as input a text—as a string— and prints the frequency of each word in the text.
# You may assume that the text has no punctuation and words are separated by blank spaces.


def wordCount(text):
    'prints frequency of each word in text'
    wordList = text.split()  # split text into list of words
    counters = {}  # dictionary of counters

    for word in wordList:
        if word in counters:  # counter for word exists
            counters[word] += 1
        else:  # counter for word doesn't exist
            counters[word] = 1

    for word in counters:  # print word counts
        if counters[word] == 1:
            print('{:8} appears {} time.'.format(word, counters[word]))
        else:
            print('{:8} appears {} times.'.format(word, counters[word]))


text = 'all animals are equal but some animals are more equal than others'

wordcount(text)


# tuple Objects Can Be Dictionary Keys
# Because tuple objects are immutable, they can be used as dictionary keys.


phonebook = {('Anna', 'Kendrick'): '(123)-456-7890',
             ('Yu', 'Tsun'): '(902)-109-0210',
             ('Hans', 'Castro'): '(773)-202-1234'}

# = {('Anna', 'Kendrick'): '(123)-456-7890', ('Yu', 'Tsun'): '(902)-109-0210', ('Hans', 'Castro'): '(773)-202-1234'}
print(phonebook)

phonebook[('Anna', 'Kendrick')]  # = '(123)-456-7890'


# 6.5
# Implement function lookup() that implements a phone book lookup application.
# Your function takes, as input, a dictionary representing a phone book.
# In the dictionary, tuples containing first and last names of individual (the keys) are mapped to strings containing phone numbers (the values).
# Your function should provide a simple user interface through which a user can enter the first
# and last name of an individual and obtain the phone number assigned to that individual.


aphonebook = {('Anna', 'Karenina'): '(123)456-78-90',
              ('Yu', 'Tsun'): '(901)234-56-78',
              ('Hans', 'Castorp'): '(321)908-76-54'}


def lookup(phonebook):
    '''implements interactive phone book service using the input
    phonebook dictionary'''

    while True:
        fname = input('Enter the first name: ')
        lname = input('Enter the last name: ')
        person = (fname, lname)                 # construct the key
        if person in phonebook:                 # if key is in dictionary
            print(phonebook[person])
        else:                                   # if key not in dictionary
            print('This name is not in the phonebook')


lookup(phonebook)


# Sets
# Built-in Python container type.
# The set class has all the properties of a mathematical set. It is used to store an unordered collection of items, with no duplicate items allowed.
# The items must be immutable objects.
# The set type supports operators that implement the classical set operations: set membership, intersection, union, symmetric difference, and so on.
# It is thus useful whenever a collection of items is modeled as a mathematical set.
# It is also useful for duplicate removal.
# A set is defined using the same notation that is used for mathematical sets: a sequence of items separated by commas and enclosed in curly braces: { }.


phonebook1 = {'123-45-67', '234-56-78', '345-67-89'}
print(phonebook1)       # = {'345-67-89', '234-56-78', '123-45-67'}
type(phonebook1)        # = <class 'set'>


# If we had defined a set with duplicate items, they would be ignored:
phonebook1 = {'123-45-67', '234-56-78', '345-67-89',
              '123-45-67', '345-67-89'}

print(phonebook1)       # = {'345-67-89', '234-56-78', '123-45-67'}


# Using the set Constructor to Remove Duplicates
# The fact that sets cannot have duplicates gives us the first great application for sets: removing duplicates from a list.
ages = [23, 19, 18, 21, 18, 20, 21, 23, 22, 23, 19, 20]

# To remove duplicates from this list, we can convert the list to a set, using the set constructor.
# The set constructor will eliminate all duplicates because a set is not supposed to have them.
# By converting the set back to a list, we get a list with no duplicates:

ages = list(set(ages))
print(ages)         # = [18, 19, 20, 21, 22, 23]

# There is, however, one major caveat: The elements have been reordered.


# Empty Sets
# We have to use the set constructor explicitly when creating an empty set:

phonebook2 = set()
print(phonebook2)           # = set()
type(phonebook2)            # = <class 'set'>


# set Operators
# The set class supports operators that correspond to the usual mathematical set operations.
# Some are operators that can also be used with list, string, and dictionary types.
# In and not in operators are used to test set membership:


phonebook1 = {'123-45-67', '234-56-78', '345-67-89'}
'123-45-67' in phonebook1       # = True
'456-78-90' in phonebook1       # = False
'456-78-90' not in phonebook1   # = True

# The len() operator returns the size of the set:
len(phonebook1)                 # = 3


# Comparison operators ==, !=, <, <=, >, and >= are supported as well, but their meaning is set-specific.
# Two sets are “equal” if and only if they have the same elements:

phonebook3 = {'345-67-89', '456-78-90'}
phonebook1 == phonebook3        # = False
phonebook1 != phonebook3        # = True


# A set is “less than or equal to” another set if it is a subset of it.
# A set is “less than another set” if it is a proper subset of it. So, for example:

{'123-45-67', '345-67-89'} <= phonebook1            # = True


# However, phonebook2 is not a proper subset of phonebook1:
phonebook2 = {'123-45-67', '345-67-89'}
phonebook1 < phonebook2     # = False


# The mathematical set operations union, intersection, difference, and symmetric difference are implemented as set operators |, &, -, and ^, respectively
# Each set operation takes two sets and returns a new set.


# Union
# The union of two sets contains all elements that are in either set:

phonebook1 | phonebook3
# = {'234-56-78', '123-45-67', '345-67-89', '456-78-90'}


# Intersection
# The intersection of two sets contains all elements that are in both sets:

phonebook1 & phonebook3
# = {'345-67-89'}


# Difference
# The difference between two sets contains all elements that are in the first set but not the second one:

phonebook1 - phonebook3
# = {'234-56-78', '123-45-67'}

phonebook3 - phonebook1
# = {'456-78-90'}


# Symmetric difference
# The symmetric difference of two sets contains all elements that are either in the first set or in the second set, but not both:

phonebook1 ^ phonebook3
# = {'234-56-78', '456-78-90', '123-45-67'}


# Set Methods
# the set class supports a number of methods.


# The set method add()
# Used to add an item to a set:

phonebook3.add('123-45-67')
print(phonebook3)
# = {'345-67-89', '456-78-90', '123-45-67'}


# The set method remove()
# Used to remove an item from a set:

phonebook3.remove('123-45-67')
print(phonebook3)
# = {'345-67-89', '456-78-90'}


# The set method clear()
# Used to empty a set:

phonebook3.clear()
print(phonebook3)
# = set()


# 6.6
# Implement function sync() that takes a list of phone books (where each phone book is a
# set of phone numbers) as input and returns a phone book (as a set) containing the union of all the phone books.

phonebook4 = {'234-56-78', '456-78-90'}
phonebooks = [phonebook1, phonebook2, phonebook3, phonebook4]
#phonebooks = set(phonebook1 | phonebook2 | phonebook3 | phonebook4)


def sync(phonebooks):
    'returns the union of sets in phonebooks'
    #phonebooks = set(phonebook1 | phonebook2 | phonebook3 | phonebook4)
    res = set()                         # initialize the accumulator
    for phonebook in phonebooks:
        res = res | phonebook           # accumulate phonebook into res
    return res


sync(phonebooks)
# = {'234-56-78', '123-45-67', '345-67-89', '456-78-90'}


# Character Encodings
# String objects are used to store text, that is, a sequence of characters. The characters could
# be upper- and lowercase letters from the alphabet, digits, punctuation marks, and possibly symbols like the dollar sign ($).


# ASCII
# For many years, the standard encoding for characters in the English language was ASCII encoding.
# You can explore the ASCII encodings using the Python function ord(), which returns the decimal ASCII code of a character:
# ASCII codes 0 through 32 and 127 include nonprintable characters, such as backspace (decimal code 8), horizontal tab
# (decimal code 9), and line feed (decimal code 10).

ord('a')        # = 97
ord('dad')


# The sequence of characters of a string value (such as 'dad') is encoded as a sequence of ASCII codes 100, 97, and 100.
# What is stored in memory is exactly this sequence of codes.
# Of course, each code is stored in binary.
# As ASCII decimal codes go from 0 to 127, they can be encoded with seven bits;
# because a byte (eight bits) is the smallest memory storage unit, each code is stored in one byte.

# For example, the decimal ASCII code for lowercase a is 97, which corresponds to binary ASCII code 1100001.
# So, in the ASCII encoding, character a is encoded in a single byte with the first bit being a 0 and the remaining bits being 1100001.
# The resulting byte 01100001 can be described more succinctly using a two-digit hex number 0x61 (6 for the leftmost four bits, 0110, and 1 for the
# rightmost 4 bits, 0001).
# In fact, it it common to use hex ASCII codes (as a shorthand for ASCII binary codes).


# The symbol &, for example, is encoded with decimal ASCII code 38, which corresponds to binary code 0100110 or hex code 0x26.


# 6.7
# Write a function encoding() that takes a string as input and prints the ASCII code—in decimal, hex, and binary notation—of every character in it.

def encoding(word):
    'prints ASCII codes of characters in S, one per line'
    print('Char Decimal Hex Binary')  # print column headings
    for letters in word:
        ascii = ord(letters)
        # print character and its code in decimal, hex, and binary
        print(' {} {:7} {:4x} {:7b}'.format(letters, ascii, ascii, ascii))


def encoding(text):
    'prints ASCII codes of characters in S, one per line'
    print('Char Decimal Hex Binary')  # print column headings
    for c in text:
        code = ord(c)  # compute ASCII code
        # print character and its code in decimal, hex, and binary
        print(' {} {:7} {:4x} {:7b}'.format(c, code, code, code))


encoding('dad')


# chr()
# The function chr() is the inverse of function ord(). It takes a numeric code and returns the character corresponding to it.


ord('a')        # = 97
chr(97)         # = 'a'


# 6.8
# Write function char(low, high) that prints the characters corresponding to ASCII decimal codes i for all values of i from low up to and including high.

def char(low, high):
    # prints the characters with ASCII codes in the range from low to high
    for i in range(low, high + 1):
        # print integer ASCII code and corresponding character
        print('{} : {}'.format(i, chr(i)))


char(62, 67)

# We use a counter loop pattern to generate integers from low to high. The character corresponding to each integer is printed:

# 62 : >
# 63 : ?
# 64 : @
# 65 : A
# 66 : B
# 67 : C


# Loop through the items in the fruits list.


fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# apple
# banana
# cherry


# In the loop, when the item value is "banana", jump directly to the next item.


fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

# apple
# cherry


# Use the range function to loop through a code set 6 times.

for x in range(6):
    print(x)

# 0
# 1
# 2
# 3
# 4
# 5


# Exit the loop when x is "banana".

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)

# apple


# Create a function named my_function.
# Execute a function named my_function.

def my_function():
    print("Hello from a function")


my_function()

# Hello from a function


# Inside a function with two parameters, print the first parameter.


def my_function(fname, lname):
    print(fname)


my_function('Jose', 'Armas')

# Jose


# Let the function return the x parameter + 5.

def my_function(x):
    return x + 5


my_function(5)
# = 10


# If you do not know the number of arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?

def my_function(*kids):
    print("The youngest child is " + kids[2])


# If you do not know the number of keyword arguments that will be passed into your function, there is a prefix you can add in the function definition, which prefix?

def my_function(**kid):
    print("His last name is " + kid["lname"])


# Create a lambda function that takes one parameter (a) and returns it.
# A lambda function can take any number of arguments, but can only have one expression.


def x(a): return a + 10


print(x(5))


# Create a class named MyClass:
# A Class is like an object constructor, or a "blueprint" for creating objects.


class myClass:
    x = 5


# Create an object of MyClass called p1:

class myClass:
    x = 5


p1 = myClass()


# Use the p1 object to print the value of x:

class myClass:
    x = 5


p1 = myClass()
print(p1.x)
# = 5


# What is the correct syntax to assign a "init" function to a class?

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# What is the correct syntax to create a class named Student that will inherit properties and methods from a class named Person?

class Student(Person):

    # We have used the Student class to create an object named x.
    # What is the correct syntax to execute the printname method of the object x?


class Person:
    def __init__(self, fname):
        self.firstname = fname

    def printname(self):
        print(self.firstname)


class Student(Person):
    pass


x = Student("Mike")
x.printname()

# = Mike


# What is the correct syntax to import a module named "mymodule"?


# Print i as long as i is less than 6

def less(i):
    if i < 6:
        print(i)


less(4)

# = 4


# The while loop requires relevant variables to be ready, in this example we need to define an indexing variable, i, which we set to 1.


def less(i):
    while i < 6:
        print(i)
        i += 1


less(1)

# 1
# 2
# 3
# 4
# 5


# Stop the loop if i is 3.

def less(i):
    while i < 6:
        print(i)
        i += 1
        if i == 3:
            break


less(1)

# 1
# 2


# In the loop, when i is 3, jump directly to the next iteration.


def less(i):
    while i < 6:
        print(i)
        i += 1
        if i == 3:
            continue


less(1)

# 1
# 2
# 3
# 4
# 5


# Print a message once the condition is false.


def less(i):
    while i < 6:
        print(i)
        i += 1
    else:
        print("i is no longer less than 6")


less(1)


# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6


# Print "A is greater than B" if a is greater than b.
a = 50
b = 10
if a > b:
    print('A is greater than B')


def number(a):
    b = 10
    if a > b:
        print('A is greater than B')


number(50)


# Print "a is not equal to b" if a is not equal to b.

a = 50
b = 10
if a != b:
    print("a is not equal to b")


def number(a):
    b = 10
    if a != b:
        print('a is not equal to b')


number(50)


# Print "Yes" if a is equal to b, otherwise print "No".

b = 10


def number(a):
    #b = 10
    if a == b:
        print('Yes')
    else:
        print("NO")


number(50)


# Print "1" if a is equal to b, print "2" if a is greater than b, otherwise print "3".


def number(a):
    b = 10
    if a == b:
        print('1')
    elif a > b:
        print('2')
    else:
        print("3")


number(50)

# 2


# Print "True" if a is equal to b, and c is equal to d.

d = 3


def number(a):
    b = 10
    c = 3
    if a == b and c == d:
        print('True')
    else:
        print("False")


number(50)

# False


# Print "True" if a is equal to b, or c is equal to d.

d = 3


def number(a):
    b = 10
    c = 3
    if a == b or c == d:
        print('True')
    else:
        print("False")


number(50)

# = True


# Use the correct short hand syntax to write the following conditional expression in one line:

if 5 > 2:
    print("Yes")
else:
    print("No")


print("Yes") if 5 > 2 else print("No")

# Yes

# get() method
# Use the get method to print the value of the "model" key of the car dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

print(car.get("model"))
# or
print(car['model'])


# Change the "year" value from 1964 to 2020.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car["year"] = 2020
print(car)

# = {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# Add the key/value pair "color" : "red" to the car dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car['color'] = 'red'
print(car)


#{'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# Use the pop method to remove "model" from the car dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.pop("model")
print(car)


# = {'brand': 'Ford', 'year': 1964}


# Use the clear method to empty the car dictionary.

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

car.clear()
print(car)
# = {}


# Check if "apple" is present in the fruits set.

fruits = {"apple", "banana", "cherry"}

if 'apple' in fruits:
    print('Yes, an apple is a fruit.')

# = Yes, an apple is a fruit.


# Use the add method to add "orange" to the fruits set.

fruits.add('orange')
print(fruits)

# = {'cherry', 'banana', 'apple', 'orange'}


# Use the correct method to add multiple items (more_fruits) to the fruits set.


fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]

fruits.update(more_fruits)
print(fruits)


# = {'apple', 'mango', 'grapes', 'orange', 'banana', 'cherry'}


# Use the remove method to remove "banana" from the fruits set.

fruits = {'apple', 'mango', 'grapes', 'orange', 'banana', 'cherry'}
fruits.remove('banana')
print(fruits)


# = {'apple', 'mango', 'grapes', 'orange', 'cherry'}


# Use the discard method to remove "banana" from the fruits set.

fruits = {"apple", "banana", "cherry"}
fruits.discard('banana')


# discard()
# The discard() method removes the specified item from the set
# This method is different from the remove() method, because the
# remove() method will raise an error if the specified item does
# not exist, and the discard() method will not.


# Use the correct syntax to print the first item in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[0])

# = apple


# Use the correct syntax to print the number of items in the fruits tuple.

fruits = ("apple", "banana", "cherry")
print(len(fruits))


# = 3


# Use negative indexing to print the last item in the tuple.

fruits = ("apple", "banana", "cherry")
print(fruits[-1])

# = cherry


# Use a range of indexes to print the third, fourth, and fifth item in the tuple.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")


print(fruits[2:5])

# = ('cherry', 'orange', 'kiwi')


# Use the correct syntax to print the first item and thrd item in the fruits tuple.

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")

print(fruits[0], fruits[2])


# Print the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

# = banana


# Change the value from "apple" to "kiwi", in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits[0] = 'kiwi'
print(fruits)


# = ['kiwi', 'banana', 'cherry']


# Use the append method to add "orange" to the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.append('orange')
print(fruits)
#['apple', 'banana', 'cherry', 'orange']


# Use the insert method to add "lemon" as the second item in the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.insert(1, 'lemon')
print(fruits)


# = ['apple', 'lemon', 'banana', 'cherry']


# Use the remove method to remove "banana" from the fruits list.

fruits = ["apple", "banana", "cherry"]
fruits.remove('banana')
print(fruits)


# = ['apple', 'cherry']


# Use negative indexing to print the last item in the list.

fruits = ["apple", "banana", "cherry"]
print(fruits[-1])
# = cherry


# Use a range of indexes to print the third, fourth, and fifth item in the list.

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])
# = ['cherry', 'orange', 'kiwi']


# Use the correct syntax to print the number of items in the list.

fruits = ["apple", "banana", "cherry"]
print(len(fruits))
# = 3


# Use the len method to print the length of the string.

x = "Hello World"
print(len(x))
# = 11


# Get the first character of the string txt.

txt = "Hello World"
x = txt[0]
print(x)
# = H


# Get the characters from index 2 to index 4 (llo).

txt = "Hello World"
x = txt[2:5]
print(x)
# = llo


# Return the string without any whitespace at the beginning or the end.

txt = " Hello World "
x = txt.strip()
print(x)


# Convert the value of txt to upper case.

txt = "Hello World"
txt = txt.upper()
print(txt)
# = HELLO WORLD

# Convert the value of txt to lower case.

txt = "Hello World"
txt = txt.lower()
print(txt)
# = hello world


# Replace the character H with a J.

txt = "Hello World"
txt = txt.replace('H', 'J')
print(txt)
# = Jello World


# Insert the correct syntax to add a placeholder for the age parameter.

age = 36
txt = "My name is John, and I am {}".format(age)
print(txt.format(age))
# = My name is John, and I am 36


# Insert the correct syntax to convert x into a floating point number.

x = 5
x = float(x)
print(x)
# = 5.0


# Insert the correct syntax to convert x into a integer.

x = 5.0
x = int(x)
print(x)
# = 5


# Insert the correct syntax to convert x into a complex number.
# The complex() function returns a complex number by specifying a real number and an imaginary number.


x = 5
x = complex(x)
print(x)
# = (5+0j)


# The following code example would print the data type of x, what data type would that be?

x = 5
print(type(x))
# = <class 'int'>


# The following code example would print the data type of x, what data type would that be?

x = "Hello World"
print(type(x))

# = <class 'str'>


# The following code example would print the data type of x, what data type would that be?

x = 20.5
print(type(x))

# = <class 'float'>


# The following code example would print the data type of x, what data type would that be?

x = ["apple", "banana", "cherry"]
print(type(x))


# = <class 'list'>


# The following code example would print the data type of x, what data type would that be?

x = ("apple", "banana", "cherry")
print(type(x))
# = <class 'tuple'>


# The following code example would print the data type of x, what data type would that be?

x = {"name": "John", "age": 36}
print(type(x))

# = <class 'dict'>


# The following code example would print the data type of x, what data type would that be?

x = True
print(type(x))

# = <class 'bool'>


# Check if "model" is present in the dictionary:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

if "model" in thisdict:
    print('Yes it is')

# = Yes it is


# Print all key names in the dictionary, one by one:

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict:
    print(x)


# or
# You can use the keys() method to return the keys of a dictionary:

for x in thisdict.keys():
    print(x)


# brand
# model
# year


# Print all values in the dictionary, one by one:

for x in thisdict:
    print(thisdict[x])


# or
# You can also use the values() method to return values of a dictionary:

for x in thisdict.values():
    print(x)


# Ford
# Mustang
# 1964


# Loop through both keys and values, by using the items() method:

for x in thisdict.items():
    print(x)

# ('brand', 'Ford')
# ('model', 'Mustang')
# ('year', 1964)


# or preferred way

for x, y in thisdict.items():
    print(x, y)

# brand Ford
# model Mustang
# year 1964


# Create a dictionary that contain three dictionaries:

myfamily = {
    "child1": {
        "name": "Rosa",
        "kids": 3
    },
    "child2": {
        "name": "Teresa",
        "kids": 2
    },
    "child3": {
        "name": "Isabel",
        "kids": 0
    }
}

print(myfamily)

# = {'child1': {'name': 'Rosa', 'kids': 3}, 'child2': {'name': 'Teresa', 'kids': 2}, 'child3': {'name': 'Isabel', 'kids': 0}}


# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:


child1 = {
    "name": "Rosa",
    "kids": 3
}
child2 = {
    "name": "Teresa",
    "kids": 2
}
child3 = {
    "name": "Isabel",
    "kids": 0
}


myfamily2 = {
    "child1": child1,
    'child2': child2,
    "child3": child3
}

print(myfamily2)


# = {'child1': {'name': 'Rosa', 'kids': 3}, 'child2': {'name': 'Teresa', 'kids': 2}, 'child3': {'name': 'Isabel', 'kids': 0}}


print(myfamily["child2"])
# =  {'name': 'Teresa', 'kids': 2}

# To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary:

print(myfamily["child2"]['name'])
# = Teresa


# Print First 10 natural numbers using while loop


def loops(i):
    while i <= 10:
        print(i)
        i += 1


loops(1)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10


# Write a program to print the following number pattern using a loop.

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5


def loops(rows):
    for i in range(1, rows + 1):
        for j in range(1, i+1):
            print(j, end=' ')
        print(' ')


loops(5)

# Decide the row count, i.e., 5, because the pattern contains five rows
# Run outer for loop 5 times using for loop and range() function
# Run inner for loop i+1 times using for loop and range() function
# In the first iteration of the outer loop, the inner loop will execute 1 time
# In the second iteration of the outer loop, the inner loop will execute 2 time
# In the third iteration of the outer loop, the inner loop will execute 3 times, and so on till row 5
# print the value of j in each iteration of inner loop (j is the the inner loop iterator variable)
# Display an empty line at the end of each iteration of the outer loop (empty line after each row)


# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)


def example(num):
    s = 0
    for i in range(1, num+1, 1):
        s += 1
    print('\n')
    print("Sum is: ", s)


example(int(input("Enter number: ")))


# Sum is:  55


# Write a program to print multiplication table of a given number
# ex #2


def multable(digits):
    num = 2
    counter = 0
    for i in range(1, digits + 1):
        counter = num * i
        print(counter)


multable(10)


# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# 20


# Write a program to display only those numbers from a list that satisfy the following conditions
# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the next number
# If the number is greater than 500, then stop the loop

def lst(numbers):
    for i in numbers:
        if i > 500:
            break
        elif i > 150:
            continue
        elif i % 5 == 0:
            print(i)


lst([12, 75, 150, 180, 145, 525, 50])


# 75
# 150
# 145


# Write a program to count the total number of digits in a number using a while loop.
# For example, the number is 75869, so the output should be 5. len()

def digits(number):
    counter = 0
    while number != 0:
        number = number // 10
        counter += 1
    print(counter)


digits(75869)

# = 5


def digits(number):
    print(len(str(number)))


digits(75869)


# Write a program to use for loop to print the following reverse number pattern


def loops(rows):
    for i in range(0, rows + 1):
        for j in range(rows - i, 0, -1):
            print(j, end=' ')
        print(' ')


loops(5)

# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1



#Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]
print(list1)
list1.reverse()
print(list1)

list1 = [10, 20, 30, 40, 50]
holder = []
for i in list1:
    holder = [i] + holder
print(holder)


# = [50, 40, 30, 20, 10]


list1 = [10, 20, 30, 40, 50]
# reverse list
new_list = reversed(list1)
# iterate reversed list
for item in new_list:
    print(item)
    
#50
#40
#30
#20
#10    



#Display numbers from -10 to -1 using for loop
for i in range(1,11,1):
    print(i)
    
#1
#2
#3
#4
#5
#6
#7
#8
#9
#10    
    
    
for i in range(-10,0,1):
    print(i)
    
#-10
#-9
#-8
#-7
#-6
#-5
#-4
#-3
#-2
#-1




#Use else block to display a message “Done” after successful execution of for loop
#For example, the following loop will execute without any error.


for i in range(5):
    print(i)
else:
    print('Done!')
    
#1
#2
#3
#4
#Done!



#Write a program to display all prime numbers within a range


    start = 25
    end = 50
    for num in range(n,end + 1):
        if num > 1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num)
            
     
            
#29
#31
#37
#41
#43
#47



#the Internet is a global network that connects computers around the world. 
# It allows programs running on two computers to send messages to each other. Typically, the communication occurs because one of the programs is 
# requesting a resource (a file, say) from the other. The program that is the provider of the resource is referred to as a server. 
# (The computer hosting the server program is often referred to as a server too.) The program requesting the resource is referred to as a client.

#The WWW contains a vast collection of web pages, documents, multimedia, and other resources. 
# These resources are stored on computers connected to the Internet that run a server program called a web server. 
# Web pages, in particular, are a critical resource on the web as they contain hyperlinks to resources on the web.

#A program that requests a resource from a web server is called a web client. 
# The web server receives the request and sends the requested resource (if if exists) back to the client.


#In order to request a resource on the web, there must be a way to identify it. 
# In other words, every resource on the web must have a unique name. 
# Furthermore, there must be a way to locate the resource (i.e., find out which computer on the Internet hosts the resource).
# Therefore, the web must have a naming and locator scheme that allows a web client to identify and locate resources.

#The client and server programs must communicate using an agreed-upon protocol that specifies precisely how
# the web client and the web server are supposed to format the request message and the reply message, respectively.

#In order to specify the format of a web page and incorporate hyperlinks into it, there needs to be a language that supports formatting 
# instructions and hyperlink definitions.
#These three components are called—the naming scheme, the protocol, and the web publishing language.


#Naming Scheme: Uniform Resource Locator
# In order to identify and access a resource on the web, each resource must have a unique identifier. 
# The identifier is called the Uniform Resource Locator (URL). The URL not only uniquely identifies a resource but also specifies how to access it, 
# just as a person’s address can be used to find the person. 
# For example, the mission statement of the W3C is hosted on the consortium’s web site, and its URL is the string


#http:// www.w3.org/Consortium/mission.html

#scheme       host       path

#The scheme specifies how to access the resource.
#The host (www.w3c.org) specifies the name of the server hosting the document, which is unique to each server.
#The path is the relative pathname of the document relative to a special directory at the server called the web server root directory.


#Note that the HTTP protocol is just one of many schemes that a URL may specify. 
# Other schemes include the HTTPS protocol, which is the secure (i.e., encrypted) version of HTTP.
#ex. https://webmail.cdm.depaul.edu/

# The FTP protocol, which is the standard protocol for transferring files over the Internet:
#ex. ftp://ftp.server.net/ 



#Protocol: HyperText Transfer Protocol
# A web server is a computer program that serves web resources it hosts upon request. 
# A web client is a computer program that makes such a request (e.g., your browser). 
# The client makes the request by first opening a network connection to the server (not unlike opening a file for reading and/or writing) 
# and then sending a request message to the server through the network connection (equivalent to writing to a file). 
# If the requested content is hosted at the server, the client will eventually receive—from the server and through the network 
# connection—a response message that contains the requested content (equivalent to reading from a file).

# Once the network connection is established, the communication schedule between the 
# client and the server as well as the precise format of the request and response messages is specified by the HyperText Transfer Protocol (HTTP).


#Suppose, for example, that you use your web browser to download the W3C mission statement with URL:
# http://www.w3.org/Consortium/mission.html

# The request message your web browser will send to the host www.w3.org will start with this line:
# GET /Consortium/mission.html HTTP/1.1


#The first line of the request message is referred to as the request line. 
# The request line must start with one of the HTTP methods. 
# The method GET is one of the HTTP methods and is the usual way that a resource is requested. 
# Following it is the path embedded in the resource’s URL; this path specifies the identity and location of the requested resource relative 
# to the web server’s root directory. 
# The version of the HTTP protocol used ends the request line.

#ex.
# Host: www.w3.org
# User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; ...
# Accept: text/html,application/xhtml+xml,application/xml;...
# Accept-Language: en-us,en;q=0.5


#The request header fields give the client a way to provide more information about the request
# to the server, including the character encoding and the languages (such as English) that the browser accepts, caching information, and so on.

#When the web server receives this request, it uses the path that appears in the request line to find the requested document. 
# If successful, it creates a reply message that contains the requested resource.

#The first few lines of the reply message are something like:
# HTTP/1.1 200 OK
# Date: Mon, 28 Feb 2011 18:44:55 GMT
# Server: Apache/2
# Last-Modified: Fri, 25 Feb 2011 04:22:57 GMT
# ...

#The first line of this message, called the response line, indicates that the request was successful; 
# if it were not, an error message would appear. The remaining lines, called the response header fields, 
# provide additional information to the client, such as the exact time when the server serviced the request, 
# the time when the requested resource was last modified, the “brand” of the server program, the character encoding of the requested resource, and others.

#A web page source file is written using a publishing language called the HyperText Markup Language (HTML).
# This language is used to define the headings, lists, images, and hyperlinks of a web page and incorporate video and other multimedia into it.


#Python WWW API

#Module urllib.request
#A browser is just one type of web client, however; any program can act as a web client and access and download resources on the web.
#In Python, the Standard Library module urllib.request gives developers this capability. 
# The module contains functions and classes that allow Python programs to open and read resources on the web in a way 
# similar to how files are opened and read.


#The function urlopen() in module urlib.request is similar to the built-in function open() that is used to open (local) files. 
# There are three differences however:
# 1. urlopen() takes as input a URL rather than a local file pathname.
# 2. It results in an HTTP request being sent to the web server hosting the content.
# 3. It returns a complete HTTP response.

"""
"""
from urllib.request import urlopen

response = urlopen("http://www.w3c.org/Consortium/facts.html")
type(response)

# = <class 'http.client.HTTPResponse'>

The object returned by function urlopen() is of type HTTPResponse, which is a type defined in Standard Library module http.client. 
Objects of this type encapsulate the HTTP response from the server. 
The HTTP response includes the requested resource but also additional information. 
For example, the HTTPResponse method geturl() returns the URL of the requested resource:


response.geturl()
# = 'https://www.w3.org/about/history/'


# To obtain all the HTTP response header fields, you can use method getheaders():

for field in response.getheaders():
    print(field)


=
('Date', 'Wed, 29 Nov 2023 03:03:57 GMT')
('Content-Type', 'text/html; charset=UTF-8')
('Transfer-Encoding', 'chunked')
.....




The HTTPResponse object returned by urlopen contains the requested resource. 
The HTTPResponse class is said to be a filelike class because it supports methods read(), readline(), and readlines(), the same methods 
supported by the types of objects returned by the file-opening function open(). 
All these methods retrieve the content of the requested resource. 
For example, let’s use the method read(): 


html = response.read()
type(html)
# = <class 'bytes'>



The method read() will return the content of the resource.
If the file is an HTML document, for example, then its content is returned. 
Note, however, that method read() returns an object of type bytes. 
This is because resources opened by urlopen() could very well be audio or video files (i.e., binary files). 
The default behavior for urlopen() is to assume that the resource is a binary file and, when this file is read, a sequence of bytes is returned.

If the resource happens to be an HTML file (i.e., a text file), it makes sense to decode the
sequence of bytes into the Unicode characters they represent.


html = html.decode()
type(html)
# = <class 'str'>
print(html)  # prints entire html of the web page


Decoding an HTML document into a Unicode string makes sense because an HTML document is a text file. 
Once decoded into a string, we can use string operators and methods to process the document. 
For example, we can now find out the number of times string 'Web' appears in (the source file of) web page:
http://www.w3c.org/Consortium/facts.html

html.count("Web")
# = 31


# Write a function that takes a URL of a web page as input and returns the content of the web page source file as a string:

from urllib.request import urlopen


def getSource(url):
    "returns the content of resource specified by url as a string"
    response = urlopen(url)
    html = response.read()
    return html.decode()  # returns entire html of the web page


getSource("https://www.google.com/")


# Write method news() that takes a URL of a news web site and a list of news topics (i.e.,strings)
# and computes the number of occurrences of each topic in the news.


from urllib.request import urlopen


def news(url, topics):
    # counts in resource with URL url the frequency of each topic in list topics
    # download and decode resource to obtain all lowercase content
    response = urlopen(url)
    html = response.read()
    content = html.decode().lower()

    for topic in topics:  # find frequency of topic in content
        n = content.count(topic)
        print("{} appears {} times".format(topic, n))


news("http://bbc.co.uk", ["economy", "climate", "education"])


# =

# economy appears 0 times
# climate appears 2 times
# education appears 0 times



The process of analyzing a document in order to break it into components and obtain
its structure is called parsing.
The Python Standard Library module html.parser provides a class, HTMLParser, that
parses HTML files. When it is fed an HTML file, it will process it from beginning to end, find
all the start tags, end tags, text data, and other components of the source file, and “process”
each one of them.

The HMLPParser class supports method feed() that takes, as input, the content of an
HTML source file, in string form. Therefore, to parse file w3c.html, we first need to read
it into a string and then feed it to the parser:


infile = open("w3c.html")
content = infile.read()
infile.close()
from html.parser import HTMLParser

parser = HTMLParser()
parser.feed(content)


When the last line is executed (i.e., when string content is fed to parser), this happens behind the scenes: 
The parser divides the string content into tokens that correspond to
HTML start tags, end tags, text data, and other HTML components, and then handles the
tokens in the order in which they appear in the source file. What this means is that for each token, an appropriate handler method is invoked. 
The handlers are methods of class HTMLParser.

Some HTMLParser handlers.
These methods do nothing when invoked; they need to be overridden to produce the desired behavior.

Token                                   Handler                                 Explanation
<tag attrs>                             handle_starttag(tag, attrs)             Start tag handler
</tag>                                  handle_endtag(tag)                      End tag handler
data                                    handle_data(data)                       Arbitrary text data handler



When the parser encounters a start tag token, handler method handle_starttag() is invoked; 
if the parser encounters a text data token, handler method handle_data() is invoked. 
Method handle_starttag() takes, as input, the start tag element name and a list containing the tag’s attributes 
(or None if the tag contains no attributes). 
Each attribute is represented by a tuple storing the name and value of the attribute. 
Method handle_data() takes just the text token as input.




What do the HTMLParser class handler methods (like handle_starttag()) really do?
Well, nothing. The handler methods of class HTMLParser are implemented to do nothing when called. 
That is why nothing interesting happened when we executed:

The HTMLParser class handler methods are really meant to be overridden by user-defined handlers that implement the behavior desired by the programmer. 
In other words, class HTMLParser is not supposed to be used directly but rather as a super class from which
the developer derives a parser that exhibits the parsing behavior desired by the programmer.



parser.feed(content)


# Develop a parser that prints the URL value of the href attribute contained in every anchor start tag of the fed HTML file.

from html.parser import HTMLParser


class LinkParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        "print value of href attribute if any"
        if tag == "a":  # if an anchor tag appears
            # search for href attribute and print its value
            for attr in attrs:
                if attr[0] == "href":
                    print(attr[1])


# In the next code, we feed the file to our parser and obtain the three URLs:

infile = open("links.html")
content = infile.read()
infile.close()
linkparser = LinkParser()
linkparser.feed(content)

# =
# http://www.google.com
# test.html
# mailto:me@example.net



Print the names of the start and end tags in the order that they appear in the document, and
with an indentation that is proportional to the element’s depth in the tree structure of the
document.

self = this instance of the class


from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    "HTML doc parser that prints tags indented by depth"

    def __init__(self):
        "initializes the parser and the initial indentation"
        HTMLParser.__init__(self)
        self.indent = 0  # initial indentation value

    def handle_starttag(self, tag, attrs):

        if tag in {"br", "p"}:
            print("{}{} start".format(self.indent * "", tag))
            self.indent += 4

    def handle_endtag(self, tag):

        if tag not in {"br", "p"}:
            self.indent -= 4
            print("{}{} end".format(self.indent * "", tag))


infile = open("w3c.html")
content = infile.read()
infile.close()
myparser = MyHTMLParser()
myparser.feed(content)



create a class object and assign it a name "Tweet"
A Class object is like a factory providing default behavior and it's able to create objects in its image
You can create instance objects by executing the class name for ex.("Tweet"), followed by a pair of parenthesis(calling the class)
The objects created in this way are known as instance objects
Instance objects start with a lowercase character & class objects to begin with an uppercase character
instance objects inherits any class attributes and get their own namespace



# empty body
class Tweet:
    pass


a = Tweet()

a.message = "25 wings."


if you want to access any attributes of that instance, for ex message, you can't just write message,
you need to write the instance name(a for ex) and then a dot and then the instance(message)
delineates the attributes that belong to the instance(ex. a) and those that belong elsewhere
i've assigned a string to the instance attribute message and I access it the same way as we assigned to it



print(a.message)
# = 25 wings.



We get an attrribute error because it's as if the class object is a factory that provides default behavior and 
when we create instance objects, we're getting items that we can change and any changes that we make 
are not then propagated back up to the factory.
they stay with the instance and die with the instance



print(Tweet.message)
# = attribute error, Tweet class object was never modifed, only it's instance objects


# We can create as many of these instance objects as we like

b = Tweet()
# another instance object assigned to 'b'
b.message = "A different message"


# demonstrate that 2 message attributes are different but exist at the same time and are accessed through their respective namespace
print(a.message)
# 25 wings.
print(b.message)
# A different message

Methods that begin with double underscores(ex. __) and end in double underscores are special hooks in Python
Known as Dunder Method 
Method is called automatically at certain times
Classes can override most of them


init method
whenever we call class objects, the instance object is first created with the dunder method and then
any attributes are initialzed with the dunder init method
Dunder init method is best known as the initializer method, although mostly referred as the constructor method
Called automatically whenever an instance is created




Overridden the dunder init method and have it print hi
Defining dunder init without any parameters is not what you normally see
normally see self as the first parameter


class Tweet:
    def __init__(self):
        print("Hi")


a = Tweet()
# = 'Hi'


Whenever the class object is called the instance is always passed as the first argument
init method is there to perform any initialization & make assignments to instance attributes
Self in a class definition always refers to the particular instance
Any other argumets that we pass in, will take up positions 2,3,4,etc



class Tweet:
    def __init__(self, message):
        self.x = message


a = Tweet("An instance")
print(a.x)
# = An instance



Created a seperate instance of the same class & passed in a diff. string
both instances coexists


b = Tweet("Another instance of Tweet")
print(b.x)
# = Another instance of Tweet



Module urllib.parse
What if we are only interested in collecting the URLs that correspond to HTTP hy-
perlinks (i.e., URLs whose scheme is the HTTP protocol)?
Note that we cannot just say “collect those URLs that start with string http” because then we would miss the relative
URLs, such as /Consortium/contact.html.
What we need is a way to construct an absolute URL from a relative URL (like /Consortium/contact.html) and the URL of the
web page containing it (http://www.w3.org/Consortium/mission.html).
The Python Standard Library module urllib.parse provides a few methods that operate on URLs, 
including one that does exactly what we want, method urljoin().

urllib.parse.urljoin(base, url)

Relative Urls-don't contain the full web address
Generally used to link to resources within the same website

    Path-Relative URL-File being linked is in the same folder as your HTML doc, then name of the file is listed
    -If file is in the subfolder, then just include the subfolder before the file name
    -Problem is that they can easily be broken
    ex. <a href = "page2.html"> Page 2 </a>
    
    
    Root-Relative URLs-Start with a slash "/"
    -Always relative to the route of the site
    -If file is in the subfolder, then just include the subfolder before the file name and start with a "/"
    -From a developer's POV, relative URLS is the easiest and simplest thing to do
    -Useful when moving code between servers & less likely to break
    ex. <a href = "/page2.html"> Page 2 </a>
    
    
    Protocol-Relative URLs include the hostname but the protocol isn't
    -Start with a double slash "//"
    -Browser uses whatever protocol is used by the page that contains the link
    -They're best avoided
    -Vulnerable to hacking
    -Slower than absolute URLs
    -May not load if you're using HTTP2 
    ex. If site uses HTTP then this is the protocol that will be used in the request the resources
    ex. If it's using HTTPS then the requested URS will use HTTPS
    ex. < link rel = "stylesheet" href = "//cdn.example.com/theme.css">



from urllib.request import urlopen

rsrce = urlopen("https://www.w3.org/mission/")
content = rsrce.read().decode()
linkparser = LinkParser()
linkparser.feed(content)


from urllib.parse import urljoin

url = "http://www.w3.org/Consortium/mission.html"
relative = "/Consortium/contact.html"
urljoin(url, relative)
# = 'https://www.w3.org/Consortium/contact.html'



the first argument, base is like the page you are on in your browser. The second argument url is the href of an anchor on that page. 
The result is the final url to which you will be directed should you click.
If url is an absolute URL (that is, starting with //, http://, https://, ...), 
the url’s host name and/or scheme will be present in the result. For example:


from urllib.parse import urljoin

url = "https://www.google.com"
relative = "//www.microsoft.com"
urljoin(url, relative)
# 'https://www.microsoft.com'


import urllib.parse

urllib.parse.urljoin("https://www.google.com", "//www.microsoft.com")
# 'https://www.microsoft.com'



Parser That Collects HTTP Hyperlinks
Collect only HTTP URLs and, instead of printing them out, it puts them into a list.
The URLs in the list will be in their absolute, rather than relative, format.


from urllib.request import urlopen
from urllib.parse import urljoin
from html.parser import HTMLParser


class Collector(HTMLParser):
    "collects hyperlink URLs into a list"

    def __init__(self, url):
        "initializes parser, the url, and a list"
        HTMLParser.__init__(self)
        self.url = url
        self.links = []

    def handle_starttag(self, tag, attrs):
        "collect hyperlink URLs in their absolute format"
        if tag == "a":
            # This loop iterates over the attribute-value pairs of the anchor tag.
            for attr in attrs:
                # This condition checks if the attribute is the "href" attribute, which typically contains the URL of the hyperlink.
                if attr[0] == "href":
                    # construct absolute URL
                    absolute = urljoin(self.url, attr[1])
                    if absolute[:4] == "http":  # collect HTTP URLs
                        self.links.append(absolute)

    def getLinks(self):
        "returns hyperlinks URLs in their absolute format"
        return self.links


url = "http://www.w3.org/Consortium/mission.html"
resource = urlopen(url)
content = resource.read().decode()
collector = Collector(url)
collector.feed(content)
for link in collector.getLinks():
    print(link)


 
http://www.w3.org/Consortium/mission.html#main
https://github.com/w3c/w3c-website
https://www.w3.org/ja/
.....


Using attr[0] would give you the name of the attribute, and in this case, it checks if the attribute is "href." 
However, to actually get the value of the "href" attribute (which is the URL you're interested in), you need to use attr[1].

In this example, attr[0] would be "href" (the name of the attribute).
attr[1] would be "http://www.w3.org/Consortium/mission.html (the value of the "href" attribute).



# Augment class Collector so that it also collects all the text data into a string that can be retrieved using method getData().


from urllib.parse import urljoin
from html.parser import HTMLParser
from urllib.request import urlopen


class Collector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.words = ""

    def handle_data(self, data):
        "collects and concatenates text data"
        self.words += data

    def getData(self):
        "returns the concatenation of all text data"
        return self.words


url = "http://www.w3.org/Consortium/mission.html"
resource = urlopen(url)
content = resource.read().decode()
collector = Collector()
collector.feed(content)
print(collector.getData())


# prints all text data from the url

from html.parser import HTMLParser
from urllib.request import urlopen


class Collector(HTMLParser):
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.links = []
        self.data = ""

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for attr, value in attrs:
                if attr == "href":
                    self.links.append(value)

    def handle_data(self, data):
        self.data += data

    def getData(self):
        return self.data


# Example usage:
url = "http://www.w3.org/Consortium/mission.html"
resource = urlopen(url)
content = resource.read().decode()

collector = Collector(url)
collector.feed(content)

# Get links
print("Links:", collector.links)

# Get data
print("Data:", collector.getData())



In this modified class, I added a data attribute to store the text data, and in the handle_data method, 
I append the data to this attribute. 
The getData method is then used to retrieve the collected text data.


# GET
import urllib.request
import urllib.parse

# x = urllib.request.urlopen("https://www.google.com/")
# print(x.read())
# Prints The source code of the URL google.com


url = "https://pythonprogramming.net/"
values = {"q": "python"}  # dictionary

data = urllib.parse.urlencode(values)  # encoding as it should be in the url
data = data.encode("utf-8")  # encode as utf-8(type of encoding). Puts data into bytes
# Requesting the url and data(encoded the data and it into utf-8. Passing variables in value that was encoded)
request = urllib.request.Request(url, data)
response = urllib.request.urlopen(request)  # visiing the url now
respData = response.read()

print(respData)
# Prints The source code of the URL https://pythonprogramming.net/search/?q=python


import urllib.request
import urllib.parse


try:
    x = urllib.request.urlopen(
        "https://www.google.com/search?q=test"
    )  # Q stands for query for google
    print(x.read())  # Read the source code of the url search resut

except (
    Exception
) as e:  # If we can't read the source code of the url, then throw the exception as e
    print(str(e))  # print the string version of exception

# = HTTP Error 403: Forbidden
# Google knows I'm a program so they decline the request


import urllib.request
import urllib.parse


try:
    url = "https://pythonprogramming.net/search/?q=python"
    headers = {}  # Send in a header every time I visit a site & it contains info on me
    ""Piece of data called User-Agent Located within headers. User-Agent reveals what kind of browser I'm on, which is Python...
    I'm no longer announcing myself as Python & switching u-agent to an internet browser""
    headers[
        "User-Agent"
    ] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
    ""URL Being hardcoded, so no data needs to be passed through. Normally pass in values in post req
    # telling Python to visit url & instead of setting our normal default parameterheaders, I'm changing things up and calling the
    headers where I switched the user agent to an internet browser
    Makes sense to go into urllib.request.Request that is a function with function parameters & they define the new internet browser instead of
    default parameters
    ""
    req = urllib.request.Request(url, headers=headers)
    resp = urllib.request.urlopen(req)
    respData = resp.read()

    saveFile = open("withHeaders.txt", "w")  # open the file with the intention to write
    saveFile.write(
        str(respData)
    )  # Have to write the string version of respData because the response data isn't in string format
    saveFile.close()

except Exception as e:
    print(str(e))  # Print string e in case we throw an exception

# created data file of The source code of the URL "https://pythonprogramming.net/search/?q=python"


import urllib.request
import urllib.parse
import re  # regular expressions


url = "http://pythonprogramming.net"
values = {"s": "search", "submit": "search"}

data = urllib.parse.urlencode(values)
data = data.encode("utf-8")
req = urllib.request.Request(url, data)
resp = urllib.request.urlopen(req)
respData = resp.read()

# print(respData)
# prints source code of the URL "https://pythonprogramming.net/search/?q=python"


# about to parse out everything between paragraph tags


 r = regular expression we want is paragraph text
() in between tags is what data you want to search for and output
.*? = find everything between paragraph tags
. = any character except for new line
* = zero or more repititions of the regular expression immediately
preceding it., it applies to the "." here
? = match the zero or more repititions of the regular expression immediately
preceding it.
Looking for this in respData and it needs to be converted into a string

paragraphs = re.findall(r"<p>(.*?)</p>", str(respData))

for eachP in paragraphs:
    print(eachP)


Each of the listed cases gives a regular expression and a set of strings. Select those strings
that are matched by the regular expression.
Regular Expression              Strings
(a) [Hh]ello                    ello, 

Hello, hello



(b) re-?sign                    re-sign, resign, re-?sign

re-sign, resign,



(c) [a-z]*                      aaa, Hello, F16, IBM, best


aaa, best


(d) [^a-z]*                     aaa, Hello, F16, IBM, best


F16, IBM,

(e) <.*>                        <h1>, 2 < 3, <<>>>>, ><


<h1>, <<>>>>, 

"""


"""
For each of the listed informal pattern descriptions or sets of strings, define a regular ex-
pression that fits the pattern description or matches all the strings in the set and no other.

(a) aac, abc, acc

a[abc]c


(b) abc, xyz


abc|xyz

(c) a, ab, abb, abbb, abbbb, . . .

a[b]*


(d) Nonempty strings consisting of lowercase letters in the alphabet (a, b, c, . . . , z)

[a-z]+

(e) Strings containing substring oe


[a-zA-Z]*oe[a-zA-Z]*

(f) String representing and HTML start or end tag


<[^>]*>

< Matches the opening angle bracket <.
[^>]* Matches zero or more characters that are not the closing angle bracket >.
> Matches the closing angle bracket >.


"""


""" 
Python Standard Library Module re


The module re in the Standard Library is Python’s tool for regular expression processing.
One of the methods defined in the module is method findall() that takes two inputs, a
regular expression and a string, and returns a list of all substrings of the input string that the
regular expression matches.




from re import findall

findall("best", "beetbtbelt?bet, best")
# ["best"]


findall("be.t", "beetbtbelt?bet, best")
# ["beet", "belt", "best"]


findall("be?t", "beetbtbelt?bet, best")
# ["bet","bt",]


findall("be*t", "beetbtbelt?bet, best")
# ["beet", "bt", "bet"]


findall("be+t", "beetbtbelt?bet, best")
# ["beet", "bet"]


# If the regular expression matches two substrings such that one is contained in the other, the function findall() will match the longer substring only.


findall("e+", "beeeetbet bt")
# ["eeee", "e"]



If the regular expression matches two overlapping substrings, the function findall() returns the left one. 
The function findall() in fact scans the input string from left to right and collects matches into a list in the order found.



findall("[^bt]+", "beetbtbelt?bet, best")
# ['ee', 'el', '?', 'e', ',', 'es']


findall("[bt]+", "beetbtbelt?bet, best")
# ['b', 'tbtb', 't', 'b', 't', 'b', 't']



Develop function frequency() that takes a string as input, computes the frequency of every
word in the string, and returns a dictionary that maps words in the string to their frequency.
You should use a regular expression to obtain the list of all words in the string.



from re import findall

content = "The pure and simple truth is rarely pure and never simple."


def frequency(content):
    pattern = "[a-zA-Z]+"
    # Use the findall function to find all occurrences of the defined pattern in the content string. This returns a list of words.
    words = findall(pattern, content)
    dictionary = {}

    for word in words:
        if word in dictionary:  # counter for word exists
            dictionary[word] += 1
        else:  # counter for word doesn't exist
            dictionary[word] = 1

    return dictionary


frequency(content)

# = {'The': 1, 'pure': 2, 'and': 2, 'simple': 2, 'truth': 1, 'is': 1, 'rarely': 1, 'never': 1}


search(). 
It also takes a regular expression and a string; it returns the first substring that is matched by the regular expression.
You can think of it as a more powerful version of string method find().



from re import search

match = search("e+", "beetbtbelt?bet")
type(match)
# = <class 're.Match'>



Method search returns a reference to an object of type SRE_Match, informally referred to as a match object. 
The type supports, for example, methods to find the start and end index of the match in the input string:
starts at index 1 and ends before index 3.


match.start()
# = 1
match.end()
# = 3

# Match objects also have an attribute variable called string that stores the searched string:

match.string
# = 'beetbtbelt?bet'

# To find the matched substring, we need to get the slice of match.string from index match.start() to index match.end():

match.string[match.start() : match.end()]  # 1:3
# = 'ee'


search("e+", "beetbtbelt?bet")
# <re.Match object; span=(1, 3), match='ee'>

from re import findall
[ab]
ab, a, b, the empty string


a.b.
ab, acb, acbc, acbd

a?b?
ab, a, b, the empty string

a*b+a*
aa, b, aabaa, aaaab, ba
          
[^\d]+
abc, 123, ?.?, 3M


For each informal pattern description or set of strings below, define a regular expres-
sion that fits the pattern description or matches all the strings in the set and no other.

#Strings containing an apostrophe (’)
#    .*'.*

#Any sequence of three lowercase letters in the alphabet
#   [a-z]{3}

The string representation of a positive integer
[1-9]+


The string representation of a nonnegative integer 
\d+



The string representation of a negative integer
-[1-9]+

The string representation of an integer (whether positive or not)
-?[1-9]+|\d+
-?\d+


The string representation of a floating-point value using the decimal point notation
-?\d+\.\d*

-?+\.\+





For each informal description listed next, write a regular expression that will match all the strings in file frankenstein.txt that match the description. Also find out the answer using the findall() function of the module re.
"""


#The enumerate() function is used to loop over the lines of the file while also keeping track of the line number (i) for each line.


#String ‘Frankenstein’
import re

for i, line in enumerate(open("frankenstein.txt")):
    for match in re.findall("Frankenstein",line):
        print(match)
print("\n")


-?\d+
#Numbers appearing in the text
import re

for i, line in enumerate(open("frankenstein.txt")):
    for match in re.findall(r"\d",line):
        print(match)
print("\n")


#Words that end with substring ‘ible’
import re

for i, line in enumerate(open("frankenstein.txt")):
    for match in re.findall(r'\b(\w+ible)\b',line):
        print(match)
print("\n")


#Words that start with an uppercase and end with ‘y’
import re

for i, line in enumerate(open("frankenstein.txt")):
    for match in re.findall(r'\b[A-Z][a-zA-Z]*y\b',line):
        print(match)
print("\n")

"[A-Z][A-Za-z]*\w+y"


#List of strings of the form ‘horror of <lowercase string> <lowercase string>’

import re

for i, line in enumerate(open("frankenstein.txt")):
    for match in re.findall(r'\bhorror of + [a-z]+ [a-z]+\b',line):
        print(match)
print("\n")



#Expressions consisting of a word followed by the word ‘death’

for i, line in enumerate(open("frankenstein.txt")):
    for match in re.findall(r'\bw+ death\b',line):
        print(match)
print("\n")



#Sentences containing the word ‘laboratory’

for i, line in enumerate(open("frankenstein.txt")):
    for match in re.findall(r'\b.*?laboratory.*?\.',line):
        print(match)
print("\n")
