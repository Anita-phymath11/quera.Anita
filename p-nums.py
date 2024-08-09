#It receives two numbers such as A and B
       #from the input and prints the prime numbers 
       #between these two numbers 
       #(including the two numbers) in the output.
def prime(a):
    """It receives two numbers such as A and B
       from the input and prints the prime numbers 
       between these two numbers 
       (including the two numbers) in the output.

    Args:
        a (int): the input and our range.

    Returns:
        int: the prime number
    """
    k=0
    for b in range(2,a):
        if a%b==0:#a is devidable to b so it is not a prime number
            k=1
            break            
    return k

a=int(input())
b=int(input())

for i in range (a,b+1):
    # print ("i ",i)
    m=prime (i)
    if m==0:
        print (i)
















































