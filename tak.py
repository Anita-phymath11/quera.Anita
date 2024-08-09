#It takes a number from the user and shows the sum of its digits,
# but if the sum of the digits does not reach a
# single digit, it adds the digits until 
# they become a single digit.
#...................................................
# Function to calculate the sum of digits
def calculate_sum_of_digits(number):
    """It takes a number from the user and shows the sum of its digits
       and it adds the digits until they become a single digit.

    Args:
        number (int): A number whose digits are added together.
    Returns:
        int: sum of digits
    """
    # Convert the number to a string
    digits = str(number)
    sum_of_digits = 0
    for digit in digits:
        sum_of_digits += int(digit)
    return sum_of_digits

# Ask the user to input a number
n = int(input())
result=10
# Call the function and print the result
while result>9:
    result = calculate_sum_of_digits(n)
    # print ("res1 ",result)
    n=result
    
print(result)