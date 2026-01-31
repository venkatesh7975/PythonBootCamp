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
# WHY: Python doesn't recognize the typo as a command it knows.
# WHEN: Typos are inevitable; look for "invalid syntax" pointing to the typo.

# Incorrect:
# forr i in range(5):
#     print(i)

# Correct:
for i in range(2):
    print(f"Correct: Fixed 'for' keyword typo. Loop iteration: {i}")

print("\n--- Syntax Errors Demo Complete ---")
