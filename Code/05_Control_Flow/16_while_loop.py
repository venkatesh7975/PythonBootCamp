# 16. While Loop
# ==========================================
# CONCEPT: Conditional Loop
# ==========================================
# Runs AS LONG AS the condition is True.

energy = 3
while energy > 0:
    print(f"Running... Energy: {energy}")
    energy -= 1 # Crucial! Or infinite loop.
print("Stopped.")
