# ==========================================
# MODULE 2: PRACTICE PROBLEMS
# ==========================================
# 1. Write a script that inputs a number and prints its binary version.
# 2. Simulate a "Loading RAM" bar using sleep() and print.
# 3. Print the memory address of the string "Hello".
# 4. Create two variables with the same value (e.g., 500) and check if their addresses are same (id(a) == id(b)).
# 5. Write a script that crashes nicely (using try-except) demonstrating Interpreter checking.
# 6. Measure how long it takes to print "Hello" 1000 times.
# 7. Input your OS name manually and print "You are using [OS]".
# 8. Calculate the size of a large string "A" * 1000 in bytes.
# 9. Write a "BIOS Check" script that prints "Checking CPU... OK", "Checking RAM... OK".
# 10. Simulate an infinite loop (use Ctrl+C to stop, or add a break).
# 11. Convert binary "0b101" back to integer (print(0b101)).
# 12. Write a script that deletes a variable `secret` and tries to print it (expect Error).
# 13. Input 2 numbers and print their sum. Use a comment to label Input and Output devices.
# 14. Print the result of 2 to the power of 100.
# 15. Create a variable `x = None`. Print its memory address.
# 16. Show that `True` is actually `1` in memory (print(True + True)).
# 17. Use `time.sleep` to make a countdown timer (3... 2... 1... Go!).
# 18. Write a script that imports `sys` and prints `sys.version`.
# 19. Define a variable, print it, delete it, redefine it, print it again.
# 20. Explain in a comment: What is the difference between HDD and RAM?

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. n=int(input()); print(bin(n))
2. import time; print("Loading..."); time.sleep(2); print("Done")
3. print(id("Hello"))
4. a=500; b=500; print(id(a)==id(b)) (Python reuses small ints, implies logic)
5. try: print(1/0) except: print("Crash averted")
6. start=time.time(); loop...; end=time.time()
7. os_name = input(); print(f"You are using {os_name}")
8. import sys; print(sys.getsizeof("A"*1000))
9. print("Checking CPU... OK") etc.
10. while True: break # Safety break
11. print(0b101) # Output: 5
12. secret=1; del secret; print(secret)
13. # Input: Keyboard; res = int(input()) + int(input()); # Output: Monitor; print(res)
14. print(2**100)
15. x=None; print(id(x))
16. print(True+True) # 2
17. time.sleep(1)...
18. import sys; print(sys.version)
19. x=1; print(x); del x; x=2; print(x)
20. # RAM is fast/volatile (Workbench). HDD is slow/permanent (Library).
'''
