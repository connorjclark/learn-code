# In Python, lines starting with a hashtag are comments.
# Comments don't do anything. Python ignores them.
# Their only purpose is for the programmer to leave notes
# about the code.

# FYI: Repl.it is a good site for experimenting with a language.
# It's like a scratchpad.

# Variables contain values. Once a variable is defined:
a = 1

# # It can be used.
b = a + 1.5

# Variable names can be of any length, must start with a letter or an underscore, and may contain numbers.
# a-z A-Z 0-9 _

# By convention, in Python, words within a variable name are separated with _
i_am_valid = 1
i_am_valid_too123 = 1
_i_am_valid_aswell = 1
thisWorksItJustIsntConventionalStyle = 1

# Invalid variable names are a syntax error, which means the program can not run at all. So we comment it out.
# 0iamnotvalid = 1

# If you attempt to use a variable before it is defined,
# an error occurs.
# c = d
# NameError: name 'd' is not defined

# When an error occurs, the program stops. Unless the error is caught and handled, the program will not continue. We'll cover that later - for now, we just comment out line 14 so that the program will continue.

# Typical math stuff.
c_sum = a + b
c_difference = a - b
c_product = a * b
c_division = a / b

# Once a variable is defined, you can redefine it easily.
d = 1
d = 2

# You can add to a variable number by reassigning.
d = d + 1 # d is equal to 3

# There's a shorthand, too.
d += 1 # d is equal to 4

# Number aren't the only thing variable can contain.

# They can contain boolean values.
is_alive = True
is_old = False

# They can contain strings.
# Strings are wrapped in quotes (either "", or '')
first_name = 'connor'
last_name = 'clark'

# You can add strings.
full_name = first_name + ' ' + last_name

# Question: what happens if you subtract strings?
# full_name = first_name - ' ' - last_name

# Writing code to add many strings together can be tedious to write, and hard to read.
# Programming languages solve this problem with "string interpolation", which just
# means, injecting variables into strings.
# In Python, "f-strings" do this.
full_name = f"{first_name} {last_name}"
age = 10
weight = 100

# bio = "His name is " + full_name + ", and he is " + str(age) + "years old at " + str(weight) + "kilos"
bio = f"His name is {full_name}, and he is {age} years old at {weight} kilos"

# Running different code based on a condition is done by using "if"
if age >= 18:
  can_drink = True
else:
  can_drink = False

# Note: A simpler way to write this is:
# can_drink = age >= 18

if can_drink:
  # `can_drink` was set to False, so this condition fails,
  # and the following line of code does not run.
  weight += 20



# Note that '=' has been used so far to mean "assign this variable to this value". For conditions that check that two values are equal, you must
# use "==".
if weight == 100:
  print('you weigh a hundred pounds!')

# If you want to do something many times, use a "while loop".
i = 0
while i < 10:
  i += 1
  age += 1

# You can print stuff by using the "print" function.
print(age) # 20
print(bio) # Question: Why doesn't this say "20 years old"?

# You can re-use code by using functions.
# A function is just some code that takes some input (the arguments)
# and possibly returns one value.
def say_hello(who):
  print(f'say hello to {who}!')

say_hello('my little friend')
say_hello('my fists')

def invest_money(some_money, years):
  if years > 5:
    print('wow! that is a long time!')

  return some_money - years * 10

my_money = 100
money_after_investing = invest_money(my_money, 1)
print(money_after_investing) # Question: what is this equal to?
print(my_money) # And this?

my_money = invest_money(my_money, 10)
print(my_money) # And this?

# So that covers variables, numbers, strings, if, while, and functions.
# Take a few moments to complete this challenge:
# Make a function that takes a number, prints every numbers from 0
# to the given number, and also prints "Cool!" for my favorite numbers,
# 7, 14, 21, and 32.

# count(10)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# Cool!
# 8
# 9
# 10

# Good news! All of this is common to most languages, including: JavaScript, C++, Ruby, C#, PHP, ... In fact, most programming languages share ~90% of the same ideas, with perhaps slightly different syntax. Your first language is the hardest. The rest is an excercise in syntax.
