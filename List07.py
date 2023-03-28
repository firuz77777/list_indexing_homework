def main(list1):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    a=0
    q=[]
    while a<len(list1):
        if list1[a] == 0:
            q+=[False]
        else:
            q+=[1]     
        a+=1  
    return q
print(main([1,0,1,1,1,0,0]))