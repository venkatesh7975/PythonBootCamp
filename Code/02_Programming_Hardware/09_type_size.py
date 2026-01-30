# 9. Size of Objects
# ==========================================
# CONCEPT: Bits and Bytes
# ==========================================
# Everything takes up space in RAM.
# sys.getsizeof() tells us how big an object is in bytes.

import sys
x = 10
print(f"Size of integer 10: {sys.getsizeof(x)} bytes")
# It's not just 4 bytes! Python integers are objects with overhead.
