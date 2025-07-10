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
