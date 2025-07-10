def check_even_or_odd(number):
    try:
        if not isinstance(number, int):
            raise TypeError("Input must be an integer.")

        if number % 2 == 0:
            print(f"{number} is Even.")
        else:
            print(f"{number} is Odd.")

    except Exception as e:
        print("Error:", e)

def check_list_even_or_odd(numbers):
    try:
        for num in numbers:
            if not isinstance(num, int):
                raise ValueError(f"Invalid item in list: {num} (not an integer)")
            check_even_or_odd(num)
    except Exception as e:
        print("Error while processing the list:", e)

# Example usage:
check_even_or_odd(7)                  # Odd
check_even_or_odd(10)                 # Even
check_even_or_odd("five")            # Error

check_list_even_or_odd([2, 5, 0, 13]) # Mixed
check_list_even_or_odd([1, "x", 4])   # Error in list

'''
7 is Odd.
10 is Even.
Error: Input must be an integer.
2 is Even.
5 is Odd.
0 is Even.
13 is Odd.
1 is Odd.
Error while processing the list: Invalid item in list: x (not an integer)
'''




