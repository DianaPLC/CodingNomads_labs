'''
Write a script that reads in the words from the words.txt file and finds and prints:

1. The shortest word (if there is a tie, print all)
2. The longest word (if there is a tie, print all)
3. The total number of words in the file.


'''
# Get the file and read it as a list of lines
with open('words.txt','r') as word_file:
    word_list = word_file.readlines()

# Length of list = number of words
num_words = len(word_list)

# Set holders for longest and shortest
shortest = word_list[0].rstrip()
short_list = [shortest]
longest = word_list[0].rstrip()
long_list = [longest]

# Iterate through list:
for word in word_list:
    word = word.rstrip()
    # If word is > longest, it is new longest
    if len(word) >= len(longest):
        longest = word
        long_list.append(longest)
        for long_word in long_list:
            if len(long_word) < len(longest):
                long_list.remove(long_word)
    # if word is < shortest, it is new shortest
    elif len(word) <= len(shortest):
        shortest = word
        short_list.append(shortest)
        for short_word in short_list:
            if len(short_word) > len(shortest):
                short_list.remove(short_word)

# Print number of words, shortest, longest
print(f"There are {num_words} words in the list.")
print_short = "The shortest words in the list are:"
for short_word in short_list:
    print_short += f"\n{short_word}"
print(print_short)
print_long = "The longest words are:"
for long_word in long_list:
    print_long += f"\n{long_word}"
print(print_long)