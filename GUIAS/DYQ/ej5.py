# Implementar Merge Sort. Justificar el orden del algoritmo mediante el teorema maestro.

def merge_sort(my_list):
	# Base Case
    if len(my_list) <= 1:
        return my_list
   
    list_1 = my_list[0:len(my_list) / 2]
    list_2 = my_list[len(my_list) / 2:]
    
   	# Induction Step
    ans_1 = merge_sort(list_1)
    ans_2 = merge_sort(list_2)
    
    # Sorting and merging two sorted list
    sort_list = sort_two_list(ans_1, ans_2)
    return sort_list

# Separate Function to sort and merge 2 sorted lists
def sort_two_list(list_1, list_2):
    final_list = []
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            final_list.append(list_1[i])
            i += 1
            continue
        final_list.append(list_2[j])
        j += 1

    while i < len(list_1):
        final_list.append(list_1[i])
        i = i + 1
        
    while j < len(list_2):
        final_list.append(list_2[j])
        j = j + 1
        
    return final_list

# Resuelvo con teorema maestro...

# T(n) = AT(n/B) + O(n^C)

# A = 2 (llamo 2 veces recursivamente)
# B = 2 (parto el arreglo en 2)
# C = 1 (costo  de partir y juntar es O(n))

# A es natural - B es Real, >1, cte - Caso base es cte

# logB(A) = log2(2) = 1 = C --> T(n) = O(n^C * logB(n)) = O(n log n)