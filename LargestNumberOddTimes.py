def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    # Your code here
    dict = {}
    
    for i in L:
        total = dict.get(i, 0)         
        dict[i] = total + 1
    
    for j in sorted(dict.keys(), reverse=True):
        if( dict[j] % 2 == 0):
            continue;
        return j;
    
    return "None"
    
L = [3, 5, 9, 9, 11, 11, 3,5]
print(largest_odd_times(L))
        