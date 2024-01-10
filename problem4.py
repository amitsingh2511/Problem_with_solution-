'''
Handling Corner Cases. If a function specifies a precondition (e.g., “given a list of integers”), 
you can assume that this precondition will be satisfied (e.g., you do not need to check if the elements 
in the list are integers). However, you will still want to check valid corner-cases (e.g., an empty 
list of integers). 
'''

def calculate_average(numbers):
    """
    Calculate the average of a list of integers.

    Args:
    - numbers (list of int): List of integers.

    Returns:
    - float: Average of the integers in the list.
    """
    # Check if the list is empty
    if not numbers:
        return 0.0  # Return 0 if the list is empty

    # Calculate the average
    average = sum(numbers) / len(numbers)
    return average

# Example usage
numbers_list = [1, 2, 3, 4, 5]
result = calculate_average(numbers_list)
print(result)

# Output 3.0
# Corner case: Empty list
empty_list_result = calculate_average([])
print(empty_list_result)

# Output 0.0

