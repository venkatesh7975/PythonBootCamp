# 9. Arbitrary Keywords (**kwargs)
# ==========================================
# CONCEPT: Dictionary Input
# ==========================================
# Collects named arguments into a Dictionary.

def build_profile(**user_info):
    print(user_info)

build_profile(name="Alice", age=30, job="Dev")
# {'name': 'Alice', 'age': 30, 'job': 'Dev'}
