# additionner le tableau [10, 14, 5, 3, 12, 11]

def sum_list(list_integer):
    #ce qu'on veut retourner, on doit dabord l'initialiser a 0
    sum_list = 0

    #on le fait grace a son index
    index = 0 
    #parcours tout les index jusqu'a atteindre le nombre de list integer 
    while index < len(list_integer):
        #additionne selon la liste et lindex pointe
        sum_list += list_integer[index]
        #pour parcourir tout les index 
        index += 1

    return sum_list


# retourner les nombres paires et impaires 
    sum_odd = 0
    sum_even = 0 

    index = 0 
    while index < len(list_integer):
        if list_integer[index] % 2 == 0 : 
            sum_even += list_integer[index]
        else :
            sum_odd += list_integer[index]
        index += 1

    return sum_even, sum_odd 

# additionner le tableau [10, 14, 5, 3, 12, 11]
def sum_list(list_integer):
    sum_list = 0

    index = 0
    while index < len(list_integer)
        sum_list += list_integer[index] 
        index += 1
    return sum_list(list_integer)

#donner min max
def min_max_list(list_value):
    min_list = 0
    max_list = 0

    index = 0
    while index < len(list_integer)