import os

# Base Directory
BASE_DIR = "Code"

# Helper Function to Create Files
def create_file(module, filename, content):
    path = os.path.join(BASE_DIR, module)
    os.makedirs(path, exist_ok=True)
    
    full_path = os.path.join(path, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {full_path}")

# ==========================================
# MODULE 4: Strings
# ==========================================
m4 = "04_Strings"

create_file(m4, "01_create_string.py", """# 1. Create String
# ==========================================
# CONCEPT: Text Data
# ==========================================
# Strings are sequences of characters enclosed in quotes.

s = 'Hello'
print(s)

# Why? To store names, addresses, messages, etc.
""")

create_file(m4, "02_quotes.py", """# 2. Quotes
# ==========================================
# CONCEPT: Flexibility
# ==========================================
# Use single (') or double (") quotes. 
# Useful if your string contains a quote.

s1 = "I 'love' Python"
s2 = 'I "love" Python'

print(s1)
print(s2)
""")

create_file(m4, "03_multiline.py", """# 3. Multiline Strings
# ==========================================
# CONCEPT: Big Text
# ==========================================
# Use triple quotes (''' or \"\"\") for text spanning multiple lines.

s = '''Line 1
Line 2
Line 3'''

print(s)
""")

create_file(m4, "04_indexing.py", """# 4. Indexing
# ==========================================
# CONCEPT: Position
# ==========================================
# We can grab a single character using its position (Index).
# Computers start counting at 0!

s = 'Python'
# P  y  t  h  o  n
# 0  1  2  3  4  5

print(s[0]) # P
print(s[5]) # n
""")

create_file(m4, "05_negative_indexing.py", """# 5. Negative Indexing
# ==========================================
# CONCEPT: Counting Backwards
# ==========================================
# -1 is the last item. -2 is the second to last.

s = 'Python'
print(s[-1]) # n
print(s[-2]) # o
""")

create_file(m4, "06_slicing.py", """# 6. Slicing [Start:Stop]
# ==========================================
# CONCEPT: Extraction
# ==========================================
# Grab a chunk of text.
# Start is inclusive. Stop is exclusive (not included).

s = 'Python'
print(s[0:2]) # 'Py' (Indices 0, 1. Stop at 2)
print(s[2:])  # 'thon' (From 2 to end)
print(s[:2])  # 'Py' (From start to 2)
""")

create_file(m4, "07_slice_steps.py", """# 7. Slicing with Steps
# ==========================================
# CONCEPT: Skipping
# ==========================================
# [Start : Stop : Step]

s = 'Python'
print(s[::2]) # 'Pto' (Every 2nd char: 0, 2, 4)
""")

create_file(m4, "08_reverse_string.py", """# 8. Reversing a String
# ==========================================
# CONCEPT: Step -1
# ==========================================
# A negative step allows us to walk backwards.

s = 'Python'
print(s[::-1]) # 'nohtyP'
""")

create_file(m4, "09_immutability.py", """# 9. Immutability
# ==========================================
# CONCEPT: Unchangeable
# ==========================================
# Once created, a string cannot be changed in place.
# You must create a NEW string.

s = 'Hello'
# s[0] = 'J' # TypeError: 'str' object does not support item assignment

s = 'J' + s[1:] # New string 'Jello'
print(s)
""")

create_file(m4, "10_concatenation.py", """# 10. Concatenation (+)
# ==========================================
# CONCEPT: Gluing Strings
# ==========================================
# Adding strings together.

first = "Hello"
space = " "
last = "World"

print(first + space + last)
""")

create_file(m4, "11_f_strings.py", """# 11. f-strings
# ==========================================
# CONCEPT: Formatting
# ==========================================
# The best way to inject variables into strings.
# Put an 'f' before the quote and use {}.

name = "Bob"
age = 30
print(f"Hi {name}, you are {age}.") 

# Common Error: Forgetting the 'f' prints "{name}" literally.
""")

create_file(m4, "12_string_methods_upper.py", """# 12. Upper Case
# ==========================================
# CONCEPT: Transformation
# ==========================================

s = "hi"
print(s.upper()) # "HI"
""")

create_file(m4, "13_string_methods_lower.py", """# 13. Lower Case
# ==========================================
# CONCEPT: Transformation
# ==========================================

s = "HI"
print(s.lower()) # "hi"
""")

create_file(m4, "14_strip.py", """# 14. Strip
# ==========================================
# CONCEPT: Cleaning
# ==========================================
# Removes whitespace from start and end.

s = "  password123  "
clean = s.strip()
print(f"'{clean}'")
""")

create_file(m4, "15_replace.py", """# 15. Replace
# ==========================================
# CONCEPT: Find and Swap
# ==========================================

s = "I like Apples"
print(s.replace("Apples", "Bananas"))
""")

create_file(m4, "16_split.py", """# 16. Split
# ==========================================
# CONCEPT: String to List
# ==========================================
# Breaks a string into pieces based on a delimiter.

data = "apple,banana,cherry"
items = data.split(",") # ['apple', 'banana', 'cherry']
print(items)
""")

create_file(m4, "17_join.py", """# 17. Join
# ==========================================
# CONCEPT: List to String
# ==========================================
# The reverse of split.

items = ['apple', 'banana', 'cherry']
text = "-".join(items)
print(text) # "apple-banana-cherry"
""")

create_file(m4, "18_find.py", """# 18. Find
# ==========================================
# CONCEPT: Searching
# ==========================================
# Returns the index of the first occurrence. Returns -1 if not found.

s = "banana"
print(s.find("a")) # 1
print(s.find("z")) # -1
""")

create_file(m4, "19_count.py", """# 19. Count
# ==========================================
# CONCEPT: Frequency
# ==========================================
# How many times does X appear?

s = "banana"
print(s.count("a")) # 3
""")

create_file(m4, "20_len.py", """# 20. Length
# ==========================================
# CONCEPT: Size
# ==========================================
# Useful for loops and checks.

s = "Python"
print(len(s)) # 6
""")

create_file(m4, "99_Practice_Problems.py", """# ==========================================
# MODULE 4: PRACTICE PROBLEMS
# ==========================================
# 1. Ask user for their name and print it in ALL CAPS.
# 2. Check if the string "apple" contains the letter "e".
# 3. Reverse the user's input string.
# 4. Count how many distinct words are in "The quick brown fox jumps".
# 5. Extract "World" from "Hello World" using slicing.
# 6. Replace spaces with underscores in "File Name With Spaces".
# 7. Check if a string starts with "Py" (startswith method).
# 8. Check if a user input is purely numbers (isnumeric method).
# 9. Format a string print: "Item: [item], Price: $[price]".
# 10. Split "192.168.1.1" by dot.
# 11. Remove leading zeros from "000123".
# 12. Create a palindrome check (is "racecar" == reversed "racecar"?).
# 13. Given s="abcdef", print every 2nd character.
# 14. Capitalize only the first letter of "python" (capitalize method).
# 15. Check if "  " is just whitespace (isspace).
# 16. Find the position of the second "o" in "Google".
# 17. Print a string 5 times using multiplication ("Na" * 5).
# 18. Escape a single quote inside a single quoted string.
# 19. Join ["A", "B", "C"] with "->".
# 20. Slice out the *last* 3 characters of any input string.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. print(input().upper())
2. print("e" in "apple")
3. s=input(); print(s[::-1])
4. s="The quick..."; print(len(s.split()))
5. s="Hello World"; print(s[6:])
6. print("...".replace(" ", "_"))
7. print(s.startswith("Py"))
8. print(s.isnumeric())
9. print(f"Item: {item}, Price: ${price}")
10. print("192.168.1.1".split("."))
11. print("000123".lstrip("0"))
12. s="racecar"; print(s == s[::-1])
13. print(s[::2])
14. print("python".capitalize())
15. print("  ".isspace())
16. s="Google"; first=s.find("o"); print(s.find("o", first+1))
17. print("Na"*5)
18. print('It\\'s me')
19. print("->".join(L))
20. print(s[-3:])
'''
""")

# ==========================================
# MODULE 5: Control Flow
# ==========================================
m5 = "05_Control_Flow"

# If/Else (1-10)
create_file(m5, "01_if.py", """# 1. If Statement
# ==========================================
# CONCEPT: Decision Making
# ==========================================

x = 10
if x > 5:
    print("x is big")
# Indentation matters!
""")

create_file(m5, "02_else.py", """# 2. Else
# ==========================================
# CONCEPT: The Alternative
# ==========================================

x = 2
if x > 5:
    print("Big")
else:
    print("Small")
""")

create_file(m5, "03_elif.py", """# 3. Elif (Else If)
# ==========================================
# CONCEPT: Multiple Options
# ==========================================
# Checks conditions in order. Stops at the first True one.

x = 5
if x > 10:
    print("Huge")
elif x == 5:
    print("Exact")
else:
    print("Small")
""")

create_file(m5, "04_nested_if.py", """# 4. Nested If
# ==========================================
# CONCEPT: Layers
# ==========================================
# An if inside an if.

x = 10
y = 20
if x == 10:
    if y == 20:
        print("Both match")
""")

create_file(m5, "05_ternary.py", """# 5. Ternary Operator
# ==========================================
# CONCEPT: One-Line If
# ==========================================
# ValueIfTrue if Condition else ValueIfFalse

score = 80
status = "Pass" if score >= 50 else "Fail"
print(status)
""")

create_file(m5, "06_pass.py", """# 6. Pass
# ==========================================
# CONCEPT: Placeholder
# ==========================================
# If you need an if block but don't have code yet, use pass.
# It does nothing.

if True:
    pass # TODO: Add code later
""")

create_file(m5, "07_input_int.py", """# 7. Input with Casting
# ==========================================
# CONCEPT: User Logic
# ==========================================
# input() returns string. We need int() to compare numbers.

# val = int(input("Enter number: "))
val = 10
if val > 5:
    print("Greater than 5")
""")

create_file(m5, "08_truthiness.py", """# 8. Conditional Truthiness
# ==========================================
# CONCEPT: Implicit Checks
# ==========================================
# Empty lists/strings are False.

L = []
if L:
    print("List has items")
else:
    print("List is empty")
""")

create_file(m5, "09_multiple_conditions.py", """# 9. Chained Comparison
# ==========================================
# CONCEPT: Range Check
# ==========================================
# Python allows Math-style chaining.

x = 5
if 1 < x < 10:
    print("x is between 1 and 10")
""")

create_file(m5, "10_simple_calculator.py", """# 10. Simple Calculator Logic
# ==========================================
# CONCEPT: Putting it together
# ==========================================

op = "+"
a = 10
b = 5

if op == "+":
    print(a + b)
elif op == "-":
    print(a - b)
else:
    print("Unknown Op")
""")

# Loops (11-20)
create_file(m5, "11_for_range.py", """# 11. For Loop (Range)
# ==========================================
# CONCEPT: Repetition
# ==========================================
# Run code X times.

for i in range(5): # 0, 1, 2, 3, 4
    print(f"Iteration {i}")
""")

create_file(m5, "12_range_start_stop.py", """# 12. Range(Start, Stop)
# ==========================================
# CONCEPT: Controlled Loop
# ==========================================

for i in range(2, 5): # 2, 3, 4 (Stops BEFORE 5)
    print(i)
""")

create_file(m5, "13_range_step.py", """# 13. Range(Start, Stop, Step)
# ==========================================
# CONCEPT: Skipping
# ==========================================

for i in range(0, 11, 2): # Evens: 0, 2, 4... 10
    print(i)
""")

create_file(m5, "14_for_list.py", """# 14. For Loop (Iterable)
# ==========================================
# CONCEPT: Data Traversal
# ==========================================
# Loop directly over items, not just numbers.

fruits = ["Apple", "Banana", "Cherry"]
for fruit in fruits:
    print(f"I like {fruit}")
""")

create_file(m5, "15_for_string.py", """# 15. For Loop (String)
# ==========================================
# CONCEPT: Char by Char
# ==========================================

for char in "Python":
    print(char)
""")

create_file(m5, "16_while_loop.py", """# 16. While Loop
# ==========================================
# CONCEPT: Conditional Loop
# ==========================================
# Runs AS LONG AS the condition is True.

energy = 3
while energy > 0:
    print(f"Running... Energy: {energy}")
    energy -= 1 # Crucial! Or infinite loop.
print("Stopped.")
""")

create_file(m5, "17_break.py", """# 17. Break
# ==========================================
# CONCEPT: Eject
# ==========================================
# Exits the loop IMMEDIATELY.

for i in range(10):
    if i == 5:
        print("Found 5! Stopping.")
        break
    print(i)
""")

create_file(m5, "18_continue.py", """# 18. Continue
# ==========================================
# CONCEPT: Skip
# ==========================================
# Skips the rest of THIS iteration and goes to next.

for i in range(5):
    if i == 3:
        print("Skipping 3")
        continue 
    print(i)
""")

create_file(m5, "19_while_true.py", """# 19. While True (Game Loop)
# ==========================================
# CONCEPT: Infinite Loop
# ==========================================
# Useful for games or servers. Must have a break.

# count = 0
# while True:
#     print("Looping")
#     count += 1
#     if count >= 3:
#         break
""")

create_file(m5, "20_nested_loop.py", """# 20. Nested Loops
# ==========================================
# CONCEPT: Matrix / Grid
# ==========================================
# A look inside a loop. O(N^2) complexity.

for row in range(3):
    for col in range(3):
        print(f"({row}, {col})", end=" ")
    print() # Newline for next row
""")

# Input Handling (21-30)
create_file(m5, "21_basic_input.py", """# 21. Basic Input
# name = input("Enter Name: ")
# print(f"Hello {name}")
""")

create_file(m5, "22_int_cast.py", """# 22. Integer Input
# age = int(input("Enter Age: "))
# print(f"Next year you are {age + 1}")
""")

create_file(m5, "23_float_cast.py", """# 23. Float Input
# price = float(input("Price: "))
# print(f"Tax: {price * 0.1}")
""")

create_file(m5, "24_split_input.py", """# 24. Multiple Inputs (Line)
# a, b = input("Enter 2 numbers: ").split()
# print(f"Sum: {int(a) + int(b)}")
""")

create_file(m5, "25_map_input.py", """# 25. Map Input
# integers = list(map(int, input("Enter numbers: ").split()))
# print(f"Sum: {sum(integers)}")
""")

create_file(m5, "26_sys_stdin.py", """# 26. Fast Input (Competitive)
import sys
# input = sys.stdin.readline
# data = input().strip()
""")

create_file(m5, "27_validation.py", """# 27. Input Validation loop
# while True:
#     age = input("Enter age: ")
#     if age.isnumeric():
#         print("Accepted")
#         break
#     print("Numbers only!")
""")

create_file(m5, "28_multiple_lines.py", """# 28. Reading N lines
# n = int(input())
# for _ in range(n):
#     line = input()
#     print(f"Read: {line}")
""")

create_file(m5, "29_eof.py", """# 29. Handling End of File
# try:
#     while True:
#         line = input()
#         print(line)
# except EOFError:
#     pass
""")

create_file(m5, "30_fast_io.py", """# 30. Fast Output
import sys
# sys.stdout.write("Hello\\n") # Faster than print
""")

create_file(m5, "99_Practice_Problems.py", """# ==========================================
# MODULE 5: PRACTICE PROBLEMS
# ==========================================
# 1. Ask for age. Print "Adult" if >= 18, else "Minor".
# 2. Loop from 1 to 100. Print only numbers divisible by 7.
# 3. Ask for a password. Keep asking until user types "secret".
# 4. Print the multiplication table of 5 (5, 10... 50).
# 5. Calculate factorial of 5 using a for loop.
# 6. Sum all numbers in defined list `L`.
# 7. Find the maximum number in list `L` without using max().
# 8. Print a checkerboard pattern (3x3 grid of X and O).
# 9. Write a calculator that asks for Num1, Op, Num2.
# 10. Count vowels in a user input string.
# 11. Print the Fibonacci sequence up to 10 terms.
# 12. Check if a number is Prime.
# 13. Reverse a number using math (not strings). 123 -> 321.
# 14. Input 3 numbers and sort them using If/Else (no sort()).
# 15. FizzBuzz: Print 1-20. Mul of 3->"Fizz", 5->"Buzz", Both->"FizzBuzz".
# 16. Extract all digits from "abc123xyz" and sum them.
# 17. Guess the Number game (Logic only).
# 18. Pattern Printing: Pyramid of stars.
# 19. Validate email input (must contain @ and .).
# 20. Count how many uppercase letters are in a string.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. if int(input()) >= 18...
2. for i in range(1,101): if i%7==0: print(i)
3. while input() != "secret": pass
4. for i in range(1, 11): print(5*i)
5. f=1; for i in range(1,6): f*=i
6. total=0; for x in L: total+=x
7. m=L[0]; for x in L: if x>m: m=x
8. nested loop (row%2, col%2)
9. n1=..; op=..; n2=..; if op==...
10. count=0; for c in s: if c in "aeiou": count+=1
11. a,b=0,1; loop 10: print(a); a,b=b,a+b
12. is_prime and loop 2..n-1
13. rev=0; while n>0: rev=rev*10 + n%10; n//=10
14. nested logic or swap
15. if i%15==0.. elif i%3==0..
16. sum(int(c) for c in s if c.isdigit())
17. while guess != secret...
18. for i in range(n): print(" "*(n-i) + "*"*(2*i+1))
19. if "@" in s and "." in s...
20. count=0; for c in s: if c.isupper(): count+=1
'''
""")

print("Generated Modules 4 & 5!")
