def personal_greeting():
    try:
        name = input("Enter your name: ").strip()
        age_input = input("Enter your age: ").strip()
        color = input("Enter your favorite color: ").strip()

        # Validate name and color
        if not name or not color:
            raise ValueError("Name and favorite color cannot be empty.")

        # Validate and convert age
           
        age = int(age_input)
        if age < 0:
            raise ValueError("Age cannot be negative.")

        print(f"\nHello {name}! You are {age} years old and love the color {color}. That's awesome!")

    except ValueError as ve:
        print("Value Error:", ve)
    except Exception as e:
        print("An unexpected error occurred:", e)

# Run the function
personal_greeting()

'''
Enter your name: Sathish
Enter your age: 52
Enter your favorite color: Black
Value Error: Age must be numeric
'''
#--------------------------------------------------------------------------------------------------------#

def basic_calculator(a, b, operator):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both inputs must be numbers (int or float).")

        if operator == '+':
            result = a + b
        elif operator == '-':
            result = a - b
        elif operator == '*':
            result = a * b
        elif operator == '/':
            if b == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            result = a / b
        else:
            raise ValueError(f"Unsupported operator: '{operator}'")

        print(f"{a} {operator} {b} = {result}")

    except Exception as e:
        print("Error:", e)

# Example usage:
basic_calculator(10, 5, '+')    # 10 + 5 = 15
basic_calculator(10, 0, '/')    # Error: divide by zero
basic_calculator(8, 2, '*')     # 8 * 2 = 16
basic_calculator("a", 3, '-')   # Error: invalid type
basic_calculator(4, 2, '^')     # Error: unsupported operator

'''
10 + 5 = 15
Error: Cannot divide by zero.
8 * 2 = 16
Error: Both inputs must be numbers (int or float).
Error: Unsupported operator: '^'
'''
#--------------------------------------------------------------------------------------------------------#

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
#--------------------------------------------------------------------------------------------------------#

def determine_age_category(age):
    try:
        if not isinstance(age, (int, float)):
            raise TypeError("Age must be a number.")
        if age < 0:
            raise ValueError("Age cannot be negative.")

        if age <= 12:
            category = "Child"
        elif 13 <= age <= 19:
            category = "Teenager"
        elif 20 <= age <= 59:
            category = "Adult"
        else:
            category = "Senior"

        print(f"Age {age} falls under: {category}")

    except Exception as e:
        print("Error:", e)

# Example usage:
determine_age_category(8)      # Child
determine_age_category(16)     # Teenager
determine_age_category(35)     # Adult
determine_age_category(70)     # Senior
determine_age_category("ten")  # Error

'''
Age 8 falls under: Child
Age 16 falls under: Teenager
Age 35 falls under: Adult
Age 70 falls under: Senior
Error: Age must be a number.
'''
#--------------------------------------------------------------------------------------------------------#

def calculate_total(item1, item2, item3, tax_percent):
    try:
        # Validate inputs
        for value in [item1, item2, item3, tax_percent]:
            if not isinstance(value, (int, float)):
                raise TypeError("All inputs must be numeric (int or float).")

        subtotal = item1 + item2 + item3
        tax_amount = (tax_percent / 100) * subtotal
        total = subtotal + tax_amount

        print(f"Subtotal: ₹{subtotal:.2f}")
        print(f"Tax (@{tax_percent}%): ₹{tax_amount:.2f}")
        print(f"Total Bill: ₹{total:.2f}")

    except Exception as e:
        print("Error:", e)

# Example usage:
calculate_total(150.50, 99.99, 200, 18)   # Normal case
calculate_total(100, "a", 50, 5)          # Error case

'''
Subtotal: ₹450.49
Tax (@18%): ₹81.09
Total Bill: ₹531.58
'''
#--------------------------------------------------------------------------------------------------------#

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
#--------------------------------------------------------------------------------------------------------#

def check_password(password, min_length=8):
    try:
        if not isinstance(password, str):
            raise TypeError("Password must be a string.")

        if len(password) < min_length:
            raise ValueError(f"Password too short. Minimum length is {min_length} characters.")

        print("Password is valid.")

    except Exception as e:
        print("Error:", e)

# Example usage:
check_password("mypwd")          # Too short
check_password(12345678)         # Invalid type
check_password("strongPass123")  # Valid

'''Error: Password too short. Minimum length is 8 characters.
Error: Password must be a string.
Password is valid.'''

#--------------------------------------------------------------------------------------------------------#

def count_numbers(number_list):
    try:
        positive_count = 0
        negative_count = 0
        zero_count = 0

        for num in number_list:
            if not isinstance(num, (int, float)):
                raise ValueError(f"Invalid item in list: {num}")
            if num > 0:
                positive_count += 1
            elif num < 0:
                negative_count += 1
            else:
                zero_count += 1

        print("Positive numbers:", positive_count)
        print("Negative numbers:", negative_count)
        print("Zeroes:", zero_count)

    except Exception as e:
        print("An error occurred:", e)

# Example usage:
numbers = [3, -1, 0, 5, -7, 0, 2, 'a']  # 'a' will trigger the exception
count_numbers(numbers) # An error occurred: Invalid item in list: a
#--------------------------------------------------------------------------------------------------------#








