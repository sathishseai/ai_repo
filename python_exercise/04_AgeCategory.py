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
