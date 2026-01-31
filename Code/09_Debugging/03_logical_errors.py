"""
03_logical_errors.py - Understanding Logical Errors (Bugs)

Logical errors are the hardest to find because the code runs without crashing,
but it produces the wrong output. These are "bugs" in the logic.

Think of it like a recipe: you followed all the steps (no syntax errors) and 
the oven didn't explode (no runtime errors), but you used salt instead of 
sugar—so the cake tastes bad (logical error).
"""

# -----------------------------------------------------------------------------
# 1. Off-by-one Error
# -----------------------------------------------------------------------------
# WHAT: Miscalculating the start or end of a loop or index.
# WHY: Python's range(n) stops AT n (not including n) and starts at 0.
# SCENARIO: A teacher trying to print "Student 1" to "Student 5" but getting 0 to 4.

print("Goal: Print numbers 1 to 5")
print("Incorrect output (0 to 4):")
for i in range(5):
    print(i, end=" ")
print("\nCorrect output (1 to 5):")
for i in range(1, 6):
    print(i, end=" ")
print("\n")

# -----------------------------------------------------------------------------
# 2. Incorrect Operator Precedence
# -----------------------------------------------------------------------------
# WHAT: Forgetting that multiplication/division happen before addition/subtraction (PEMDAS).
# WHY: Math rules apply in code just like in a classroom.
# SCENARIO: A banking app calculating the average balance of two accounts.

print("Goal: Calculate average of 10 and 20")
# Incorrect: 10 + 20 / 2 = 10 + 10 = 20
wrong_avg = 10 + 20 / 2
# Correct: (10 + 20) / 2 = 30 / 2 = 15
correct_avg = (10 + 20) / 2
print(f"Goal: 15 | Incorrect: {wrong_avg} | Correct: {correct_avg}\n")

# -----------------------------------------------------------------------------
# 3. Variable Scoping Issues
# -----------------------------------------------------------------------------
# WHAT: Accidentally creating a local variable when you meant to update a global one.
# WHY: Python assumes a variable is local if you assign to it inside a function.
# SCENARIO: A score tracker that never updates the main high score record.

total = 100
def add_to_total(n):
    # LOGICAL ERROR: This creates a NEW local 'total' variable.
    # The global 'total' remains unchanged.
    total = 0 
    total += n
    return total

print(f"Global total: {total}")
print(f"Result of function call: {add_to_total(5)}")
print(f"Global total after call: {total} (Still 100!)\n")

# -----------------------------------------------------------------------------
# 4. Logical Check Flaws (The "Truthy" Trap)
# -----------------------------------------------------------------------------
# WHAT: Writing an 'if' statement that always evaluates to True because of how 'or' works.
# WHY: 'val == "A" or "B"' checks (val == "A") OR ("B"). Since "B" is a non-empty string, it's always True.
# SCENARIO: A security system that lets everyone in because the check is flawed.

val = "C"
print(f"Testing if '{val}' is 'A' or 'B'")
if val == "A" or "B": # Logical bug: this is (val == "A") or (bool("B")).
    print("Buggy Check: This branch ALWAYS runs because 'B' is truthy!")

if val in ["A", "B"]:
    print("Correct Check: This branch won't run for 'C'.")
else:
    print("Correct Check: 'C' is not 'A' or 'B'.")

print("\n--- Logical Errors Demo Complete ---")
