# Interactive Practice Problems - Module 5 (Control Flow)
import time

def quiz():
    print("Welcome to the Module 5 Practice Quiz! (Control Flow)")
    print("Press Enter to reveal the answer to each question.")
    print("-" * 50)
    
    questions = [
        ("Ask for age. Print 'Adult' if >= 18, else 'Minor'.", 
         "if int(input()) >= 18..."),
         
        ("Loop from 1 to 100. Print only numbers divisible by 7.", 
         "for i in range(1,101): if i%7==0: print(i)"),
         
        ("Ask for a password. Keep asking until user types 'secret'.", 
         "while input() != 'secret': pass"),
         
        ("Print the multiplication table of 5 (5, 10... 50).", 
         "for i in range(1, 11): print(5*i)"),
         
        ("Calculate factorial of 5 using a for loop.", 
         "f=1; for i in range(1,6): f*=i"),
         
        ("Sum all numbers in defined list `L`.", 
         "total=0; for x in L: total+=x"),
         
        ("Find the maximum number in list `L` without using max().", 
         "m=L[0]; for x in L: if x>m: m=x"),
         
        ("Print a checkerboard pattern (3x3 grid of X and O).", 
         "nested loop (row%2, col%2)"),
         
        ("Write a calculator that asks for Num1, Op, Num2.", 
         "n1=..; op=..; n2=..; if op==..."),
         
        ("Count vowels in a user input string.", 
         "count=0; for c in s: if c in 'aeiou': count+=1"),
         
        ("Print the Fibonacci sequence up to 10 terms.", 
         "a,b=0,1; loop 10: print(a); a,b=b,a+b"),
         
        ("Check if a number is Prime.", 
         "is_prime and loop 2..n-1"),
         
        ("Reverse a number using math (not strings). 123 -> 321.", 
         "rev=0; while n>0: rev=rev*10 + n%10; n//=10"),
         
        ("Input 3 numbers and sort them using If/Else (no sort()).", 
         "nested logic or swap"),
         
        ("FizzBuzz: Print 1-20. Mul of 3->'Fizz', 5->'Buzz', Both->'FizzBuzz'.", 
         "if i%15==0.. elif i%3==0.."),
         
        ("Extract all digits from 'abc123xyz' and sum them.", 
         "sum(int(c) for c in s if c.isdigit())"),
         
        ("Guess the Number game (Logic only).", 
         "while guess != secret..."),
         
        ("Pattern Printing: Pyramid of stars.", 
         "for i in range(n): print(' '*(n-i) + '*'*(2*i+1))"),
         
        ("Validate email input (must contain @ and .).", 
         "if '@' in s and '.' in s..."),
         
        ("Count how many uppercase letters are in a string.", 
         "count=0; for c in s: if c.isupper(): count+=1")
    ]
    
    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
