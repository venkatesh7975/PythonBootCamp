# 39. Counter
# ==========================================
# CONCEPT: Counting Tool
# ==========================================
# Auto-counts items in a list.

from collections import Counter
L = ["A", "A", "B"]
c = Counter(L)
print(c) # Counter({'A': 2, 'B': 1})
