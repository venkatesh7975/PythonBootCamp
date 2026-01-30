# 11. f-strings
# ==========================================
# CONCEPT: Formatting
# ==========================================
# The best way to inject variables into strings.
# Put an 'f' before the quote and use {}.

name = "Bob"
age = 30
print(f"Hi {name}, you are {age}.") 

# Common Error: Forgetting the 'f' prints "{name}" literally.
