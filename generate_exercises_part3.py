import os

# Base Directory
BASE_DIR = "Code"

# Helper Function to Create Files
def create_file(module, filename, content):
    path = os.path.join(BASE_DIR, module)
    os.makedirs(path, exist_ok=True)
    
    full_path = os.path.join(path, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created: {full_path}")

# ==========================================
# MODULE 6: Data Structures (Data Structures)
# ==========================================
m6 = "06_Data_Structures"

# Lists (1-10)
create_file(m6, "01_create_list.py", """# 1. Create List
# ==========================================
# CONCEPT: Collection
# ==========================================
# Lists hold multiple items in order. Mutable (changeable).

# Empty list
empty = []

# List with items
L = [1, 2, 3, "Apple", True] 

print(L)
# Why? To group related data (like a shopping list).
""")

create_file(m6, "02_access_list.py", """# 2. Access List Items
# ==========================================
# CONCEPT: Indexing
# ==========================================
# Just like strings, use [index].

L = [10, 20, 30, 40]
print(L[0]) # 10 (First)
print(L[-1]) # 40 (Last)

# Common Error: L[100] (IndexError)
""")

create_file(m6, "03_modify_list.py", """# 3. Modify List
# ==========================================
# CONCEPT: Mutable
# ==========================================
# You can change items inside a list.

L = ["Apple", "Banana", "Cherry"]
print(f"Before: {L}")

L[0] = "Orange" # Change Apple to Orange
print(f"After: {L}")
""")

create_file(m6, "04_append.py", """# 4. Append
# ==========================================
# CONCEPT: Adding Items
# ==========================================
# Adds to the END of the list.

L = [1, 2]
L.append(3)
L.append(4)
print(L) # [1, 2, 3, 4]
""")

create_file(m6, "05_insert.py", """# 5. Insert
# ==========================================
# CONCEPT: Injecting
# ==========================================
# Add item at a specific position.

L = ["A", "C"]
L.insert(1, "B") # Insert "B" at index 1
print(L) # ['A', 'B', 'C']
""")

create_file(m6, "06_remove.py", """# 6. Remove
# ==========================================
# CONCEPT: Deletion by Value
# ==========================================
# Removes the FIRST matching value.

L = [1, 2, 3, 2]
L.remove(2) # Removes the first 2
print(L) # [1, 3, 2]

# Common Error: L.remove(99) (ValueError if not found)
""")

create_file(m6, "07_pop.py", """# 7. Pop
# ==========================================
# CONCEPT: Deletion by Index
# ==========================================
# Removes item at index AND returns it. Default is last (-1).

L = ["A", "B", "C"]
removed = L.pop() # Removes "C"
print(f"Removed: {removed}")
print(f"List: {L}")
""")

create_file(m6, "08_sort.py", """# 8. Sort
# ==========================================
# CONCEPT: Ordering
# ==========================================
# Sorts the list in place (modifies original).

L = [3, 1, 4, 1, 5]
L.sort()
print(L)

# Reverse sort
L.sort(reverse=True)
print(L)
""")

create_file(m6, "09_reverse.py", """# 9. Reverse
# ==========================================
# CONCEPT: Flipping
# ==========================================
# Reverses order in place.

L = [1, 2, 3]
L.reverse()
print(L) # [3, 2, 1]
""")

create_file(m6, "10_list_comp.py", """# 10. List Comprehension
# ==========================================
# CONCEPT: Pythonic Loops
# ==========================================
# Create a list in one line. [expr for item in iterable]

# Old way
squares = []
for x in range(5):
    squares.append(x**2)

# New way
sq = [x**2 for x in range(5)]
print(sq)
""")

# Tuples (11-15)
create_file(m6, "11_create_tuple.py", """# 11. Create Tuple
# ==========================================
# CONCEPT: Immutable List
# ==========================================
# Use parentheses (). Cannot change after creation.

t = (1, 2, 3)
print(t)
""")

create_file(m6, "12_access_tuple.py", """# 12. Access Tuple
# ==========================================
# CONCEPT: Reading
# ==========================================
# Same as lists.

t = ("A", "B")
print(t[0])
""")

create_file(m6, "13_unpacking.py", """# 13. Unpacking
# ==========================================
# CONCEPT: Destructuring
# ==========================================
# Assign tuple items to variables.

coords = (10, 20)
x, y = coords # x=10, y=20
print(f"x={x}, y={y}")

# Common Error: Variables count must match Tuple size.
""")

create_file(m6, "14_immutable.py", """# 14. Immutability Check
# ==========================================
# CONCEPT: Safety
# ==========================================

t = (1, 2, 3)
# t[0] = 99 # TypeError!
print("Cannot change tuple items!")
""")

create_file(m6, "15_tuple_methods.py", """# 15. Tuple Methods
# ==========================================
# CONCEPT: Limited Tools
# ==========================================
# Only count() and index(). No append/remove!

t = (1, 2, 3, 2)
print(t.count(2)) # 2
print(t.index(3)) # 2 (Index of value 3)
""")

# Sets (16-25)
create_file(m6, "16_create_set.py", """# 16. Create Set
# ==========================================
# CONCEPT: Unique Collection
# ==========================================
# Use {}. No duplicates allowed. Unordered.

s = {1, 2, 3, 3, 3}
print(s) # {1, 2, 3}
""")

create_file(m6, "17_add.py", """# 17. Add to Set
# ==========================================
# CONCEPT: Single Item
# ==========================================

s = {1, 2}
s.add(3)
s.add(2) # Does nothing (Duplicate)
print(s)
""")

create_file(m6, "18_remove_set.py", """# 18. Remove from Set
# ==========================================
# CONCEPT: Deletion
# ==========================================

s = {1, 2, 3}
s.remove(2)
print(s)

# s.remove(99) # Error!
""")

create_file(m6, "19_union.py", """# 19. Union (|)
# ==========================================
# CONCEPT: Combining
# ==========================================
# All items from both sets.

A = {1, 2}
B = {3, 4}
print(A | B) # {1, 2, 3, 4}
""")

create_file(m6, "20_intersection.py", """# 20. Intersection (&)
# ==========================================
# CONCEPT: Common Items
# ==========================================
# Items in BOTH sets.

A = {1, 2, 3}
B = {2, 3, 4}
print(A & B) # {2, 3}
""")

create_file(m6, "21_difference.py", """# 21. Difference (-)
# ==========================================
# CONCEPT: Subtraction
# ==========================================
# Items in A but NOT in B.

A = {1, 2, 3}
B = {2, 3, 4}
print(A - B) # {1}
""")

create_file(m6, "22_unique_list.py", """# 22. Deduplicate List
# ==========================================
# CONCEPT: Power Move
# ==========================================
# Convert List -> Set -> List.

L = [1, 2, 2, 3, 3, 3]
unique = list(set(L))
print(unique)
""")

create_file(m6, "23_subset.py", """# 23. Subset (<)
# ==========================================
# CONCEPT: Containment
# ==========================================

small = {1, 2}
big = {1, 2, 3, 4}
print(small < big) # True
""")

create_file(m6, "24_frozenset.py", """# 24. Frozenset
# ==========================================
# CONCEPT: Immutable Set
# ==========================================
# Like a tuple, but for sets. Can be used as Dict Key.

fs = frozenset([1, 2, 3])
# fs.add(4) # Error!
print(fs)
""")

create_file(m6, "25_discard.py", """# 25. Discard (Safe Remove)
# ==========================================
# CONCEPT: Safety
# ==========================================
# Like remove(), but no error if item missing.

s = {1, 2}
s.discard(99) # No error
print(s)
""")

# Dictionaries (26-40)
create_file(m6, "26_create_dict.py", """# 26. Create Dictionary
# ==========================================
# CONCEPT: Key-Value Pairs
# ==========================================
# Use {key: value}.

d = {
    "name": "Alice",
    "age": 25,
    "city": "Paris"
}
print(d)
""")

create_file(m6, "27_access_dict.py", """# 27. Access Dictionary
# ==========================================
# CONCEPT: Lookups
# ==========================================
# Use the Key to get the Value.

d = {"name": "Bob", "age": 30}
print(d["name"]) # Bob

# Common Error: d["job"] (KeyError)
""")

create_file(m6, "28_add_key.py", """# 28. Add/Modify Item
# ==========================================
# CONCEPT: Assignment
# ==========================================

d = {}
d["name"] = "Charlie" # Add new
d["name"] = "Chuck"   # Overwrite existing
print(d)
""")

create_file(m6, "29_modify_val.py", """# 29. Modify Value
# ==========================================
# CONCEPT: Update
# ==========================================

stats = {"score": 10}
stats["score"] += 5
print(stats)
""")

create_file(m6, "30_keys.py", """# 30. Keys
# ==========================================
# CONCEPT: Iteration
# ==========================================
# Get all keys.

d = {"a": 1, "b": 2}
keys = d.keys()
print(list(keys))
""")

create_file(m6, "31_values.py", """# 31. Values
# ==========================================
# CONCEPT: Iteration
# ==========================================
# Get all values.

d = {"a": 1, "b": 2}
vals = d.values()
print(list(vals))
""")

create_file(m6, "32_items.py", """# 32. Items
# ==========================================
# CONCEPT: Iteration
# ==========================================
# Get pairs (tuples).

d = {"a": 1, "b": 2}
for k, v in d.items():
    print(f"Key: {k}, Value: {v}")
""")

create_file(m6, "33_get.py", """# 33. Get Method
# ==========================================
# CONCEPT: Safe Access
# ==========================================
# Returns None (or default) if key missing. No Error!

d = {"name": "Alice"}
print(d.get("age")) # None
print(d.get("age", 0)) # 0 (Default)
""")

create_file(m6, "34_pop_dict.py", """# 34. Pop Dictionary
# ==========================================
# CONCEPT: Removal
# ==========================================
# Removes key and returns value.

d = {"a": 1, "b": 2}
val = d.pop("a")
print(val)
print(d)
""")

create_file(m6, "35_update.py", """# 35. Update
# ==========================================
# CONCEPT: Merge
# ==========================================
# Adds keys from another dict. Overwrites if present.

d1 = {"a": 1}
d2 = {"b": 2, "a": 100}
d1.update(d2)
print(d1) # {'a': 100, 'b': 2}
""")

create_file(m6, "36_iter_dict.py", """# 36. Iterate Dictionary
# ==========================================
# CONCEPT: Loop
# ==========================================

d = {"Apple": 1.2, "Banana": 0.5}
for fruit in d: # Loops over KEYS by default
    print(f"{fruit}: ${d[fruit]}")
""")

create_file(m6, "37_dict_comp.py", """# 37. Dictionary Comprehension
# ==========================================
# CONCEPT: One-Liner Dict
# ==========================================
# {k:v for item in iterable}

nums = [1, 2, 3]
sq_dict = {x: x**2 for x in nums}
print(sq_dict) # {1: 1, 2: 4, 3: 9}
""")

create_file(m6, "38_defaultdict.py", """# 38. DefaultDict
# ==========================================
# CONCEPT: Advanced Dict
# ==========================================
# Auto-creates values if missing.

from collections import defaultdict
d = defaultdict(int) # Default value 0
d["a"] += 1
print(d["a"])
""")

create_file(m6, "39_counter.py", """# 39. Counter
# ==========================================
# CONCEPT: Counting Tool
# ==========================================
# Auto-counts items in a list.

from collections import Counter
L = ["A", "A", "B"]
c = Counter(L)
print(c) # Counter({'A': 2, 'B': 1})
""")

create_file(m6, "40_del_key.py", """# 40. Del Keyword
# ==========================================
# CONCEPT: Deletion
# ==========================================
# The dangerous way to delete.

d = {"a": 1}
del d["a"]
# del d["a"] # KeyError!
""")

create_file(m6, "99_Practice_Problems.py", """# ==========================================
# MODULE 6: PRACTICE PROBLEMS
# ==========================================
# 1. Create a list of 5 favorite movies. Print the 3rd one.
# 2. Add a new movie to the end of the list.
# 3. Remove the first movie by name.
# 4. Sort the list alphabetically.
# 5. Create a Tuple representing a coordinate (x, y, z).
# 6. Unpack the tuple into variables x, y, z.
# 7. Create a Set of colors "Red", "Blue", "Red". Print it (Duplicates?).
# 8. Check if "Green" is in the color set.
# 9. Create a Dictionary representing a "Book" (Title, Author, Year).
# 10. Change the Year of the book.
# 11. Add a new key "Genre" to the book dict.
# 12. Write a loop to print all Keys and Values of the book dict.
# 13. Create a list of numbers 1-10. Use slicing to get the first 5.
# 14. Use List Comprehension to create a list of even numbers 0-20.
# 15. Given L=[10, 20, 30], use pop() to remove and print the last item.
# 16. Combine two sets: A={1,2} and B={2,3} (Union).
# 17. Find the difference: A={1,2} - B={2,3}.
# 18. Count how many times the number 5 appears in tuple T=(1,5,5,5,2).
# 19. Start with an empty list. Use a loop to add numbers 1 to 5.
# 20. Count frequency of words in string "to be or not to be" using a Dict.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. movies=["A","B","C","D","E"]; print(movies[2])
2. movies.append("F")
3. movies.remove("A")
4. movies.sort()
5. t=(10, 20, 30)
6. x,y,z=t
7. s={"Red","Blue","Red"}; print(s) (One Red)
8. print("Green" in s)
9. book={"Title":"X", "Author":"Y", "Year":2000}
10. book["Year"]=2024
11. book["Genre"]="Fiction"
12. for k,v in book.items(): print(k, v)
13. L=list(range(1,11)); print(L[:5])
14. [x for x in range(21) if x%2==0]
15. print(L.pop())
16. print(A | B)
17. print(A - B)
18. print(T.count(5))
19. L=[]; for i in range(1,6): L.append(i)
20. s="to be..."; d={}; for w in s.split(): d[w]=d.get(w,0)+1
'''
""")

print("Generated Module 6!")
