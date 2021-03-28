'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
word1 = input("Please enter a word: ")
word2 = input("Please enter another word: ")
word3 = input("One more time: ")

longest = ""

def wordOutput(word):
    length = len(word)
    global longest
    if length > len(longest):
        longest = word
    output = str(length)+", "+word
    print(output)

wordOutput(word1)
wordOutput(word2)
wordOutput(word3)

print(longest,"is the longest word")