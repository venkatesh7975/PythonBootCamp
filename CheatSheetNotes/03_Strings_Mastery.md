# 🧵 Python Cheat Sheet: Strings Mastery

## 1. Creation & Quotes
- `s1 = 'Single'`
- `s2 = "Double"`
- `s3 = """Triple (Multiline)"""`

## 2. Slicing Syntax: `[start : stop : step]`
- `s[0]`: First char.
- `s[-1]`: Last char.
- `s[1:4]`: Indices 1, 2, 3 (Stop is exclusive!).
- `s[:3]`: Start to index 2.
- `s[2:]`: Index 2 to the end.
- `s[::-1]`: **Reverse the string.**
- `s[::2]`: Every 2nd character.

## 3. Formatting (The f-string 🔗)
```python
name = "Neo"
print(f"Follow the white rabbit, {name}.") 
```

## 4. Key String Methods
| Method | Description |
|--------|-------------|
| `.upper()` / `.lower()` | Change case. |
| `.strip()` | Remove whitespace from ends. |
| `.replace("A", "B")` | Replace A with B. |
| `.split(",")` | String -> List (breaks at comma). |
| `"-".join(list)` | List -> String (glues with dash). |
| `.find("x")` | Get index of "x" (or -1). |
| `.count("a")` | How many "a"s? |

## 5. Immutability
Strings **CANNOT** be changed in place. 
- ❌ `s[0] = "J"` (Error!)
- ✅ `s = "J" + s[1:]` (Create a NEW string)
