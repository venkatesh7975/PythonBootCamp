# Interactive Quiz - Module 2
import time

def quiz():
    print("Welcome to the Module 2 Quiz! (Press Enter to reveal answers)")
    print("-" * 50)
    
    questions = [
        ("Write a script that inputs a number and prints its binary version.", 
         "n=int(input()); print(bin(n))"),
         
        ("Simulate a 'Loading RAM' bar using sleep() and print.", 
         "import time; print('Loading...'); time.sleep(2); print('Done')"),
         
        ("Print the memory address of the string 'Hello'.", 
         "print(id('Hello'))"),
         
        ("Create two variables with the same value (e.g., 500) and check if their addresses are same (id(a) == id(b)).", 
         "a=500; b=500; print(id(a)==id(b))"),
         
        ("Write a script that crashes nicely (using try-except) demonstrating Interpreter checking.", 
         "try: print(1/0) except: print('Crash averted')"),
         
        ("Measure how long it takes to print 'Hello' 1000 times.", 
         "start=time.time(); loop...; end=time.time()"),
         
        ("Input your OS name manually and print 'You are using [OS]'.", 
         "os_name = input(); print(f'You are using {os_name}')"),
         
        ("Calculate the size of a large string 'A' * 1000 in bytes.", 
         "import sys; print(sys.getsizeof('A'*1000))"),
         
        ("Write a 'BIOS Check' script that prints 'Checking CPU... OK', 'Checking RAM... OK'.", 
         "print('Checking CPU... OK') etc."),
         
        ("Simulate an infinite loop (use Ctrl+C to stop, or add a break).", 
         "while True: break # Safety break"),
         
        ("Convert binary '0b101' back to integer (print(0b101)).", 
         "print(0b101) # Output: 5"),
         
        ("Write a script that deletes a variable `secret` and tries to print it (expect Error).", 
         "secret=1; del secret; print(secret)"),
         
        ("Input 2 numbers and print their sum. Use a comment to label Input and Output devices.", 
         "# Input: Keyboard; res = int(input()) + int(input()); # Output: Monitor; print(res)"),
         
        ("Print the result of 2 to the power of 100.", 
         "print(2**100)"),
         
        ("Create a variable `x = None`. Print its memory address.", 
         "x=None; print(id(x))"),
         
        ("Show that `True` is actually `1` in memory (print(True + True)).", 
         "print(True+True) # 2"),
         
        ("Use `time.sleep` to make a countdown timer (3... 2... 1... Go!).", 
         "time.sleep(1)..."),
         
        ("Write a script that imports `sys` and prints `sys.version`.", 
         "import sys; print(sys.version)"),
         
        ("Define a variable, print it, delete it, redefine it, print it again.", 
         "x=1; print(x); del x; x=2; print(x)"),
         
        ("Explain in a comment: What is the difference between HDD and RAM?", 
         "# RAM is fast/volatile (Workbench). HDD is slow/permanent (Library).")
    ]

    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        user_input = input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
