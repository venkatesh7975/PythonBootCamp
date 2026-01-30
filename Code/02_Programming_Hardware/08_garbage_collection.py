# 8. Garbage Collection
# ==========================================
# CONCEPT: Memory Management
# ==========================================
# Python has a 'Garbage Collector' that deletes variables you don't use anymore 
# to free up RAM.

x = [1, 2, 3] # Create list in memory
print("List created.")

del x # Manually delete 'reference' to list
# The Garbage Collector will now remove the list from RAM.

# print(x) # This works cause NameError (x is gone)
print("x deleted from memory.")
