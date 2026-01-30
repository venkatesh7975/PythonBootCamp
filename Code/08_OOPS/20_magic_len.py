# 20. Magic Method (__len__)
# ==========================================
# CONCEPT: Size
# ==========================================
# Controls len(obj).

class Cart:
    items = ["A", "B", "C"]
    
    def __len__(self):
        return len(self.items)

c = Cart()
print(len(c)) # 3
