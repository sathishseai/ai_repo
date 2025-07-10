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
