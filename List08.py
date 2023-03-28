def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
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
            q+=[True]     
        a+=1  
    return q
print(main([1,0,1,1,1,0,0]))