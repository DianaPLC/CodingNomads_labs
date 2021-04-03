'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
    #Code comments are missing
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

value_list = []
for tuple_ in unsorted_list:
    value_list.append(tuple_[1])

print(value_list)
value_list.sort()
    #Transitioning to a form that permits .sort() is a great idea; not sure about the impact on efficiency

for value in value_list:
    for tuple_ in unsorted_list:
        if tuple_[1] == value:
            sorted_list.append(tuple_)
            unsorted_list.remove(tuple_)
                #pop would reduce the two lines above to one
            break
#Overall, this ends up iterating through the list n+n^2 times, and also applying .sort(); inefficient

print(sorted_list)
