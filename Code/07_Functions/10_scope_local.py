# 10. Local Scope
# ==========================================
# CONCEPT: Privacy
# ==========================================
# Variables inside a function are invisible outside.

def my_func():
    secret = "I am hidden"

# print(secret) # NameError: name 'secret' is not defined
