'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [18,4,11,-2,5,100]

def stats(num_list):
    """Returns key statistics for a list of numbers

    Takes a list of ints and/or floats

    Returns max, min, average, and sum of list in ints and floats
    """

    num_list.sort()
    max = num_list[-1]
    min = num_list[0]
    total = sum(num_list)
    avg = total/len(num_list)
    all_stats = {"max":max, "min":min, "sum":total, "average":avg}
    return all_stats

# call the function below here
stats = stats(example_list)
for stat, value in stats.items():
    print(f"{stat}: {value}")