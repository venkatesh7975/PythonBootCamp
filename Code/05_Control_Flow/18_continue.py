# 18. Continue
# ==========================================
# CONCEPT: Skip
# ==========================================
# Skips the rest of THIS iteration and goes to next.

for i in range(5):
    if i == 3:
        print("Skipping 3")
        continue 
    print(i)
