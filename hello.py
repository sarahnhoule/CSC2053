import math
import code
from re import A

print("hello world!")
#this is a comment
'this is also a comment'
'''
use this for several lines of comment
'''
# code1
# codepoint2namec
# code 3
# code 4 commented using control + forward slash

int_example = 5
float_example = 5.5
result = 5.5 // 4
print(result)

result = 5.5 % 4
print(result)

squared = 5**2
print(squared)

abs_value = abs(-5.5)
print(abs_value)

x = 10
y = 100

if x>=10 or y<=100:
    print("at least one of the statements is true")
    print("this is a statement block")

grade = 72
if grade>=90:
    letter = 'A'
elif grade >=90:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
else:
    letter = 'D'

print(letter)

x = 5;
x = 'now x is a string'


#slice a string
first_name = 'Sarah'
first_two_chars=first_name[0:2]
print(first_two_chars)

if 'S' in first_name:
    print('There is an S in your first name')

    for i in range(len(first_name)):
        print(first_name[i])
        if first_name[i] == 'a': print('I found an a')

#default argument:
def hello_default_arg(name="To whom it may concern"):
    print("Hello",name)
def return_two():
    return 1,5

x, y = return_two()
print(x,y)
x = return_two()
print(x)