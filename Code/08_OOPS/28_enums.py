# 28. Enums
# ==========================================
# CONCEPT: Constants
# ==========================================
# Enumerations for fixed options.

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.RED)
