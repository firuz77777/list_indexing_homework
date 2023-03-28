def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    a = list_num[1:-1]
    q=0
    max=a[0]
    while q<len(a):
        if max<a[q]:
            max=a[q]
        q+=1
    return max
print(main([1,2,3,4,5,6,7]))