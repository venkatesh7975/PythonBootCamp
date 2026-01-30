# 19. Type Hints
# ==========================================
# CONCEPT: Clarity
# ==========================================
# Optional hints about types. Python ignores them but IDEs love them.

def greet(name: str) -> str:
    return "Hello " + name

# greet(123) # IDE might warn you, but Python runs it.
