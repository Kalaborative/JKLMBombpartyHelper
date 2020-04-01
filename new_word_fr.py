import json

while True:
    print("Enter the new word you want to add:")
    new_word = input("> ")
    new_word = new_word.lower()
    print("Seeing if this word already exists...")
    current_dict = open('touslesmots.txt', "r")
    all_words = current_dict.read().splitlines()
    current_dict.close()
    print(len(all_words))
    if new_word in all_words:
        print("This word already exists. No new word added!")
    else:
        francais = open('touslesmots.txt', "a+")
        print("Adding new word: '{}'...".format(new_word))
        new_word += "\n"
        francais.write(new_word)
        francais.close()
        print("Done!")
