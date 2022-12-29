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
