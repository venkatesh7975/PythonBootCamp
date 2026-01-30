# ==========================================
# MODULE 6: PRACTICE PROBLEMS
# ==========================================
# 1. Create a list of 5 favorite movies. Print the 3rd one.
# 2. Add a new movie to the end of the list.
# 3. Remove the first movie by name.
# 4. Sort the list alphabetically.
# 5. Create a Tuple representing a coordinate (x, y, z).
# 6. Unpack the tuple into variables x, y, z.
# 7. Create a Set of colors "Red", "Blue", "Red". Print it (Duplicates?).
# 8. Check if "Green" is in the color set.
# 9. Create a Dictionary representing a "Book" (Title, Author, Year).
# 10. Change the Year of the book.
# 11. Add a new key "Genre" to the book dict.
# 12. Write a loop to print all Keys and Values of the book dict.
# 13. Create a list of numbers 1-10. Use slicing to get the first 5.
# 14. Use List Comprehension to create a list of even numbers 0-20.
# 15. Given L=[10, 20, 30], use pop() to remove and print the last item.
# 16. Combine two sets: A={1,2} and B={2,3} (Union).
# 17. Find the difference: A={1,2} - B={2,3}.
# 18. Count how many times the number 5 appears in tuple T=(1,5,5,5,2).
# 19. Start with an empty list. Use a loop to add numbers 1 to 5.
# 20. Count frequency of words in string "to be or not to be" using a Dict.

# ==========================================
# SOLUTIONS
# ==========================================
'''
1. movies=["A","B","C","D","E"]; print(movies[2])
2. movies.append("F")
3. movies.remove("A")
4. movies.sort()
5. t=(10, 20, 30)
6. x,y,z=t
7. s={"Red","Blue","Red"}; print(s) (One Red)
8. print("Green" in s)
9. book={"Title":"X", "Author":"Y", "Year":2000}
10. book["Year"]=2024
11. book["Genre"]="Fiction"
12. for k,v in book.items(): print(k, v)
13. L=list(range(1,11)); print(L[:5])
14. [x for x in range(21) if x%2==0]
15. print(L.pop())
16. print(A | B)
17. print(A - B)
18. print(T.count(5))
19. L=[]; for i in range(1,6): L.append(i)
20. s="to be..."; d={}; for w in s.split(): d[w]=d.get(w,0)+1
'''
