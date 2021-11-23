# list_integer = [10, 14, 5, 3, 12, 11 ]

def sum_list(List_integer) :

    sigma = 0

    index = 0
    while index < len(list_integer):
        sigma += list_integer[index]
        index += 1

    return sigma


#nombre paire et impaire 
def sum_odd_even_list(list_integer):
    sigma_even = 0
    sigma_odd = 0

    index = 0
    while index < len(list_integer):
        if list_integer[index] % 2 == 0 :
            sigma_even += list_integer[index]
        else :
            sigma_odd += list_integer[index]
        index += 1

    return sigma_even, sigma_odd;

def min_max_list(list_value):
    min_value = list_value[0]
    max_value = list_value[0]

    index = 1
    while index < len(list_integer):

        if list_value[index] > max_value:
            max_value = list_value[index]

        elif list_value[index] < min_value:
            min_value = list_value[index]

        index +=1

    return min_value, max_value;



#determiner le plus grand ecart positif entre les deux nombres qui se suivent dans la liste
def max_step_in_list(list_value):
    # ecart indice 1 et indice 0 on initialise

    max_step = list_value[1] - list_value[0]
    previous_value = list_value[1]

    index = 2
    while index < len(list_value):

        step = list_value[index] - previous_value

        if step > max_step:
            max_step = step

        previous_value = list_value[index]

        index += 1

    return max_step





#pour renverser la liste
#  reverse_list(15, 7, 8,  12, 9, 4, 11)
def reverse_list(list_value) :
    index_inf = 0
    index_sup = len(list_value) - 1

    while index_sup > index_inf:

        tmp = list_value[index_inf]
        list_value[index_inf] = list_value[index_sup]
        list_value[index_sup] = tmp

        index_inf += 1
        index_sup -= 1
    print(list_value)
    return list_value

#pour appeler la fonction 
#reverse_list([15, 7, 8,  12, 9, 4, 11])




#exercice pour du chaud/froid 
import random 

max_random = 1000
mysterious_nb = random.randint(1, max_random)

print(mysterious_nb)

#on initie une valeur fausse
is_found = False
guess_counter = 0 

while not is_found: 
    guess = int(input("N=?"))
    guess_counter += 1

    if guess > mysterious_nb:
        print("Too big boi")
    elif guess < mysterious_nb:
        print("Trop petit")
    else: 
        is_found = True 

print("Trouver en:", guess_counter, "coups")


# def ToBitReversedIndex(Natural, Range):
#     if Range < 4
#         return Natural 

#     Reversed = Natural & 1
#     Natural >>= 1
#     Range >>= 1 
#     whilde Range != 2:
#         Reversed <<= 1 
#         Reversed += Natural & 1 
#         Natural >>= 1 
#         Range >>= 1

#     Reversed <<= 1
#     Reversed += Natural & 1






# trouver une liste parmi une liste et retourner son index quand elle est identique 
list_among_list = [12, 47, 125, 32, 10, 15, 11]
small_list = [32, 10, 15]

def search_sub_list(source, target):
    len_source = len(source)
    len_tartget = len(target)

    index_source = 0
    # on parcours tout le tableau 
    while index_source <= (len_source - len_target):

        index_target = 0 
        index_test = index_source

        # des qu'on trouve le bon on s'arrete 
        while target[index_target] == source[index_test] and target[index_target] < source[index_test]:
            index_target += 1
            index_test += 1
        
        if index_target == len_target:
            return index_source

        index_source += 1

    # au cas ou le resultat n'est pas trouvé on retourne -1
    return -1 

search_sub_list([15, 7, 8,  12, 9, 4, 11],[32, 10, 15])








#filtre de nombre premiers 
def SievePrimeNumber(SieveLimit):
    # Sieve of Eratosthene itself 

    is PrimeList = [True] * (SieveLimit + 1)

    IndexNumberToTest = 2
    while IndexNumberToTest ** 2 <= SieveLimit:
        if IsPrimeList[IndexNumerToTest]:
            IndexMultipleToMark = 2 * IndexNumberToTest 
            while IndexMultipleToMark <= SieveLimit:
                IsPrimeList[IndexMultipleToMark] = False
                IndexMultipleToMark += IndexNumberToTest 

        IndexNumberToTest += 1
    # TRansformation of the IsPrimeList in a list of prime number 

    PrimeNumberList = []
    IndexNumberToTest = 2
    while IndexNumberToTest <= SieveLimit:
        if IsPrimeList[IndexNumberToTest]:
            PrimeNumberList.append(IndexNumberToTest)
            IndexNumberToTest += 1

    return PrimeNumberList

    print(SievePrimeNumber(100)) 


