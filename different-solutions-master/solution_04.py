'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

#Missing code comments
for tup in list(unsorted_list):

    current_min = unsorted_list[0][1]
    index = 0

    for i in range(0, len(unsorted_list)): #start from i = 1
        if unsorted_list[i][1] < current_min:
            current_min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index])
        #simpler to use pop

print(unsorted_list)
print(sorted_list)
