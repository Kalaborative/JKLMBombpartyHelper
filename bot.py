from time import sleep
from random import choice
from termcolor import colored
import pyperclip
import json
letterbank = "abcdefghijlmnopqrstuv"

individual_letters = []

for l in letterbank:
    individual_letters.append(l)

print("Choose ENGLISH or FRENCH")
language = input("> ")
if language.lower() == "english":
    with open("sowpods.txt", "r") as wordlist:
        text = wordlist.read().splitlines()
        print("Word list loaded.")
        sleep(1)
        print("To quit the program, type 'stop'.")
        sleep(1)
        print("Type 'report' to report a word for not valid.")
        reported_words = []
        while True:
            matching_words = []
            if not individual_letters:
                for l in letterbank:
                    individual_letters.append(l)
            print(individual_letters)
            letters = input("Send a combination of letters: ")
            if letters.lower() == "stop":
                if reported_words:
                    print("Reported words this game:")
                    for bad_word in reported_words:
                        print(colored(bad_word, 'red'))
                break
            found = False
            for word in text:
                if letters in word.lower():
                    found = True
                    matching_words.append(word)
            
            if not found:
                print("A match could not be found!")
            else:
                preferred_words = [word for word in matching_words for i in individual_letters if i in word.lower()]
                if preferred_words:
                    chosen_word = choice(preferred_words)
                else:
                    chosen_word = choice(matching_words)                    
                print("Result: {}".format(colored(chosen_word, 'green')))
                pyperclip.copy(chosen_word)
                print("Press enter to accept otherwise enter any text if failed.")
                unacceptable = input("> ")
                if "report" in unacceptable:
                    print("Reported this word.")
                    reported_words.append(chosen_word)
                if not unacceptable:
                    for c in chosen_word:
                        if c.lower() in individual_letters:
                            individual_letters.remove(c.lower())    
elif language.lower() == "french":
    with open("touslesmots.txt", "r") as wordlist:
        text = wordlist.read().splitlines()

        # Longer words only! 
        # text = [t for t in text if len(t) > 8]

        print("Word list loaded.")
        sleep(1)
        print("To quit the program, type 'stop'.")
        sleep(1)
        print("Type 'report' to report a word for not valid.")
        reported_words = []
        while True:
            matching_words = []
            if not individual_letters:
                for l in letterbank:
                    individual_letters.append(l)
            # print(individual_letters)
            letters = input("Send a combination of letters: ")
            if letters.lower() == "stop":
                if reported_words:
                    print("Reported words this game:")
                    for bad_word in reported_words:
                        print(colored(bad_word, 'red'))
                break
            found = False
            for word in text:
                if letters in word.lower():
                    found = True
                    matching_words.append(word)
            
            if not found:
                print("A match could not be found!")
            else:
                preferred_words = [word for word in matching_words for i in individual_letters if i in word]

                # Prefer words that are adjectives!
                # preferred_words_adj = [p for p in preferred_words if p[-4:] == "ment"]
                # if preferred_words_adj:
                #     chosen_word = choice(preferred_words_adj)
                if preferred_words:
                    chosen_word = choice(preferred_words)
                else:
                    chosen_word = choice(matching_words)                    
                print("Result: {}".format(colored(chosen_word, 'green')))
                pyperclip.copy(chosen_word)
                print("Press enter to accept otherwise enter any text if failed.")
                unacceptable = input("> ")
                if "report" in unacceptable:
                    reported_words.append(chosen_word)
                    print("Reported this word.")
                text.remove(chosen_word)
                if not unacceptable:                  
                    for c in chosen_word:
                        if c.lower() in individual_letters:
                            individual_letters.remove(c.lower())
else:
    print("Please type either 'english' or 'french'.")