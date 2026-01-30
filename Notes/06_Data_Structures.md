# 6️⃣ Data Structures: The Organizers 🗄️

Welcome to **The Warehouse**! 🏬 Imagine buying 1000 items from Amazon. You don't dump them on the floor. You organize them!

---

## 21. Lists: The Infinite Shopping List 📝

> **Definition**: Ordered, Mutable collection.

### 🛒 Analogy: Sticky Note Pad
*   **Ordered**: Milk is #1, Eggs are #2.
*   **Mutable**: You can cross off items or add new ones.
*   **Duplicates**: You can have "Milk" written twice.

**Syntax**: `[item1, item2]`

**Methods**:
*   `append("Candy")`: Add to end. 🍬
*   `pop()`: Remove the last item. 💨
*   `sort()`: Organize A-Z. 🔤

---

## 22. Sets: The VIP Club 🎟️

> **Definition**: Unordered, Unique items only.

### 🎒 Analogy: A Bag of Marbles
*   **Unordered**: Reach in, you don't know which color you grab first.
*   **Unique**: If you have two Red marbles, the Bag only counts "Red" once.

**Syntax**: `{item1, item2}`

**Power Move**: Removing duplicates from a list!
`list(set([1, 2, 2, 3]))` -> `[1, 2, 3]`

---

## 23. Tuples: The Sealed Letter ✉️

> **Definition**: Ordered, Immutable collection.

### 🔒 Analogy: GPS Coordinates
Once you set the coordinates for "Home", you don't want them to change by accident!
`(40.7128, -74.0060)` -> NYC 🗽.
If you change one number, you end up in the ocean. 🌊

**Syntax**: `(item1, item2)`

**Why use it?**
1.  **Safety**: Data integrity.
2.  **Speed**: Faster than lists. ⚡

---

## 24. Dictionaries: The Magic Book 📖

> **Definition**: Key-Value Pairs.

### 📞 Analogy: The Phonebook
*   **Key**: Name (Must be unique!)
*   **Value**: Phone Number.

**Syntax**: `{"key": "value"}`

**Example**:
```python
student = {
    "name": "Alex",
    "age": 20,
    "grade": "A"
}
```

**Accessing**:
*   `student["name"]` -> `"Alex"`
*   `student["grade"]` -> `"A"`

---

## 🕵️‍♂️ Debugging Detective: The Missing Key

**Scenario**:
```python
scores = {"Alice": 90, "Bob": 85}
print(scores["Charlie"])
```
**Error**: `KeyError: 'Charlie'` ❌
**Why?**: "Charlie" isn't in the dictionary!
**Fix**: Use `.get()`!
`print(scores.get("Charlie", "Not Found"))` -> `"Not Found"` ✅

---

## 🏋️‍♀️ Gym Time: Mental Reps

1.  **List Logic**: If `my_list = [1, 2, 3]`, what does `my_list.pop()` return? And what is left in `my_list`?
2.  **Set Stylin'**: `my_set = {1, 2, 2, 3}`. How many items are in it?
3.  **Tuple Trouble**: `t = (1, 2)`. Can I do `t[0] = 5`? Why not?
4.  **Dictionary Dare**: Create a dictionary for a "Car" with keys: `Brand`, `Model`, `Year`.

---

## 🤣 Fun Zone

**Q: Why was the computer cold?**
**A:** Because it left its Windows open! 🪟❄️

---

## 🏆 Challenge Mode: 20 Practice Problems

### 🧠 Conceptual (Multiple Choice & Short Answer)

1.  **Mutability**: Which of these is Immutable? List, Set, Dictionary, Tuple.
2.  **Order**: Does a Set keep items in the order you added them?
3.  **Duplicates**: If you add "Apple" twice to a Set, how many "Apple"s are there?
4.  **Syntax**: Which brackets does a List use?
5.  **Access**: How do you access the value associated with key "Age" in dict `d`?
6.  **Method**: What list method adds an item to the end?
7.  **Key Type**: Can a List be a key in a Dictionary? (Hint: Keys must be immutable).
8.  **Empty**: How do you create an empty Tuple?
9.  **LIFO**: Lists can act as a Stack. What method removes the last element?
10. **Conversion**: How do you turn a List `L` into a Set?

### 💻 Coding Challenges

11. **List Access**: Print the 2nd item of `L = [10, 20, 30]`.
12. **Dict Add**: Add `{"City": "Paris"}` to existing dict `person`.
13. **Set Unique**: Given `L = [1, 1, 2, 2, 3]`, print the unique numbers.
14. **Tuple Unpack**: Given `t = (10, 20)`, assign them to `x` and `y` in one line.
15. **List Change**: Change the first item of `L = ["A", "B"]` to "Z".
16. **Dict Check**: Check if "Score" is a key in `d = {"Name": "Ash"}`.
17. **List Slicing**: Print the last 2 items of `L = [1, 2, 3, 4, 5]`.
18. **Nested Access**: Given `data = {"User": {"Name": "Sam"}}`, print "Sam".
19. **List Math**: Multiply every number in `[1, 2, 3]` by 2 and print the new list.
20. **Merge**: Combine two lists `A = [1, 2]` and `B = [3, 4]` into one.

<details>
<summary><strong>⬇️ Click to Reveal Solutions</strong></summary>

**Conceptual Answers**
1. Tuple.
2. No.
3. One.
4. Square `[]`.
5. `d["Age"]`.
6. `.append()`.
7. No (because Lists are mutable).
8. `()` or `tuple()`.
9. `.pop()`.
10. `set(L)`.

**Coding Answers**
11. `print(L[1])`.
12. `person["City"] = "Paris"`.
13. `print(list(set(L)))`.
14. `x, y = t`.
15. `L[0] = "Z"`.
16. `if "Score" in d: ...`.
17. `print(L[-2:])`.
18. `print(data["User"]["Name"])`.
19. `new_L = [x*2 for x in [1, 2, 3]]` (List Comprehension) or loop.
20. `C = A + B`.
</details>

---
**Next Up:** We learn how to automate tasks with **Functions**! 🤖
