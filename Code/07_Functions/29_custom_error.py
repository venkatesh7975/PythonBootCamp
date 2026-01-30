# 29. Custom Exception
# ==========================================
# CONCEPT: Specificity
# ==========================================
# Create your own error type.

class TooColdError(Exception):
    pass

temp = -10
if temp < 0:
    # raise TooColdError("Brrr!")
    pass
