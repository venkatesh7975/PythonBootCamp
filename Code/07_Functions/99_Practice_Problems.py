# Interactive Practice Problems - Module 7 (Functions)
import time

def quiz():
    print("Welcome to the Module 7 Practice Quiz! (Functions)")
    print("Press Enter to reveal the answer to each question.")
    print("-" * 50)
    
    questions = [
        ("Define a function `greet(name)` that prints 'Hello, [name]'.", 
         "def greet(n):..."),
         
        ("Define `add(a, b)` that returns sum. Call it with 5, 10.", 
         "def add(a,b): return a+b"),
         
        ("Write a function with a default argument `country='Unknown'`.", 
         "def origin(country='Unknown'):..."),
         
        ("Write a function that accepts `*args` and prints the count of arguments.", 
         "def count_args(*args): print(len(args))"),
         
        ("Write a function that accepts `**kwargs` and prints all keys.", 
         "def print_keys(**kwargs): print(kwargs.keys())"),
         
        ("Create a global variable `count` and increment it inside a function.", 
         "global count; count+=1"),
         
        ("Write a recursive function to calculate factorial of n.", 
         "if n==1: return 1 else n*fact(n-1)"),
         
        ("Use `map` and `lambda` to square a list of numbers.", 
         "list(map(lambda x: x**2, L))"),
         
        ("Use `filter` and `lambda` to get even numbers from a list.", 
         "list(filter(lambda x: x%2==0, L))"),
         
        ("Write a function with a Docstring and print the docstring.", 
         "def f(): 'Doc'; ...; print(f.__doc__)"),
         
        ("Create a simple generator that yields 'A', 'B', 'C'.", 
         "def gen(): yield 'A'..."),
         
        ("Write a function nested inside another function.", 
         "def out(): def in():..."),
         
        ("Create a decorator that prints 'Running...' before the function.", 
         "def dec(f): def wrap(): print('Run'); f(); return wrap"),
         
        ("Handle a `ValueError` when converting user input string to int.", 
         "try: int('a') except ValueError: ..."),
         
        ("Use `finally` to print 'Done' after a try-except block.", 
         "finally: print('Done')"),
         
        ("Raise a `TypeError` if an argument `n` is not an int.", 
         "if not isinstance(n, int): raise TypeError"),
         
        ("Use assert to check if `2+2 == 4`.", 
         "assert 2+2==4"),
         
        ("Write a function that returns MULTIPLE values (e.g. min and max) (Return tuple).", 
         "return min(L), max(L)"),
         
        ("Create a lambda that adds 10 to a number.", 
         "f = lambda x: x+10"),
         
        ("Write a recursive function to print a countdown.", 
         "def cd(n): if n>0: print(n); cd(n-1)")
    ]
    
    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
