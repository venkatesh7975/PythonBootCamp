# 6. Speed Test
# ==========================================
# CONCEPT: Execution Speed
# ==========================================
# Python is 'slow' compared to C because it's interpreted. 
# But let's see how fast it counts to 1 million.

import time
start = time.time()

# Count to 1,000,000
for i in range(1000000):
    pass

end = time.time()
print(f"Time taken: {end - start:.5f} seconds")
