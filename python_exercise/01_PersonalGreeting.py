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





