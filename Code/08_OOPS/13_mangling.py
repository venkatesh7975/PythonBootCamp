# 13. Name Mangling
# ==========================================
# CONCEPT: Strong Hiding
# ==========================================

class Secret:
    def __init__(self):
        self.__code = 1234

s = Secret()
# print(s.__code) # Error!
print(s._Secret__code) # The back door way to access it.
