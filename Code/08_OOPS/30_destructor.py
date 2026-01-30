# 30. Destructor (__del__)
# ==========================================
# CONCEPT: Cleanup
# ==========================================
# Runs when object is deleted. (Rarely used, but good to know).

class FileHandler:
    def __del__(self):
        print("File Closed.")

f = FileHandler()
del f # Triggers __del__
