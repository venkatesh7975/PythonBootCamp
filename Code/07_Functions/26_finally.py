# 26. Finally Block
# ==========================================
# CONCEPT: Cleanup
# ==========================================
# Runs no matter what.

try:
    f = open("data.txt", "w")
    f.write("Hi")
except:
    print("Error")
finally:
    f.close() # Always close file!
    print("Closed file.")
