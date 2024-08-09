#It takes an integer and a positive number 
# from the user and prints a solid rhombus with a diameter of 2n+1
def draw_rhombus(num):
    """
    Prints a solid rhombus with a diameter of 2n+1 with the input numbers.

    Args:
        num (int): The input number which we use to make a solid rhombus.
    """
    for i in range(1, num+2):
        print(" " * (num-i+1) + "*" * (2*i-1))
        
    for i in range(num, 0, -1):
        print(" " * (num-i+1) + "*" * (2*i-1))

num = int(input())
draw_rhombus(num)