# 20. Inner Functions
# ==========================================
# CONCEPT: Encapsulation
# ==========================================
# Helper functions hidden inside.

def outer():
    print("Outer")
    
    def inner():
        print("Inner")
    
    inner()

outer()
# inner() # Error, not visible here.
