'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''
sentence = input("Please enter a sentence: ")

sentence = sentence.lower()
vowels = ["a","e","i","o","u"]
pseudo_vowels = ["y","w"]

def get_count(sentence,set):
    total = 0
    for letter in set:
        count = sentence.count(letter)
        time_times = " times"
        if count == 1:
            time_times = " time"
        print(letter," appears ",count,time_times)
        total += count
    return total

vowel_total = get_count(sentence,vowels)
pseudo_total = get_count(sentence,pseudo_vowels)
print("There are ",vowel_total," regular vowels in the sentence, and ",pseudo_total," y's and w's")
