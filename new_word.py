print("English or French?")
language = input("> ")

language = language.lower()
while True:
    print("Enter the new word you want to add:")
    print("Or enter batch of words separated by the | or , symbol.")
    word_or_words = input("> ")
    query = []
    if "|" in word_or_words:
        query = word_or_words.split(" | ")
    elif "," in word_or_words:
        query = word_or_words.split(", ")
    else:
        query.append(word_or_words)
    query = [q.lower() for q in query]
    if language == "english":
        current_dict = open('sowpods.txt', "r")
        all_words = current_dict.read().splitlines()
        current_dict.close()
        for word in query:
            print("Checking {}...".format(word))
            if word in all_words:
                print("This word already exists. No new word added!")
            else:
                english = open('sowpods.txt', "a+")
                print("Adding new word: '{}'...".format(word))
                word += "\n"
                english.write(word)
                english.close()
                print("Done!")
        print("\n")
    elif language == "french":
        current_dict = open('touslesmots.txt', "r")
        all_words = current_dict.read().splitlines()
        current_dict.close()
        for word in query:
            print("Checking {}...".format(word))
            if word in all_words:
                print("This word already exists. No new word added!")
            else:
                francais = open('touslesmots.txt', "a+")
                print("Adding new word: '{}'...".format(word))
                word += "\n"
                francais.write(word)
                francais.close()
                print("Done!")
        print("\n")