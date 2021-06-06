'''
Write a program that reads words.txt and prints only the words
with more than 20 characters (not counting whitespace).
'''

with open('words.txt', 'r') as word_file:
    word_list = word_file.readlines()

for word in word_list:
    word = word.rstrip()
    if len(word) > 20:
        print(word)