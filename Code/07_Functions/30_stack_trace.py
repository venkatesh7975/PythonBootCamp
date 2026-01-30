# 30. Stack Trace (Traceback)
# ==========================================
# CONCEPT: Debugging Trail
# ==========================================
# Python prints the path to the error.

import traceback

try:
    print(1/0)
except:
    traceback.print_exc() # Prints the error details
