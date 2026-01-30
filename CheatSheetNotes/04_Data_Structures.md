# 📦 Python Cheat Sheet: Data Structures

## 1. Lists `[]` (Ordered, Mutable)
- **Access**: `L[0]`, `L[-1]`.
- **Add**: `L.append(x)` (to end), `L.insert(0, x)` (at index).
- **Remove**: `L.pop()` (last), `L.remove(value)` (by name), `del L[0]`.
- **Sort**: `L.sort()` (in-place), `sorted(L)` (returns new list).
- **Comprehension**: `[x**2 for x in range(10) if x%2==0]`

## 2. Tuples `()` (Ordered, Immutable)
- **Why?** Faster than lists, protected from change.
- **Single item**: `t = (5,)` (Comma is required!).
- **Unpacking**: `x, y = (10, 20)`

## 3. Sets `{}` (Unordered, Unique)
- **Best for**: Removing duplicates, membership testing.
- **Ops**: `A | B` (Union), `A & B` (Intersection), `A - B` (Difference).
- **Add**: `S.add(x)`, `S.remove(x)`.

## 4. Dictionaries `{"key": "val"}` (Unordered/Ordered, Mapped)
- **Access**: `d["name"]` or `d.get("name", "Default")` (No error if missing!).
- **Keys/Values**: `d.keys()`, `d.values()`, `d.items()`.
- **Delete**: `del d["key"]` or `d.pop("key")`.

## Summary Table
| Structure | Symbol | Mutable? | Ordered? | Duplicates? |
|-----------|---------|----------|----------|-------------|
| **List** | `[]` | Yes | Yes | Yes |
| **Tuple** | `()` | No | Yes | Yes |
| **Set** | `{}` | Yes | No | **No** |
| **Dict** | `{k:v}` | Yes | Yes* | No (Keys) |
*\*As of Python 3.7+*
