# 5. Print End
# ==========================================
# CONCEPT: Customizing Output (end)
# ==========================================
# Why? By default, print() creates a new line. Sometimes we want to stay on the same line.
# How? Use the `end="..."` argument.

print("Hello", end=" ")
print("World")
# Output: Hello World (on one line)

print("Loading", end="...")
print("Done!")

# Common Errors:
# 1. Forgetting to add a space in end=" " will mash words together (HelloWorld).
