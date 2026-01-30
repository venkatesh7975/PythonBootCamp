# 27. Raise Exception
# ==========================================
# CONCEPT: Trigger Error
# ==========================================
# Manually cause an error.

def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")

# check_age(-5) # Crashes with ValueError
