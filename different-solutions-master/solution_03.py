'''
Write a script that sorts a list of tuples based on the number value in the tuple.
For example:

unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = [('second_element', 2), ('first_element', 4), ('third_element', 6)]

'''
#Missing code comments
unsorted_list = [('first_element', 4), ('second_element', 2), ('third_element', 6)]
sorted_list = []

for x in range(0, len(unsorted_list)):

    min = unsorted_list[0][1]
    print(min) #good for debugging; should be removed in final code
    index = 0

    for i in range(0, len(unsorted_list)): #Starting from index 0 is not necessary; this checks if min<min on the first pass
        if unsorted_list[i][1] < min:
            min = unsorted_list[i][1]
            index = i
    sorted_list.append(unsorted_list[index])
    unsorted_list.remove(unsorted_list[index]) #if using index like this, use the .del method instead
        #Again, pop could reduce the two lines above to one


print(unsorted_list)
print(sorted_list)
#Similar to the first solution, I think you can save a bit of time by assuming each value is lowest/highest as you go.