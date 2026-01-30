# 17. Break
# ==========================================
# CONCEPT: Eject
# ==========================================
# Exits the loop IMMEDIATELY.

for i in range(10):
    if i == 5:
        print("Found 5! Stopping.")
        break
    print(i)
