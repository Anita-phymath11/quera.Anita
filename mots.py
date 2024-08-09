#The user enters a name according to the number entered,
# and the number of repeated letters in all these words is displayed
sum_of_repeated_chars=0
def get_repeated_sum(name):
    """The number of repeated letters in 
    all these words is displayed according to the number and names entered.

    Args:
        name (str): input names.

    Returns:
        int: the number of repeated letters in each name
    """
    count = 0
    freq_dict = {}

    for char in name:
        if char in freq_dict:
            freq_dict[char] += 1
        else:
            freq_dict[char] = 0
            
    for value in freq_dict.values():
        if value >= 1:
            count += value 

    return count

iri=int(input())
for i in range(1,iri+1):
    n = input()
    sum_of_repeated_chars+= get_repeated_sum(n)
print(sum_of_repeated_chars)   
# print(f"The sum of repeated characters in the name {name} is: {sum_of_repeated_chars}")
