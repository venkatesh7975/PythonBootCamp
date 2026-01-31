"""
03_logical_errors.py - Understanding Logical Errors (Bugs)

Logical errors are the hardest to find because the code runs without crashing,
but it produces the wrong output. These are "bugs" in the logic.
"""

# -----------------------------------------------------------------------------
# 1. Off-by-one Error
# -----------------------------------------------------------------------------
print("Goal: Print numbers 1 to 5")
# Incorrect: range(5) gives 0, 1, 2, 3, 4
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
print("Goal: Calculate average of 10 and 20")
# Incorrect: 10 + 20 / 2 = 10 + 10 = 20
wrong_avg = 10 + 20 / 2
# Correct: (10 + 20) / 2 = 30 / 2 = 15
correct_avg = (10 + 20) / 2
print(f"Goal: 15 | Incorrect: {wrong_avg} | Correct: {correct_avg}\n")

# -----------------------------------------------------------------------------
# 3. Variable Scoping Issues
# -----------------------------------------------------------------------------
total = 100
def add_to_total(n):
    # This creates a LOCAL variable 'total' instead of using the global one
    # unless 'global total' is specified.
    total = 0 
    total += n
    return total

print(f"Global total: {total}")
print(f"Result of function call (expected 105 if global, but got local): {add_to_total(5)}")
print(f"Global total after call: {total} (Still 100!)\n")

# -----------------------------------------------------------------------------
# 4. Logical Check Flaws
# -----------------------------------------------------------------------------
status = False
# Incorrect: 'if status == True or False' is always True because 'False' is truthy as a non-empty check?
# Wait, 'if False' is False, but 'if status == True or False' is (status == True) or (False)
# If status is False, it's (False == True) or (False) => False or False => False.
# However, many beginners write 'if x == "A" or "B":' which is always True.

val = "C"
print(f"Testing if '{val}' is 'A' or 'B'")
if val == "A" or "B": # Logical bug: this is (val == "A") or ("B"). "B" is truthy.
    print("Buggy Check: This branch always runs!")

if val in ["A", "B"]:
    print("Correct Check: This branch won't run for 'C'.")
else:
    print("Correct Check: 'C' is not 'A' or 'B'.")

print("\n--- Logical Errors Demo Complete ---")
