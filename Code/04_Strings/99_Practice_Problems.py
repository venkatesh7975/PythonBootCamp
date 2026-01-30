# Interactive Practice Problems - Module 4 (Strings)
import time

def quiz():
    print("Welcome to the Module 4 Practice Quiz! (Strings)")
    print("Press Enter to reveal the answer to each question.")
    print("-" * 50)
    
    questions = [
        ("Ask user for their name and print it in ALL CAPS.", 
         "print(input().upper())"),
         
        ("Check if the string 'apple' contains the letter 'e'.", 
         "print('e' in 'apple')"),
         
        ("Reverse the user's input string.", 
         "s=input(); print(s[::-1])"),
         
        ("Count how many distinct words are in 'The quick brown fox jumps'.", 
         "s='The quick...'; print(len(s.split()))"),
         
        ("Extract 'World' from 'Hello World' using slicing.", 
         "s='Hello World'; print(s[6:])"),
         
        ("Replace spaces with underscores in 'File Name With Spaces'.", 
         "print('...'.replace(' ', '_'))"),
         
        ("Check if a string starts with 'Py' (startswith method).", 
         "print(s.startswith('Py'))"),
         
        ("Check if a user input is purely numbers (isnumeric method).", 
         "print(s.isnumeric())"),
         
        ("Format a string print: 'Item: [item], Price: $[price]'.", 
         "print(f'Item: {item}, Price: ${price}')"),
         
        ("Split '192.168.1.1' by dot.", 
         "print('192.168.1.1'.split('.'))"),
         
        ("Remove leading zeros from '000123'.", 
         "print('000123'.lstrip('0'))"),
         
        ("Create a palindrome check (is 'racecar' == reversed 'racecar'?).", 
         "s='racecar'; print(s == s[::-1])"),
         
        ("Given s='abcdef', print every 2nd character.", 
         "print(s[::2])"),
         
        ("Capitalize only the first letter of 'python' (capitalize method).", 
         "print('python'.capitalize())"),
         
        ("Check if '  ' is just whitespace (isspace).", 
         "print('  '.isspace())"),
         
        ("Find the position of the second 'o' in 'Google'.", 
         "s='Google'; first=s.find('o'); print(s.find('o', first+1))"),
         
        ("Print a string 5 times using multiplication ('Na' * 5).", 
         "print('Na'*5)"),
         
        ("Escape a single quote inside a single quoted string.", 
         "print('It\\'s me')"),
         
        ("Join ['A', 'B', 'C'] with '->'.", 
         "print('->'.join(L))"),
         
        ("Slice out the *last* 3 characters of any input string.", 
         "print(s[-3:])")
    ]
    
    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
