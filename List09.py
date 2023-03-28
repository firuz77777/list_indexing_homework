def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a1=0
    a=0
    while a<len(list1):
        if list1[a]!=list1[1]:
            a1=1
        if a1==1:
            w=True
        else:
            w=False
        a+=1
    return w 
print(main([1,1,1,1,1,1,1]))