"""
01_syntax_errors.py - Understanding Syntax Errors in Python

Syntax errors are mistakes in the code that violate Python's grammar rules.
Because they are structural errors, the code will not run at all until they are fixed.
"""

# -----------------------------------------------------------------------------
# 1. Missing Colons
# -----------------------------------------------------------------------------
# Incorrect:
# if True
#     print("Hello")

# Correct:
if True:
    print("Correct: Added colon after if statement.")

# -----------------------------------------------------------------------------
# 2. Unmatched Parentheses/Brackets
# -----------------------------------------------------------------------------
# Incorrect:
# print("Oops"

# Correct:
print("Correct: Closed the parenthesis.")

# -----------------------------------------------------------------------------
# 3. Invalid Indentation
# -----------------------------------------------------------------------------
# Incorrect:
# def my_function():
# print("No indentation")

# Correct:
def my_function():
    print("Correct: Properly indented inside function.")

my_function()

# -----------------------------------------------------------------------------
# 4. Keyword Typos / Invalid Syntax
# -----------------------------------------------------------------------------
# Incorrect:
# forr i in range(5):
#     print(i)

# Correct:
for i in range(2):
    print(f"Correct: Fixed 'for' keyword typo. Loop iteration: {i}")

print("\n--- Syntax Errors Demo Complete ---")
