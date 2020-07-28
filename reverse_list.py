# Author: Makaliah Dickinson
# Date: 7/27/2020
# Description: Write a function that takes as a parameter a list and and reverses the order of the elements in that list.
#             It should not return anything - it should reverse the original list.

def reverse_list(lst):
    i = 0
    j = len(lst) - 1
    while i < j:
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp
        i += 1
        j -= 1


lst = [7, -3, 12, 9]
reverse_list(lst)
print(lst)
