# 6. Slicing [Start:Stop]
# ==========================================
# CONCEPT: Extraction
# ==========================================
# Grab a chunk of text.
# Start is inclusive. Stop is exclusive (not included).

s = 'Python'
print(s[0:2]) # 'Py' (Indices 0, 1. Stop at 2)
print(s[2:])  # 'thon' (From 2 to end)
print(s[:2])  # 'Py' (From start to 2)
