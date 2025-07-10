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




