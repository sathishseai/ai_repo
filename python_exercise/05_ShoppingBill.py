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
