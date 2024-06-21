def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high: 
        quite = (low + high) / 2
        kick = list[quite]
        if kick == item:
            return quite
        if kick > item:
            high = quite - 1
        else:
            low = quite + 1
    return None 

my_list = [1, 3, 5, 7, 9]




    
    