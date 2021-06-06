'''
Write a script that reads in the contents of words.txt and writes the contents in reverse
to a new file words_reverse.txt.
'''

# Read words as a list
with open('words.txt','r') as word_file:
    word_list = word_file.readlines()

# Write to a new file
with open('words_reverse.txt','w') as reverse_file:
    for word in reversed(word_list):
        reverse_file.write(word)