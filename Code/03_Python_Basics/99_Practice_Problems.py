# Interactive Quiz - Module 3
import time

def quiz():
    print("Welcome to the Module 3 Quiz! (Press Enter to reveal answers)")
    print("-" * 50)
    
    questions = [
        ("Create a variable `age` and assign 21. Print it.", 
         "age=21; print(age)"),
         
        ("Swap `x=1` and `y=2` without a temp variable.", 
         "x,y=y,x"),
         
        ("Calculate the area of a rectangle (l=10, w=5).", 
         "print(10*5)"),
         
        ("Check if 7 is even/odd using modulus.", 
         "print('Even' if 7%2==0 else 'Odd')"),
         
        ("Check if `age` (15) is between 13 and 19 (Teenager).", 
         "age=15; print(13 <= age <= 19)"),
         
        ("Calculate Average of 3 numbers: 10, 20, 30.", 
         "print((10+20+30)/3)"),
         
        ("Convert 98.6 Fahrenheit to Celsius (C = (F-32) * 5/9).", 
         "print((98.6-32) * 5/9)"),
         
        ("Define `a=10`. Add 5 to it using `+=`.", 
         "a=10; a+=5"),
         
        ("Check if 'apple' and 'Apple' are equal (Equality).", 
         "print('apple'=='Apple') # False"),
         
        ("Find the remainder of 100 divided by 7.", 
         "print(100%7)"),
         
        ("Calculate 2 to the power of 10.", 
         "print(2**10)"),
         
        ("Create a variable name with multiple words using Snake Case.", 
         "my_variable_name = 1"),
         
        ("Assign 10 to a, b, and c in one line.", 
         "a=b=c=10"),
         
        ("What is the type of `result = 10 / 2`? Print logic.", 
         "Type is float. print(type(10/2))"),
         
        ("Use `and` to check if 10 is positive AND even.", 
         "val=10; print(val>0 and val%2==0)"),
         
        ("Use `not` to check if variable `is_raining` (False) is NOT raining.", 
         "is_raining=False; print(not is_raining)"),
         
        ("Floor divide 15 by 4.", 
         "print(15//4)"),
         
        ("Create a complex logical statement that evaluates to False.", 
         "print(True and False)"),
         
        ("Check if ' ' (Space) is Truthy.", 
         "print(bool(' ')) # True"),
         
        ("Calculate the hypotenuse of right triangle with sides 3 and 4 ((a^2 + b^2)^0.5).", 
         "print((3**2 + 4**2)**0.5) # 5.0")
    ]

    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        user_input = input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
