# ⚙️ Python Cheat Sheet: Functions & Advanced

## 1. Function Basics
```python
def greet(name="User"): # Default argument
    return f"Hello {name}"

res = greet("Alice")
```

## 2. Dynamic Arguments
- `*args`: Collects extra positional arguments into a **Tuple**.
- `**kwargs`: Collects extra keyword arguments into a **Dictionary**.
```python
def my_func(*args, **kwargs):
    print(args)   # (1, 2)
    print(kwargs) # {'a': 3}

my_func(1, 2, a=3)
```

## 3. Lambda (One-line Functions)
- **Syntax**: `lambda arguments: expression`
- `square = lambda x: x * x`
- Often used with `map()` and `filter()`.

## 4. Scope (LEGB Rule)
1. **L**ocal (Inside function)
2. **E**nclosing (Nested functions)
3. **G**lobal (Top level)
4. **B**uilt-in (Python keywords)
- Use `global x` or `nonlocal x` to modify higher-level variables.

## 5. Modern Tools
- **Decorators**: `@my_decorator` - Wrap functions with extra logic.
- **Generators**: `yield` instead of `return` - Creates an iterator (Memory efficient!).
- **Recursion**: Function calling itself. (Must have a **Base Case**!).
