# 12. Encapsulation (Private)
# ==========================================
# CONCEPT: Hiding
# ==========================================
# _name (Weak private, convention)
# __name (Strong private, mangled)

class Account:
    def __init__(self):
        self._balance = 0 # Private-ish

a = Account()
# We should access it via methods, but python allows direct access if we really want.
