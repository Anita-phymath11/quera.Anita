#It receives three positive integers as input
# from the user and prints YES if it is possible to construct a
# right triangle with the length of the given sides and NO otherwise.
def isFisa(x,y,z):
    """ Gets 3 inputs prints YES if it is possible to construct a
       right triangle with the length of the given sides and NO otherwise.

    Args:
        x (int): input
        y (int): input
        z (int): input

    Returns:
        str: If it is possible to construct a right triangle which 3 inputs.
    """
    ret="NO"    
    if x**2+y**2==z**2 or z**2+y**2==x**2 or z**2+x**2==y**2:
        ret="YES"
    
    return ret

a=int(input())
b=int(input())
c=int(input())

print(isFisa(a,b,c))