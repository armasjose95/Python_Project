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
