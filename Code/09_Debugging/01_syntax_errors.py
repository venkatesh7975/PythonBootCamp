"""
01_syntax_errors.py - Understanding Syntax Errors in Python

Syntax errors are mistakes in the code that violate Python's grammar rules.
Because they are structural errors, the code will not run at all until they are fixed.

Think of it like a human language: "I go store" is understandable but grammatically 
incorrect. Python, however, refuses to "read" the code if the grammar is wrong.
"""

# -----------------------------------------------------------------------------
# 1. Missing Colons (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Forgetting the ':' at the end of control statements (if, for, while, def, class).
# WHY: In Python, a colon tells the interpreter that a new block of code starts next.
# WHEN: Often happens when you're typing quickly or switching from a language like C++ or Java.

# Incorrect:
# if True
#     print("Hello")

# Correct:
if True:
    print("Correct: Added colon after if statement.")

# -----------------------------------------------------------------------------
# 2. Unmatched Parentheses/Brackets (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Opening a bracket ( or [ or { but forgetting to close it.
# WHY: Python keeps looking for the end of the expression and gets confused.
# WHEN: Common in long print statements or complex mathematical calculations.
# TIP: Many IDEs will highlight the matching bracket for you.

# Incorrect:
# print("Oops"

# Correct:
print("Correct: Closed the parenthesis.")

# -----------------------------------------------------------------------------
# 3. Invalid Indentation (IndentationError / TabError)
# -----------------------------------------------------------------------------
# WHAT: Inconsistent spacing at the start of lines.
# WHY: Python uses indentation (not curly braces {}) to group blocks of code.
# WHEN: Very common when copy-pasting code or mixing tabs and spaces.
# RULE: Use 4 spaces per indentation level.

# Incorrect:
# def my_function():
# print("No indentation")

# Correct:
def my_function():
    print("Correct: Properly indented inside function.")

my_function()

# -----------------------------------------------------------------------------
# 4. Keyword Typos / Invalid Syntax (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Misspelling reserved Python keywords (for, while, import, etc.).

# Incorrect:
# forr i in range(5):
#     print(i)

# Correct:
for i in range(1):
    print(f"Correct: Fixed 'for' keyword typo.")

# -----------------------------------------------------------------------------
# 5. Assignment vs Equality (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Using '=' (assignment) inside an 'if' statement instead of '==' (equality).
# WHY: '=' is for giving a variable a value; '==' is for comparing two values.
# SCENARIO: Trying to check if a user's role is 'admin'.

# Incorrect:
# if user_role = "admin":
#     print("Access granted")

# Correct:
user_role = "guest"
if user_role == "admin":
    print("Welcome Admin")
else:
    print("Correct: Used '==' for comparison.")

# -----------------------------------------------------------------------------
# 6. Invalid Identifiers (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Naming a variable starting with a number or using invalid characters.
# WHY: Python variable names must start with a letter or underscore.

# Incorrect:
# 1st_place = "Gold"

# Correct:
first_place = "Gold"
print(f"Correct: Variable name starts with a letter: {first_place}")

# -----------------------------------------------------------------------------
# 7. Break/Continue/Return Outside Allowed Scope (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Using 'break' or 'continue' outside a loop, or 'return' outside a function.
# WHY: These keywords have specific jobs that only make sense in certain contexts.

# Incorrect:
# break 
# return 10

# Correct:
def get_number():
    return 10  # Correct: 'return' is inside a function.

for x in range(1):
    break      # Correct: 'break' is inside a loop.

print("Correct: Break and Return used in proper contexts.")

# -----------------------------------------------------------------------------
# 8. Mismatched Quotes (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Starting a string with ' and ending with " or vice versa.
# SCENARIO: Forgetting which quote you started with in a long string.

# Incorrect:
# my_string = "Hello'

# Correct:
my_string = "Hello"
print(f"Correct: Quotes match: {my_string}")

# -----------------------------------------------------------------------------
# 9. Literal Structure Errors (SyntaxError)
# -----------------------------------------------------------------------------
# WHAT: Commas in the wrong place or missing values in a list/dict literal.
# WHY: Python expects a specific pattern for data structures.

# Incorrect:
# my_list = [1, 2,, 3]

# Correct:
my_list = [1, 2, 3]
print(f"Correct: List structure is valid: {my_list}")

print("\n--- Syntax Errors Demo Complete ---")
