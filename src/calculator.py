# function to calculate sum from the given string
def add(numbers: str) -> int:
    # If the input string is empty, return 0
    if not numbers:
        return 0

    # Check if the input string contains a custom delimiter
    if numbers.startswith("//"):
        # Find the index of the first newline character
        delimiter_index = numbers.find("\n")
        if delimiter_index == -1:
            raise ValueError("string not properly formatted.")

        # Extract the delimiter from the line following "//"
        delimiter = numbers[2:delimiter_index]
        # Extract the numbers part from the string
        numbers = numbers[delimiter_index + 1 :]
        # check string numberpart properly formatted/contains delimeter
        if numbers.find(delimiter) == -1:
            return 0
    else:
        # Default delimiter is comma
        delimiter = ","

    # Replace the custom delimiter with commas
    numbers = numbers.replace("\n", delimiter)
    num_list = numbers.split(delimiter)

    # Convert the list of strings to a list of integers
    try:
        int_list = [int(num.strip()) for num in num_list if num.strip()]
    except ValueError:
        raise ValueError("The input string contains non-numeric values.")

    # Return the sum of the integers
    return sum(int_list)
