# ==========================================
# MODULE 7: PRACTICE PROBLEMS
# ==========================================
# 1. Define a function `greet(name)` that prints "Hello, [name]".
# 2. Define `add(a, b)` that returns sum. Call it with 5, 10.
# 3. Write a function with a default argument `country="Unknown"`.
# 4. Write a function that accepts `*args` and prints the count of arguments.
# 5. Write a function that accepts `**kwargs` and prints all keys.
# 6. Create a global variable `count` and increment it inside a function.
# 7. Write a recursive function to calculate factorial of n.
# 8. Use `map` and `lambda` to square a list of numbers.
# 9. Use `filter` and `lambda` to get even numbers from a list.
# 10. Write a function with a Docstring and print the docstring.
# 11. Create a simple generator that yields "A", "B", "C".
# 12. Write a function nested inside another function.
# 13. Create a decorator that prints "Running..." before the function.
# 14. Handle a `ValueError` when converting user input string to int.
# 15. Use `finally` to print "Done" after a try-except block.
# 16. Raise a `TypeError` if an argument `n` is not an int.
# 17. Use assert to check if `2+2 == 4`.
# 18. Write a function that returns MULTIPLE values (e.g. min and max) (Return tuple).
# 19. Create a lambda that adds 10 to a number.
# 20. Write a recursive function to print a countdown.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. def greet(n):...
2. def add(a,b): return a+b
3. def origin(country="Unknown"):...
4. def count_args(*args): print(len(args))
5. def print_keys(**kwargs): print(kwargs.keys())
6. global count; count+=1
7. if n==1: return 1 else n*fact(n-1)
8. list(map(lambda x: x**2, L))
9. list(filter(lambda x: x%2==0, L))
10. def f(): "Doc"; ...; print(f.__doc__)
11. def gen(): yield "A"...
12. def out(): def in():...
13. def dec(f): def wrap(): print("Run"); f(); return wrap
14. try: int("a") except ValueError: ...
15. finally: print("Done")
16. if not isinstance(n, int): raise TypeError
17. assert 2+2==4
18. return min(L), max(L)
19. f = lambda x: x+10
20. def cd(n): if n>0: print(n); cd(n-1)
'''
