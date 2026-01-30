# Interactive Practice Problems - Module 6 (Data Structures)
import time

def quiz():
    print("Welcome to the Module 6 Practice Quiz! (Data Structures)")
    print("Press Enter to reveal the answer to each question.")
    print("-" * 50)
    
    questions = [
        ("Create a list of 5 favorite movies. Print the 3rd one.", 
         "movies=['A','B','C','D','E']; print(movies[2])"),
         
        ("Add a new movie to the end of the list.", 
         "movies.append('F')"),
         
        ("Remove the first movie by name.", 
         "movies.remove('A')"),
         
        ("Sort the list alphabetically.", 
         "movies.sort()"),
         
        ("Create a Tuple representing a coordinate (x, y, z).", 
         "t=(10, 20, 30)"),
         
        ("Unpack the tuple into variables x, y, z.", 
         "x,y,z=t"),
         
        ("Create a Set of colors 'Red', 'Blue', 'Red'. Print it (Duplicates?).", 
         "s={'Red','Blue','Red'}; print(s) (One Red)"),
         
        ("Check if 'Green' is in the color set.", 
         "print('Green' in s)"),
         
        ("Create a Dictionary representing a 'Book' (Title, Author, Year).", 
         "book={'Title':'X', 'Author':'Y', 'Year':2000}"),
         
        ("Change the Year of the book.", 
         "book['Year']=2024"),
         
        ("Add a new key 'Genre' to the book dict.", 
         "book['Genre']='Fiction'"),
         
        ("Write a loop to print all Keys and Values of the book dict.", 
         "for k,v in book.items(): print(k, v)"),
         
        ("Create a list of numbers 1-10. Use slicing to get the first 5.", 
         "L=list(range(1,11)); print(L[:5])"),
         
        ("Use List Comprehension to create a list of even numbers 0-20.", 
         "[x for x in range(21) if x%2==0]"),
         
        ("Given L=[10, 20, 30], use pop() to remove and print the last item.", 
         "print(L.pop())"),
         
        ("Combine two sets: A={1,2} and B={2,3} (Union).", 
         "print(A | B)"),
         
        ("Find the difference: A={1,2} - B={2,3}.", 
         "print(A - B)"),
         
        ("Count how many times the number 5 appears in tuple T=(1,5,5,5,2).", 
         "print(T.count(5))"),
         
        ("Start with an empty list. Use a loop to add numbers 1 to 5.", 
         "L=[]; for i in range(1,6): L.append(i)"),
         
        ("Count frequency of words in string 'to be or not to be' using a Dict.", 
         "s='to be...'; d={}; for w in s.split(): d[w]=d.get(w,0)+1")
    ]
    
    for i, (q, a) in enumerate(questions, 1):
        print(f"\\nQ{i}: {q}")
        input("   Your Answer: ")
        print(f"👉 Solution: {a}")
        print("-" * 50)

if __name__ == "__main__":
    quiz()
