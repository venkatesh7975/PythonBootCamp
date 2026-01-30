# ==========================================
# MODULE 4: PRACTICE PROBLEMS
# ==========================================
# 1. Ask user for their name and print it in ALL CAPS.
# 2. Check if the string "apple" contains the letter "e".
# 3. Reverse the user's input string.
# 4. Count how many distinct words are in "The quick brown fox jumps".
# 5. Extract "World" from "Hello World" using slicing.
# 6. Replace spaces with underscores in "File Name With Spaces".
# 7. Check if a string starts with "Py" (startswith method).
# 8. Check if a user input is purely numbers (isnumeric method).
# 9. Format a string print: "Item: [item], Price: $[price]".
# 10. Split "192.168.1.1" by dot.
# 11. Remove leading zeros from "000123".
# 12. Create a palindrome check (is "racecar" == reversed "racecar"?).
# 13. Given s="abcdef", print every 2nd character.
# 14. Capitalize only the first letter of "python" (capitalize method).
# 15. Check if "  " is just whitespace (isspace).
# 16. Find the position of the second "o" in "Google".
# 17. Print a string 5 times using multiplication ("Na" * 5).
# 18. Escape a single quote inside a single quoted string.
# 19. Join ["A", "B", "C"] with "->".
# 20. Slice out the *last* 3 characters of any input string.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. print(input().upper())
2. print("e" in "apple")
3. s=input(); print(s[::-1])
4. s="The quick..."; print(len(s.split()))
5. s="Hello World"; print(s[6:])
6. print("...".replace(" ", "_"))
7. print(s.startswith("Py"))
8. print(s.isnumeric())
9. print(f"Item: {item}, Price: ${price}")
10. print("192.168.1.1".split("."))
11. print("000123".lstrip("0"))
12. s="racecar"; print(s == s[::-1])
13. print(s[::2])
14. print("python".capitalize())
15. print("  ".isspace())
16. s="Google"; first=s.find("o"); print(s.find("o", first+1))
17. print("Na"*5)
18. print('It\'s me')
19. print("->".join(L))
20. print(s[-3:])
'''
