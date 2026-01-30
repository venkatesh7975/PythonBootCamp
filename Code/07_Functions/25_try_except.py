# 25. Try Except
# ==========================================
# CONCEPT: Error Handling
# ==========================================
# Catch specific errors.

try:
    print(10/0)
except ZeroDivisionError:
    print("Can't divide by zero!")
except Exception as e:
    print(f"Other error: {e}")
