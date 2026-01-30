# Interactive Quiz - Module 1
import time

def quiz():
    print("Welcome to the Module 1 Quiz! (Press Enter to reveal answers)")
    print("-" * 50)
    
    questions = [
        ("Write a program to print 'Welcome to Python' 3 times.", 
         "print('Welcome to Python\\n' * 3)"),
         
        ("Print 'Python', 'is', 'fun' separated by underscores (_).", 
         "print('Python', 'is', 'fun', sep='_')"),
         
        ("Print 'Code' and 'Time' on the same line, separated by a star (*).", 
         "print('Code', 'Time', sep='*')"),
         
        ("Write an algorithm (print steps) to Tie Shoelaces.", 
         "print('1. Grab laces...'); print('2. Cross them...')"),
         
        ("Fix this code: Print('Hello World')", 
         "print('Hello World') (Lowercase p)"),
         
        ("Print a square using hashes (#).", 
         "print('###\\n# #\\n###')"),
         
        ("Use escape characters to print: 'Title' then a newline, then 'Subtitle'.", 
         "print('Title\\nSubtitle')"),
         
        ("Print the calculation: 5 + 10 = 15 (Just print the text).", 
         "print('5 + 10 = 15')"),
         
        ("Print 'Loading' ending with 3 dots, then 'Complete' on the same line.", 
         "print('Loading', end='...'); print('Complete')"),
         
        ("Create a simple 'Menu' using print statements (Start, Options, Exit).", 
         "print('1. Start\\n2. Options\\n3. Exit')"),
         
        ("Debug this: variable score = 100. Print 'Score is 100'.", 
         "score=100; print(f'Score is {score}')"),
         
        ("Print a Triangle using stars.", 
         "print('  *  \\n *** \\n*****')"),
         
        ("Print 'Quotes' inside a string: She said 'Hi'.", 
         "print('She said "Hi"')"),
         
        ("Print your name, age, and city on separate lines using one print() command with \\n.", 
         "print('Name\\nAge\\nCity')"),
         
        ("Print the following path: C:\\Users\\Name (Hint: Escaping backslashes).", 
         "print('C:\\\\Users\\\\Name')"),
         
        ("Using 'sep', print time: 12 : 30 : 00.", 
         "print(12, 30, 00, sep=' : ')"),
         
        ("Using 'end', print a progress bar: [#####     ].", 
         "print('[', end=''); print('#'*5, end=''); print(' '*5, end=''); print(']')"),
         
        ("Write a comment explaining what `print()` does.", 
         "# functions displays text to console"),
         
        ("Print a Diamond shape.", 
         "print('  *  \\n *** \\n  *  ')"),
         
        ("Make a 'Business Card' output with borders.", 
         "print('________'); print('| Name |'); print('|______|')")
    ]

    score = 0
    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        user_input = input("   Your Answer (Mental or Type it): ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
