# 11. Global Scope
# ==========================================
# CONCEPT: Visibility
# ==========================================
# Variables defined outside are visible inside.

x = "Global"

def show_x():
    print(x) # Works!

show_x()
