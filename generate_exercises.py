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
# MODULE 1: Introduction to Software
# ==========================================
m1 = "01_Introduction_to_Software"

create_file(m1, "01_hello_world.py", """# 1. Hello World
# ==========================================
# CONCEPT: The First Program
# ==========================================
# Why? This is the traditional first step in learning any language.
# It tests if Python is installed and working correctly.
#
# How? The `print()` function takes text (a string) and displays it on the screen.

print("Hello, World!")

# Common Errors:
# 1. print "Hello" (Missing parentheses - Python 2 style error)
# 2. Print("Hello") (Capital P - Python is case sensitive)
""")

create_file(m1, "02_comments.py", """# 2. Comments
# ==========================================
# CONCEPT: Notes for Humans
# ==========================================
# Why? Code is read more often than it is written. Comments help explain 'Why' you did something.
# The computer ignores these lines completely.

# Single line comment: starts with a hash (#)
print("This runs.") # This is an inline comment

# print("This does not run.")

'''
Multi-line comments 
use three single quotes 
or three double quotes.
'''

# Common Errors:
# 1. Forgetting the # makes Python try to run your text as code.
""")

create_file(m1, "03_print_basics.py", """# 3. Print Basics
# ==========================================
# CONCEPT: Outputting Data
# ==========================================
# Why? We need to see results! 
# How? print() can take multiple arguments separated by commas.

print("apples")
print("bananas")
print("cherries")

# Printing multiple items
print("I", "love", "Python") # Adds a space automatically

# Common Errors:
# 1. typos in the function name (pirnt instead of print)
""")

create_file(m1, "04_print_separator.py", """# 4. Print Separator
# ==========================================
# CONCEPT: Customizing Output (sep)
# ==========================================
# Why? Sometimes you don't want a space between items.
# How? Use the `sep="..."` argument inside print().

print("A", "B", "C", sep="-") # Output: A-B-C
print("User", "Domain", "com", sep="@") # Output: User@Domain@com

# Try it yourself:
# Print a date like 2023/10/25 using sep="/"
""")

create_file(m1, "05_print_end.py", """# 5. Print End
# ==========================================
# CONCEPT: Customizing Output (end)
# ==========================================
# Why? By default, print() creates a new line. Sometimes we want to stay on the same line.
# How? Use the `end="..."` argument.

print("Hello", end=" ")
print("World")
# Output: Hello World (on one line)

print("Loading", end="...")
print("Done!")

# Common Errors:
# 1. Forgetting to add a space in end=" " will mash words together (HelloWorld).
""")

create_file(m1, "06_escape_characters.py", """# 6. Escape Characters
# ==========================================
# CONCEPT: Special Formatting
# ==========================================
# Why? How do you print a "New Line" or a "Tab" character?
# How? Use the backslash (\\) followed by a code.

# \\n = Newline (Enter key)
print("Line 1\\nLine 2")

# \\t = Tab (Indent)
print("Column1\\tColumn2")

# \\" = Quote inside a quote
print(\"She said \\"Hello\\" to me.\")
""")

create_file(m1, "07_software_algorithm.py", """# 7. Algorithm Simulation
# ==========================================
# CONCEPT: Algorithms
# ==========================================
# Why? An algorithm is just a step-by-step recipe to solve a problem.
# Before coding, write the algorithm!

print("Algorithm: Making Tea")
print("---------------------")
print("Step 1: Boil Water")
print("Step 2: Add Tea Bag to Cup")
print("Step 3: Pour Boiling Water")
print("Step 4: Steep for 3 minutes")
print("Step 5: Remove Bag and Drink")
""")

create_file(m1, "08_debugging_print.py", """# 8. Debugging with Print
# ==========================================
# CONCEPT: Finding Bugs
# ==========================================
# Why? When code doesn't work, we need to see what's happening inside.
# How? Add print statements to show variable values at different steps.

x = 10
print(f"DEBUG: x starts at {x}")

x = x + 5
print(f"DEBUG: Added 5, x is now {x}")

x = x * 2
print(f"DEBUG: Doubled, x is now {x}")
""")

create_file(m1, "09_user_interaction.py", """# 9. Simple Interaction
# ==========================================
# CONCEPT: User Experience (UX)
# ==========================================
# Why? Programs interact with users. Text layout matters.

print("=======================")
print("   WELCOME TO PYTHON   ")
print("=======================")
print() # Empty line
print("Loading modules...")
print("Done!")
""")

create_file(m1, "10_ascii_art.py", """# 10. ASCII Art
# ==========================================
# CONCEPT: Art with Text
# ==========================================
# Just for fun! Using characters to draw pictures.

print("  O  ")
print(" /|\\ ")
print(" / \\ ")
print("Running Man!")
""")

create_file(m1, "99_Interactive_Quiz.py", """# Interactive Quiz - Module 1
import time

def quiz():
    print("Welcome to the Module 1 Quiz! (Press Enter to reveal answers)")
    print("-" * 50)
    
    questions = [
        ("Write a program to print 'Welcome to Python' 3 times.", 
         "print('Welcome to Python\\\\n' * 3)"),
         
        ("Print 'Python', 'is', 'fun' separated by underscores (_).", 
         "print('Python', 'is', 'fun', sep='_')"),
         
        ("Print 'Code' and 'Time' on the same line, separated by a star (*).", 
         "print('Code', 'Time', sep='*')"),
         
        ("Write an algorithm (print steps) to Tie Shoelaces.", 
         "print('1. Grab laces...'); print('2. Cross them...')"),
         
        ("Fix this code: Print('Hello World')", 
         "print('Hello World') (Lowercase p)"),
         
        ("Print a square using hashes (#).", 
         "print('###\\\\n# #\\\\n###')"),
         
        ("Use escape characters to print: 'Title' then a newline, then 'Subtitle'.", 
         "print('Title\\\\nSubtitle')"),
         
        ("Print the calculation: 5 + 10 = 15 (Just print the text).", 
         "print('5 + 10 = 15')"),
         
        ("Print 'Loading' ending with 3 dots, then 'Complete' on the same line.", 
         "print('Loading', end='...'); print('Complete')"),
         
        ("Create a simple 'Menu' using print statements (Start, Options, Exit).", 
         "print('1. Start\\\\n2. Options\\\\n3. Exit')"),
         
        ("Debug this: variable score = 100. Print 'Score is 100'.", 
         "score=100; print(f'Score is {score}')"),
         
        ("Print a Triangle using stars.", 
         "print('  *  \\\\n *** \\\\n*****')"),
         
        ("Print 'Quotes' inside a string: She said 'Hi'.", 
         "print('She said \"Hi\"')"),
         
        ("Print your name, age, and city on separate lines using one print() command with \\\\n.", 
         "print('Name\\\\nAge\\\\nCity')"),
         
        ("Print the following path: C:\\\\Users\\\\Name (Hint: Escaping backslashes).", 
         "print('C:\\\\\\\\Users\\\\\\\\Name')"),
         
        ("Using 'sep', print time: 12 : 30 : 00.", 
         "print(12, 30, 00, sep=' : ')"),
         
        ("Using 'end', print a progress bar: [#####     ].", 
         "print('[', end=''); print('#'*5, end=''); print(' '*5, end=''); print(']')"),
         
        ("Write a comment explaining what `print()` does.", 
         "# functions displays text to console"),
         
        ("Print a Diamond shape.", 
         "print('  *  \\\\n *** \\\\n  *  ')"),
         
        ("Make a 'Business Card' output with borders.", 
         "print('________'); print('| Name |'); print('|______|')")
    ]

    score = 0
    for i, (q, a) in enumerate(questions, 1):
        print(f"\\\\nQ{i}: {q}")
        user_input = input("   Your Answer (Mental or Type it): ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
""")

# ==========================================
# MODULE 2: Programming & Hardware
# ==========================================
m2 = "02_Programming_Hardware"

create_file(m2, "01_cpu_simulation.py", """# 1. CPU Simulation
# ==========================================
# CONCEPT: Fetch-Decode-Execute Cycle
# ==========================================
# How a CPU works:
# 1. Fetch: Get instruction from RAM.
# 2. Decode: Understand what to do.
# 3. Execute: Do it.

import time

print("CPU: Fetching Instruction...")
time.sleep(1) # Fake delay
print("CPU: Decoding (Understanding 1011001)...")
time.sleep(1)
print("CPU: Executing (Adding Numbers)...")
print("Done!")
""")

create_file(m2, "02_memory_vars.py", """# 2. Memory Visualization
# ==========================================
# CONCEPT: RAM & Addresses
# ==========================================
# Variables are just fancy names for memory addresses (like house addresses).
# 'id()' shows the memory address.

a = 10
b = 20
c = 10 # Points to SAME address as 'a' for efficiency!

print(f"Address of a (10): {id(a)}")
print(f"Address of b (20): {id(b)}")
print(f"Address of c (10): {id(c)}")
""")

create_file(m2, "03_interpreter_demo.py", """# 3. Interpreter Demo
# ==========================================
# CONCEPT: Interpreted Language
# ==========================================
# Python reads line-by-line. If line 3 crashes, line 1 and 2 still ran!
# Unlike C++ (Compiled), which wouldn't run at all if there was an error.

print("Line 1 executed")
print("Line 2 executed")

# Uncomment below to crash:
# print(1 / 0) 

print("Line 4 executed (If Line 3 didn't crash)")
""")

create_file(m2, "04_binary_concept.py", """# 4. Binary Concept
# ==========================================
# CONCEPT: 0s and 1s
# ==========================================
# Computers only know ON (1) and OFF (0).
# bin() converts decimal numbers to binary strings.

n = 10
print(f"Decimal (Human): {n}")
print(f"Binary (Computer): {bin(n)}") # 0b1010
""")

create_file(m2, "05_input_output.py", """# 5. I/O Devices
# ==========================================
# CONCEPT: Input and Output
# ==========================================
# Input: Keyboard, Mouse, Mic (Function: input())
# Output: Monitor, Speaker, Printer (Function: print())

print("This is Output (Monitor).")
name = input("Input Needed (Keyboard) - Enter Name: ")
print(f"You entered: {name}")
""")

create_file(m2, "06_speed_test.py", """# 6. Speed Test
# ==========================================
# CONCEPT: Execution Speed
# ==========================================
# Python is 'slow' compared to C because it's interpreted. 
# But let's see how fast it counts to 1 million.

import time
start = time.time()

# Count to 1,000,000
for i in range(1000000):
    pass

end = time.time()
print(f"Time taken: {end - start:.5f} seconds")
""")

create_file(m2, "07_os_check.py", """# 7. OS Check
# ==========================================
# CONCEPT: Operating System
# ==========================================
# Python runs on Windows, Mac, Linux. 
# 'os' module lets us talk to the system.

import os
print(f"Running on OS Type: {os.name}")
# nt = Windows
# posix = Mac/Linux
""")

create_file(m2, "08_garbage_collection.py", """# 8. Garbage Collection
# ==========================================
# CONCEPT: Memory Management
# ==========================================
# Python has a 'Garbage Collector' that deletes variables you don't use anymore 
# to free up RAM.

x = [1, 2, 3] # Create list in memory
print("List created.")

del x # Manually delete 'reference' to list
# The Garbage Collector will now remove the list from RAM.

# print(x) # This works cause NameError (x is gone)
print("x deleted from memory.")
""")

create_file(m2, "09_type_size.py", """# 9. Size of Objects
# ==========================================
# CONCEPT: Bits and Bytes
# ==========================================
# Everything takes up space in RAM.
# sys.getsizeof() tells us how big an object is in bytes.

import sys
x = 10
print(f"Size of integer 10: {sys.getsizeof(x)} bytes")
# It's not just 4 bytes! Python integers are objects with overhead.
""")

create_file(m2, "10_hardware_specs.py", """# 10. Mock Hardware Specs
# ==========================================
# CONCEPT: Hardware Components
# ==========================================
# Just a simulation printing hardware info.

print("Checking System Hardware...")
print("-" * 20)
print("CPU: 8 Cores (The Brain)")
print("RAM: 16 GB (The Workbench)")
print("HDD: 1 TB (The Library)")
print("GPU: RTX 4090 (The Painter)")
""")

create_file(m2, "99_Interactive_Quiz.py", """# Interactive Quiz - Module 2
import time

def quiz():
    print("Welcome to the Module 2 Quiz! (Press Enter to reveal answers)")
    print("-" * 50)
    
    questions = [
        ("Write a script that inputs a number and prints its binary version.", 
         "n=int(input()); print(bin(n))"),
         
        ("Simulate a 'Loading RAM' bar using sleep() and print.", 
         "import time; print('Loading...'); time.sleep(2); print('Done')"),
         
        ("Print the memory address of the string 'Hello'.", 
         "print(id('Hello'))"),
         
        ("Create two variables with the same value (e.g., 500) and check if their addresses are same (id(a) == id(b)).", 
         "a=500; b=500; print(id(a)==id(b))"),
         
        ("Write a script that crashes nicely (using try-except) demonstrating Interpreter checking.", 
         "try: print(1/0) except: print('Crash averted')"),
         
        ("Measure how long it takes to print 'Hello' 1000 times.", 
         "start=time.time(); loop...; end=time.time()"),
         
        ("Input your OS name manually and print 'You are using [OS]'.", 
         "os_name = input(); print(f'You are using {os_name}')"),
         
        ("Calculate the size of a large string 'A' * 1000 in bytes.", 
         "import sys; print(sys.getsizeof('A'*1000))"),
         
        ("Write a 'BIOS Check' script that prints 'Checking CPU... OK', 'Checking RAM... OK'.", 
         "print('Checking CPU... OK') etc."),
         
        ("Simulate an infinite loop (use Ctrl+C to stop, or add a break).", 
         "while True: break # Safety break"),
         
        ("Convert binary '0b101' back to integer (print(0b101)).", 
         "print(0b101) # Output: 5"),
         
        ("Write a script that deletes a variable `secret` and tries to print it (expect Error).", 
         "secret=1; del secret; print(secret)"),
         
        ("Input 2 numbers and print their sum. Use a comment to label Input and Output devices.", 
         "# Input: Keyboard; res = int(input()) + int(input()); # Output: Monitor; print(res)"),
         
        ("Print the result of 2 to the power of 100.", 
         "print(2**100)"),
         
        ("Create a variable `x = None`. Print its memory address.", 
         "x=None; print(id(x))"),
         
        ("Show that `True` is actually `1` in memory (print(True + True)).", 
         "print(True+True) # 2"),
         
        ("Use `time.sleep` to make a countdown timer (3... 2... 1... Go!).", 
         "time.sleep(1)..."),
         
        ("Write a script that imports `sys` and prints `sys.version`.", 
         "import sys; print(sys.version)"),
         
        ("Define a variable, print it, delete it, redefine it, print it again.", 
         "x=1; print(x); del x; x=2; print(x)"),
         
        ("Explain in a comment: What is the difference between HDD and RAM?", 
         "# RAM is fast/volatile (Workbench). HDD is slow/permanent (Library).")
    ]

    for i, (q, a) in enumerate(questions, 1):
        print(f"\\\\nQ{i}: {q}")
        user_input = input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
""")

# ==========================================
# MODULE 3: Python Basics
# ==========================================
m3 = "03_Python_Basics"

create_file(m3, "01_variables.py", """# 1. Variables
# ==========================================
# CONCEPT: Storing Data
# ==========================================
# Variables are containers. You don't "declare" type in Python.
# Just assign a value.

x = 5             # Integer
name = "Python"   # String
price = 19.99     # Float

print(x)
print(name)
print(price)

# Why? To reuse data later without typing "Python" every time.
""")

create_file(m3, "02_reassign.py", """# 2. Reassignment
# ==========================================
# CONCEPT: Variables Handling Change
# ==========================================
# Variables can change value (and type!) at any time.

x = 5
print(f"x is {x}")

x = 100
print(f"x is now {x}")

x = "Hello" # Changing type from int to str (Dynamic Typing)
print(f"x is now {x}")
""")

create_file(m3, "03_naming_rules.py", """# 3. Naming Rules
# ==========================================
# CONCEPT: Logic & Convention
# ==========================================
# Rules:
# 1. Start with letter or underscore (_).
# 2. No numbers at start (1var is BAD).
# 3. Case sensitive (Age != age).
# 4. No spaces (use_snake_case).

my_var = 10
_private = 20
VAR_CONST = 30 # Convention for constants

# 2cool = 10 # SyntaxError!

print(my_var)
""")

create_file(m3, "04_multiple_assign.py", """# 4. Multiple Assignment
# ==========================================
# CONCEPT: Efficiency
# ==========================================
# Assign multiple variables in one line.

name, age, city = "Alice", 25, "New York"

print(name)
print(age)
print(city)

# Common Error: Not enough values
# a, b = 1 # ValueError
""")

create_file(m3, "05_swap_vars.py", """# 5. Swapping Variables
# ==========================================
# CONCEPT: Pythonic Magic
# ==========================================
# In other languages, you need a Temp variable to swap 2 items.
# In Python, do it in one line!

a = 5
b = 10

print(f"Before: a={a}, b={b}")

# The Magic Swap
a, b = b, a

print(f"After: a={a}, b={b}")
""")

create_file(m3, "06_integers.py", """# 6. Integers (int)
# ==========================================
# CONCEPT: Whole Numbers
# ==========================================
# No decimal points. Positive or negative.

x = 10
y = -50
z = 12345678901234567890 (Python handles HUGE numbers!)

print(type(x))
print(x + y)
""")

create_file(m3, "07_floats.py", """# 7. Floats (float)
# ==========================================
# CONCEPT: Decimals
# ==========================================
# Numbers with points.

pi = 3.14159
g = -9.8

# Scientific Notation
# 2.5e3 = 2.5 * 10^3 = 2500.0
x = 2.5e3 

print(x)
print(type(pi))
""")

create_file(m3, "08_strings.py", """# 8. Strings (str)
# ==========================================
# CONCEPT: Text
# ==========================================
# Text enclosed in quotes.

s1 = 'Single Quotes'
s2 = "Double Quotes"

print(type(s1))
print(s1)
""")

create_file(m3, "09_booleans.py", """# 9. Booleans (bool)
# ==========================================
# CONCEPT: True/False
# ==========================================
# Used for logic and conditions.
# Capital T and F!

is_active = True
is_game_over = False

print(type(is_active))
print(is_active)
""")

create_file(m3, "10_none.py", """# 10. NoneType
# ==========================================
# CONCEPT: Absence of Value
# ==========================================
# Null, Nil, Nothing. 
# Used as a placeholder.

empty_box = None
print(type(empty_box))
""")

create_file(m3, "11_addition.py", """# 11. Addition
# ==========================================
# CONCEPT: Math +
# ==========================================

print(10 + 5)
print(1.5 + 2.5)
print(True + 1) # True is 1! Output: 2
""")

create_file(m3, "12_subtraction.py", """# 12. Subtraction
# ==========================================
# CONCEPT: Math -
# ==========================================

print(10 - 5)
print(5 - 10) # Negative result
""")

create_file(m3, "13_multiplication.py", """# 13. Multiplication
# ==========================================
# CONCEPT: Math *
# ==========================================

print(10 * 5)
print(5 * 2.5) # Float result
""")

create_file(m3, "14_division.py", """# 14. Division (/)
# ==========================================
# CONCEPT: True Division
# ==========================================
# ALWAYS returns a float, even if clean division.

print(10 / 2) # 5.0 (Float)
print(5 / 2)  # 2.5
""")

create_file(m3, "15_floor_div.py", """# 15. Floor Division (//)
# ==========================================
# CONCEPT: Integer Division
# ==========================================
# Chops off the decimal part. Rounds DOWN.

print(10 // 3) # 3.333 -> 3
print(-10 // 3) # -3.33 -> -4 (Rounds down!)
""")

create_file(m3, "16_modulus.py", """# 16. Modulus (%)
# ==========================================
# CONCEPT: Remainder
# ==========================================
# Extremely useful for finding even/odd or looping.

print(10 % 3) # 10 / 3 = 3 rem 1
print(4 % 2)  # 0 (Even number)
print(5 % 2)  # 1 (Odd number)
""")

create_file(m3, "17_exponent.py", """# 17. Exponent (**)
# ==========================================
# CONCEPT: Power
# ==========================================
# Do NOT use ^ (that's XOR). Use **.

print(2 ** 3) # 2 * 2 * 2 = 8
print(4 ** 0.5) # Square root of 4 = 2.0
""")

create_file(m3, "18_pemdas.py", """# 18. Order of Operations
# ==========================================
# CONCEPT: PEMDAS / BODMAS
# ==========================================
# Parentheses -> Exponents -> Mul/Div -> Add/Sub

res = 2 + 3 * 4 # 3*4=12, +2 = 14
print(res)

res2 = (2 + 3) * 4 # 5*4=20
print(res2)
""")

create_file(m3, "19_equals.py", """# 19. Equality (==)
# ==========================================
# CONCEPT: Checking Equality
# ==========================================
# = is assignment. == is question.

x = 5
print(x == 5) # True
print(x == 10) # False
""")

create_file(m3, "20_not_equals.py", """# 20. Not Equals (!=)
# ==========================================
# CONCEPT: Inequality
# ==========================================
# ! usually means NOT in C-style languages.

x = 5
print(x != 3) # True, 5 is NOT 3.
""")

create_file(m3, "21_greater.py", """# 21. Greater Than (>)
# ==========================================
# CONCEPT: Comparison
# ==========================================

print(5 > 3) # True
print(1 > 10) # False
""")

create_file(m3, "22_less.py", """# 22. Less Than (<)
# ==========================================
# CONCEPT: Comparison
# ==========================================

print(2 < 10) # True
""")

create_file(m3, "23_greater_equal.py", """# 23. Greater/Equal (>=)
# ==========================================
# CONCEPT: Comparison
# ==========================================

print(5 >= 5) # True
print(4 >= 5) # False
""")

create_file(m3, "24_less_equal.py", """# 24. Less/Equal (<=)
# ==========================================
# CONCEPT: Comparison
# ==========================================

print(4 <= 5) # True
""")

create_file(m3, "25_and.py", """# 25. Logic AND
# ==========================================
# CONCEPT: Both must be True
# ==========================================

print(True and True)   # True
print(True and False)  # False
print(False and False) # False
""")

create_file(m3, "26_or.py", """# 26. Logic OR
# ==========================================
# CONCEPT: At least one True
# ==========================================

print(True or False)   # True
print(False or False)  # False
""")

create_file(m3, "27_not.py", """# 27. Logic NOT
# ==========================================
# CONCEPT: Flip it
# ==========================================

print(not True)  # False
print(not False) # True
""")

create_file(m3, "28_logic_combo.py", """# 28. Logic Combinations
# ==========================================
# CONCEPT: Complex Logic
# ==========================================

# (True) AND (True)
print((5 > 3) and (2 < 4)) 

# order: NOT -> AND -> OR
""")

create_file(m3, "29_truthy_falsy.py", """# 29. Truthy & Falsy
# ==========================================
# CONCEPT: Implicit Booleans
# ==========================================
# Most things are True.
# Falsy things: 0, 0.0, "", [], None, False.

print(bool(0))        # False
print(bool(1))        # True
print(bool("Hello"))  # True
print(bool(""))       # False (Empty string)
""")

create_file(m3, "30_short_circuit.py", """# 30. Short Circuiting
# ==========================================
# CONCEPT: Optimization
# ==========================================
# Python stops checking if it already knows the answer.

# OR: If first is True, answer is True. Skips second part.
print(True or (1/0)) # No crash!

# AND: If first is False, answer is False. Skips second part.
print(False and (1/0)) # No crash!
""")

create_file(m3, "99_Interactive_Quiz.py", """# Interactive Quiz - Module 3
import time

def quiz():
    print("Welcome to the Module 3 Quiz! (Press Enter to reveal answers)")
    print("-" * 50)
    
    questions = [
        ("Create a variable `age` and assign 21. Print it.", 
         "age=21; print(age)"),
         
        ("Swap `x=1` and `y=2` without a temp variable.", 
         "x,y=y,x"),
         
        ("Calculate the area of a rectangle (l=10, w=5).", 
         "print(10*5)"),
         
        ("Check if 7 is even/o