# 9. Immutability
# ==========================================
# CONCEPT: Unchangeable
# ==========================================
# Once created, a string cannot be changed in place.
# You must create a NEW string.

s = 'Hello'
# s[0] = 'J' # TypeError: 'str' object does not support item assignment

s = 'J' + s[1:] # New string 'Jello'
print(s)
