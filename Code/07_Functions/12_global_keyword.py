# 12. Global Keyword
# ==========================================
# CONCEPT: Modification
# ==========================================
# To CHANGE a global variable, declare it global inside function.

count = 0

def increment():
    global count
    count += 1

increment()
print(count) # 1
