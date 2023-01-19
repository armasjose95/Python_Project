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
poisonous = flowers[-1]
print(poisonous)  # = lilly of the valley
# (e) Assign to list dangerous the concatenation of lists thorny and poisonous.
dangerous = [thorny] + str(poisonous)
print(dangerous)

dangerous = str[thorny] + str(poisonous)
print(dangerous)


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
# List of Words =['Spider', 'Man']
print(f'List of Words ={anotherList.split()}')

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
