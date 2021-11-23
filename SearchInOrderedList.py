# principe de la dichotomie en découpant les choses par 2 puis par 2 

# vraie correction
def search_in_ordered_list(source, target):
    index_inf = 0 
    index_sup = len(source) - 1

    while index_inf <= index_sup:
        index_test = (index_sup + index_inf) // 2

        if source[index_test] == target:
            return index_test
        elif source[index_test] > target:
            index_sup = index_test - 1
        else:
            index_inf = index_test + 1
    return -1 


# trouver sur internet 
find_num = 15
def binary_search(find_num,l):
    #  View the number of calls to the list
    print(l)
    #  For list index value out of range: IndexError: list index out of range
    if len(l) == 0:
        print("The value found does not exist! !")
        return
    mid_index = len(l) // 2  #  Get the index of the middle value of the list
    if find_num > l[mid_index]:
        l = l[mid_index + 1:]  #  The list is sliced ​​from the middle index plus 1 to the end of the list.
        binary_search(find_num,l)
    elif find_num < l[mid_index]:
        l = l[:mid_index]  #  The list is sliced ​​from the head of the list to the middle index.
        binary_search(find_num,l)
    else:
        print('find it')
binary_search(find_num,nums)

 print(search_in_ordered_list([2, 5, 7, 9, 14, 32, 33, 35, 40, 50, 60, 70, 80, 200, 400], 35))







MyOrderedList = [2, 5, 7, 9, 14, 32, 33, 35, 40, 50, 60, 70, 80, 200, 400]
MyTarget = 0 

IndexMyTarget = search_in_ordered_list



def search_in_ordered_list(find_num, 1): 

    find_num = 35
    mid_index = len(1) // 2  # l'index du milieu de la liste
    
    #mid_val = Find the middle value of the list




    print(search_in_ordered_list([2, 5, 7, 9, 14, 32, 33, 35, 40, 50, 60, 70, 80, 200, 400], 35))