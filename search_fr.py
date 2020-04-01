from random import shuffle
with open("touslesmots.txt", "r") as text:
    words = text.read().splitlines()
    while True:
        search = input("Enter your string: ")
        print("Searching ...")
        matches = []
        for word in words:
            if search.lower() in word:
                matches.append(word)
        if matches:
            print("Found {} results: ".format(len(matches)))
            shuffle(matches)
            if len(matches) > 20:
                matches = matches[:20]
                print("Printing the first twenty results: ")
            for m in matches:
                    print(m)
        else:
            print("No matches found for that string.")
