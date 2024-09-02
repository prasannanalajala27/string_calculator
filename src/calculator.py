# function to calculate sum from the given string
def add(numbers: str) -> int:
    # If the input string is empty, return 0
    if not numbers:
        return 0

    # Replace newlines with commas and then split the string by commas
    numbers = numbers.replace("\n", ",")
    num_list = numbers.split(",")

    # Convert the list of strings to a list of integers
    try:
        int_list = [int(num.strip()) for num in num_list if num.strip()]
    except ValueError:
        raise ValueError("The input string contains non-numeric values.")

    # Return the sum of the integers
    return sum(int_list)
