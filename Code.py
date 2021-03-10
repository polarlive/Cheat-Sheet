''' # Python

-Variables and data types-

print("    /|")
print("   / |")
print("  /  |")
print(" /___|")

character_name = "Sam"
character_age = "23"

print("There once was a man named " + character_name+".")
print("He did not like being " + character_age+".")

-Booleans-

is_male = True
is_male = False

-Working with strings-

print("John")
print("Jo\n" "hn")

phrase = "John"
#         0123

print(phrase)
print(phrase + " is cool")

print(phrase.upper())
print(phrase.lower())

print(phrase.isupper())
print(phrase.islower())

print(phrase.upper().isupper())

print(len(phrase))
print(phrase[0])

print(phrase.index("P"))
print(phrase.index("Pol"))
print(phrase.index("ar"))

print(phrase.replace("Polar", "John"))

-Working with numbers-

print(2)
print(-2.03)
print(3+4.5)

print(3 * (4+5))
print(10 % 3)

my_num = 5
print(my_num)
print(str(my_num) + " my favorite number")

from math import *

my_num = -5
print(abs(my_num))
print(pow(4, 6))

print(max(4, 6))
print(min(4, 6))

print(round(3.2))

print(floor(3.7))
print(ceil(3.7))
print(sqrt(36))

-Getting input from users-

name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)

-Building a basic calculator-

num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)
result = int(num1) + int(num2)

print(result)

-Mad libs game- 

color = input("Enter a color: ")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)

-Lists-

friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
              0        1       2       3       4

friends[1] = "Mike"
print(friends[1])

[1:3] Takes the select bunch

-List functions-

lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Jim", "Oscar", "Toby"]

friends2 = friends.copy()

friends.extend(lucky_numbers)
friends.append("Adam")
friends.insert(1, "Kelly")
friends.remove("Kevin")
friends.clear
friends.pop()
friends.sort()

lucky_numbers.sort()
lucky_numbers.reverse()

print(friends)
print(friends2)
print(friends.index("Kevin"))
print(friends.count("Jim"))

-Tuples-

coordinates = [(4, 5), (6, 7) (80, 34)]
print(coordinates[0])

-Functions-

def say_hi(name, age):
    print("Hello " + name + ", you are " + age)

say_hi("Mike", "35")
say_hi("Steve", "70")

-Return Statement-

def cube(num):
    return num*num*num

result = cube(4)
print(result)

-If statements-

is_male = False
is_female = False

if is_male and is_female:
    print("You are both a human")
elif is_male and not(is_female):
    print("The male is a human, The female is not")
elif is_female and not(is_male):
    print("The female is a human, The male is not")
else:
   
 print("Neither of you are humans")

-If statements and Comparisons-

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

print(max_num(3, 4, 5))

def best_body(part1, part2, part3):
    if part1 >= part2 and part1 >= part3:
        return part1
    elif part2 >= part1 and part2 >= part3:
        return part2
    else:
        return part3

print(best_body(1, 2, 3))

-Building a better calculator-

num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op== "*":
    print(num1 * num2)
elif op== "/":
    print (num1 / num2)
else: 
    print("Invalid Error")

-Dictionaries-

monthConversions = {
    0: "January",
    1: "February",
    2: "March",
    3: "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",   
}

print(monthConversions["Apr"])
print(monthConversions.get("oof", "Not a Valid key"))

-While loop-

i = 1
while i <= 10:
    print(i)
    i = i + 1

print("Done with loop")

num1 = 1
while num1 <= 14:
    print(num1)
    num1 = num1 + 1

-Building a guessing game-

secret_word = "polar"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
         guess = input("enter guess: ")
         guess_count += 1
    else:
         out_of_guesses = True
    
if out_of_guesses:
     print("You lost.")
else:
     print("Congrats, you got it!!!")

-For Loop-

friends = ["Michael", "Lily", "Poki", "Toast"]

for name in friends:
    print(name)

for index in range(10):
    print(index)
    
for index in range(3, 10):
    print(index)

for index in range(len(friends)):
    print(friends[index])
    friends[1]

for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")

-Exponent Function-

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(3, 3))

-2D lists and nested loops-

num_grid = [
    [1, 2, 3], #0
    [4, 5, 6], #1
    [7, 8, 9], #2
    [0]        #3
    #0  1  2
]

print(num_grid[0][2])

for row in num_grid:
    for col in row:
        print(col)

-Build a translator-

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeiouAEIOU":
            if letter.isupper():
                translation = translation + "P"
            else:
                translation = translation + "p"
        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

-Try Except-

try:
    number = int(input("Enter a number: "))
    print(number)
except:
    print("USE A FUCKING NUMBER!")

try:
    dbz = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as Error:
    print(Error)
except ValueError:
    print("Invalid input")

-Reading Files-

open("employees.txt", "r" ) # Read File
open("employees.txt", "w" ) # Write File
open("employees.txt", "a" ) # Append File
open("employees.txt", "r+" ) # Read/Write File

employee_file = open("employees.txt", "r")
print(employee_file.read())
employee_file.close()

employee_file = open("employees.txt", "r")
print(employee_file.readlines())
employee_file.close()

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print (employee)
employee_file.close()

-Writing Files-

employee_file = open("employees.txt", "a")
employee_file.write("\nKelly")
employee_file.close()

employee_file = open("employees.txt", "w")
employee_file.write("\nKelly")
employee_file.close()

-Modules and Pip-

import useful_tools
print(useful_tools.roll_dice(10))

-Classes and Objects- 

from Student import Student

student1 = Student("Jack", "Buisness", 3.1, False)
student2 = Student("John", "Art", 3.5, True)
print(student2.gpa)

-Building a Multiple Choice Quiz-

from Question import Question

question_prompts = [
    "How many subscribers does Polar have?\n(a) 30\n(b) 1000\n(c) 21\n(d) 1\n\n",
    "How old is Polar?\n(a) 3\n(b) 18\n(c) 20\n(d) 14\n\n",
    "How cool is Polar?\n(a) 10%\n(b) 100%\n(c) 0%\n(d) 1%\n\n",
]

questions = [
    Question(question_prompts[0], "c"),
    Question(question_prompts[1], "d"),
    Question(question_prompts[2], "b")
    

]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)
'''
