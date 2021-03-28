'''

Using string slicing, take in the user's name and print out their name translated to pig latin.
For the purpose of this program, we will say that any word or name can be
translated to pig latin by moving the first letter to the end, followed by "ay".

For example: ryan -> yanray, caden -> adencay

'''
name = input("Please enter your name: ")
vowels = "aeiou"

if name[0].lower() in vowels:
    translated = name+"way"
else:
    translated = name[1:]+name[0].lower()+"ay"

print(translated.capitalize())