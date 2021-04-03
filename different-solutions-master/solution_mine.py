'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
#Acknowledging that using sorted() is probably best, here is a solution that doesn't rely on that.
#My goal was to reduce full iterations through the list; I'm not sure this reduces runtime, though, since it has a lot
# of nested logic. Depending on requirements, I think this could be a useful solution for longer lists. (Though for a long
# enough list probably a sorting algorithm that reliably splits the list in half would be better.)

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]

#Seed the sorted list with a first element to set comparative value for sorting
sorted_list = [unsorted_list.pop(0)]
last_val = sorted_list[0][1]
last_index = 0

for tup in unsorted_list:
    val = tup[1]
    #Check each value against the last added one to limit number of items in the sorted list we iterate over
    if val < last_val:
        #If the new item is lower than the last one, check downward until you find an item that is lower than the new one,
        # or the start of the list.
        while last_index > 0:
            if val > sorted_list[last_index-1][1]:
                break
            last_index -= 1
    else:
        #If the new item is higher than the last one, check upward until you find an item that is higher than the new one,
        # or the end of the list
        last_index += 1
        while last_index < len(sorted_list):
            if val < sorted_list[last_index][1]:
                break
            last_index += 1
    last_val = val
    sorted_list.insert(last_index,tup)

print(sorted_list)
