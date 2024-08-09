#This program takes a number between 1 and 6 and print the opposite number on the dice.
dice_list=[[1,6],[2,5],[3,4]] 

def getDice(s):
    """Takes a number between 1 and 6 and
    shows the opposite number on the dice.

    Args:
        s (int): The number which the user enters.

    Returns:
        int: The opposite of input.
    """
    for i in range(len(dice_list)):
        if dice_list[i][0]==s:
            return dice_list[i][1]
        elif dice_list[i][1]==s:
            return dice_list[i][0]
# while 1:        
n=int(input( ))
# if n<1 or n>6:
#     print("invalid input! ")
    # continue
m=getDice(n)
print(m)