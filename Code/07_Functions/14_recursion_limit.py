# 14. Recursion Limit
# ==========================================
# CONCEPT: Safety Net
# ==========================================
# Python stops infinite recursion to save memory. 
# Usually 1000 calls deep.

import sys
print(sys.getrecursionlimit())

def infinite():
    infinite()

# infinite() # RecursionError
