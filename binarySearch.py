def binary_search(list, item):
    low = 0
    high = len(list) - 1
    
    while low <= high: 
        quite = (low + high) // 2
        kick = list[quite]
        if kick == item:
            return quite
        if kick > item:
            high = quite - 1
        else:
            low = quite + 1
    return None 

my_list = [1, 3, 5, 7, 9]

print(binary_search(my_list, 3))  # Uso correto de print em Python 3
print(binary_search(my_list, -1))

    
    