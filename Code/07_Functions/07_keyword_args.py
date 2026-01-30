# 7. Keyword Arguments
# ==========================================
# CONCEPT: Named Input
# ==========================================
# Order doesn't matter if you use names.

def describe_pet(animal, name):
    print(f"I have a {animal} named {name}")

# Correct
describe_pet(animal="Dog", name="Rex")
# Also Correct (Order swapped!)
describe_pet(name="Rex", animal="Dog")
