# 19. Type Hints
# ==========================================
# CONCEPT: Clarity
# ==========================================
# Optional hints about types. Python ignores them but IDEs love them.

def greet(name: str) -> str:
    return "Hello " + name

# greet(123) # IDE might warn you, but Python runs it.but only specific ides

print(greet("John"))
print(greet(123))
# Road Sign Analogy

# Type hint = Speed limit board

# Driver (Python) can still overspeed

# Police (IDE / mypy) can warn

# Accident (runtime error) can still happen