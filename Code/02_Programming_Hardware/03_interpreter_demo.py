# 3. Interpreter Demo
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
