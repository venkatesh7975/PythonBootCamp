# 30. Short Circuiting
# ==========================================
# CONCEPT: Optimization
# ==========================================
# Python stops checking if it already knows the answer.

# OR: If first is True, answer is True. Skips second part.
print(True or (1/0)) # No crash!

# AND: If first is False, answer is False. Skips second part.
print(False and (1/0)) # No crash!
