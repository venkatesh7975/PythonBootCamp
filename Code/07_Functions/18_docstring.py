# 18. Docstrings
# ==========================================
# CONCEPT: Documentation
# ==========================================
# Triple quotes describing what the function does.
# Stored in .__doc__

def square(n):
    '''Takes a number n and returns n squared.'''
    return n**2

print(square.__doc__)
