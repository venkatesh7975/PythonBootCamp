# 8. Conditional Truthiness
# ==========================================
# CONCEPT: Implicit Checks
# ==========================================
# Empty lists/strings are False.

L = []
if L:
    print("List has items")
else:
    print("List is empty")
