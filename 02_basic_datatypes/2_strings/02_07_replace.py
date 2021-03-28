'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

sentence = input("Please type a short sentence: ")
symbol = input("Please enter a symbol: ")

first_letter = sentence[0]
output = sentence.replace(first_letter,symbol)
print(output)
