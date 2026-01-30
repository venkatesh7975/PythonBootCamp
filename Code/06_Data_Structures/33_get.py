# 33. Get Method
# ==========================================
# CONCEPT: Safe Access
# ==========================================
# Returns None (or default) if key missing. No Error!

d = {"name": "Alice"}
print(d.get("age")) # None
print(d.get("age", 0)) # 0 (Default)
