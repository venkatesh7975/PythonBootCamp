# 38. DefaultDict
# ==========================================
# CONCEPT: Advanced Dict
# ==========================================
# Auto-creates values if missing.

from collections import defaultdict
d = defaultdict(int) # Default value 0
d["a"] += 1
print(d["a"])
