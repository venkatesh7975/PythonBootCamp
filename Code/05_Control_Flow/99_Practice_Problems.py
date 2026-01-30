# ==========================================
# MODULE 5: PRACTICE PROBLEMS
# ==========================================
# 1. Ask for age. Print "Adult" if >= 18, else "Minor".
# 2. Loop from 1 to 100. Print only numbers divisible by 7.
# 3. Ask for a password. Keep asking until user types "secret".
# 4. Print the multiplication table of 5 (5, 10... 50).
# 5. Calculate factorial of 5 using a for loop.
# 6. Sum all numbers in defined list `L`.
# 7. Find the maximum number in list `L` without using max().
# 8. Print a checkerboard pattern (3x3 grid of X and O).
# 9. Write a calculator that asks for Num1, Op, Num2.
# 10. Count vowels in a user input string.
# 11. Print the Fibonacci sequence up to 10 terms.
# 12. Check if a number is Prime.
# 13. Reverse a number using math (not strings). 123 -> 321.
# 14. Input 3 numbers and sort them using If/Else (no sort()).
# 15. FizzBuzz: Print 1-20. Mul of 3->"Fizz", 5->"Buzz", Both->"FizzBuzz".
# 16. Extract all digits from "abc123xyz" and sum them.
# 17. Guess the Number game (Logic only).
# 18. Pattern Printing: Pyramid of stars.
# 19. Validate email input (must contain @ and .).
# 20. Count how many uppercase letters are in a string.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. if int(input()) >= 18...
2. for i in range(1,101): if i%7==0: print(i)
3. while input() != "secret": pass
4. for i in range(1, 11): print(5*i)
5. f=1; for i in range(1,6): f*=i
6. total=0; for x in L: total+=x
7. m=L[0]; for x in L: if x>m: m=x
8. nested loop (row%2, col%2)
9. n1=..; op=..; n2=..; if op==...
10. count=0; for c in s: if c in "aeiou": count+=1
11. a,b=0,1; loop 10: print(a); a,b=b,a+b
12. is_prime and loop 2..n-1
13. rev=0; while n>0: rev=rev*10 + n%10; n//=10
14. nested logic or swap
15. if i%15==0.. elif i%3==0..
16. sum(int(c) for c in s if c.isdigit())
17. while guess != secret...
18. for i in range(n): print(" "*(n-i) + "*"*(2*i+1))
19. if "@" in s and "." in s...
20. count=0; for c in s: if c.isupper(): count+=1
'''
