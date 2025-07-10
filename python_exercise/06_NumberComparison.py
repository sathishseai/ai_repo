def compare_numbers(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numbers (int or float).")

        if a > b:
            print(f"{a} is greater than {b}.")
        elif a < b:
            print(f"{a} is less than {b}.")
        else:
            print(f"{a} is equal to {b}.")

    except Exception as e:
        print("Error:", e)

# Example usage:
compare_numbers(10, 5)     # 10 is greater than 5
compare_numbers(4, 9)      # 4 is less than 9
compare_numbers(7, 7)      # 7 is equal to 7
compare_numbers("x", 3)    # Error

'''
Error: All inputs must be numeric (int or float).
10 is greater than 5.
4 is less than 9.
7 is equal to 7.
Error: Both inputs must be numbers (int or float).
'''
