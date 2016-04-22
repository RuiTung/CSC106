

import random
from random import randint
playing =True
num = randint (1, 100)
guesses = 0
print "Let's playing Guessing Game."
print "What I need you to do is just guess guess guess."
print "What is your guessing number?"
while(playing):
    print "Please enter a number between 1 and 100"
    guess = int(raw_input("What is your gueesing number?"))
    if (guess > 100 or guess < 1):
        invalid = True
        while(invalid):
            print "This is an invalid value. Please enter a number between 0 - 100."
            guess = int(raw_input("What is your guessing number?"))
            if (100 >= guess >= 1):
                invalid = False
    if (guess == num):
        print "Bingo! Congratulations!"
        playing = False
    elif (guess > num):
        print "It's too high. Please try again.^_^"
    else:
        print "It's too low. Please try again. Don't give up.↖(^ω^)↗"

answer = str(raw_input("Do you think our Python Guessing game is funny? yes or no? "))
if (answer == "yes"):
    print "Thank you very much!~O(∩_∩)O~"
else:
    print "Just give us a break......please.⊙﹏⊙"
                 
                    




# Pros
# 1. Readability. Python is easy to read and use. 
#    There is not so many grammers and there is no need to set variable type. 
#    It looks like a pseudocode.
# 2. Free and open source. Users can read source code and change it.
# 3. Interpretation. Python is easy to compile on any computer. 
#    There is no need to worry about compiler.
# 4. Extendibility. If there is something important code that users do not want to share with it, 
#    users can wirte part of code with C/C++, then use is on Python's program.

# Cons
# 1. Single Line statement. Users cannot put progress into one line.
# 2. The running speed of Python is lower than C and C++;
# 3. Ident. The ident is the limit of Python. 
#    Because the only way to distinguish the logic relationship is ident.
#    The normal error is confusing "space" and "tab", 
#    and the error cannot distinguished by naked eye.

# Comparison of Python and Scratch
# We prefer Python to Scratch.
# Reasons:
# 1. Although Scratch is more fun, it needs more efforts to finish a project. 
#    Such as, background music, different costumes, etc. 
#    Python is just need us focus on the code.
#    Python makes us feel more comfortable than Scratch.
# 2. Pathon is more professional than Scratch. 
#    Scratch is disigned for kids, and which is not suitable for us.
# 3. Scratch do not have so many loops, which cannot satisfied some requirements perfectly.
#    (e.g. check user's entered letters, or a decimal value, instead of an integer for guessing game.) 
#    For instance, it does not have while loop, and we can just use if/if else, 
#    repeat until to meet requirement.

# Pair Programming
# 1. Pros. Through pair programming, the division of labor is clear. 
#    Both of us are charge of specific responsibilities. 
#    Drivers is charge of code and navigator is charge of checking. 
#    Our work efficiency can be promoted.
# 2. Cons. When we have different opinions, 
#    we have to spend much more time to make disgussions, 
#    becuase when there are different opnions we have to switch our roles frequently.





