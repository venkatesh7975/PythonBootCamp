# 6. Default Arguments
# ==========================================
# CONCEPT: Fallback
# ==========================================
# Optional parameters.

def greet(name="User"):
    print(f"Hello, {name}")

greet("Alice") # Hello, Alice
greet()        # Hello, User
