"""
04_exception_handling.py - Master Exception Handling

Learn how to gracefully handle errors using try, except, else, and finally.
"""

def divide_numbers(a, b):
    print(f"Attempting: {a} / {b}")
    try:
        # Code that might raise an error
        result = a / b
    except ZeroDivisionError:
        # Handle specific error
        print("Error: You cannot divide by zero!")
    except TypeError as e:
        # Handle another specific error
        print(f"Error: Invalid input types! ({e})")
    except Exception as e:
        # Catch-all for any other errors
        print(f"An unexpected error occurred: {e}")
    else:
        # Runs ONLY if no exception was raised
        print(f"Success! The result is: {result}")
    finally:
        # Runs ALWAYS (useful for cleanup like closing files)
        print("Cleanup: Operation attempt finished.\n")

# Testing the function
divide_numbers(10, 2)   # Success case
divide_numbers(10, 0)   # ZeroDivisionError
divide_numbers(10, "2") # TypeError

# Raising a custom exception
print("--- Custom Exception ---")
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    print(f"Age {age} is valid.")

try:
    check_age(-5)
except ValueError as e:
    print(f"Caught custom error: {e}")

print("\n--- Exception Handling Demo Complete ---")
