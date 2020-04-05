from random import shuffle
with open("touslesmots.txt", "r") as text:
    words = text.read().splitlines()
    print("Enter the string to find, optionally enter desired letters after a space.")
    print("Example: ar")
    print("Example: att b")
    print("Example: tt skp")
    while True:
        search = input("Enter your string: ")
        print("Searching ...")
        multi_search = search.split(" ")
        if len(multi_search) > 2:
            print("Please search only with one space.")
        else:      
            matches = []
            for word in words:
                if multi_search[0].lower() in word:
                    matches.append(word)
            try:
                additional = multi_search[1].lower()
                for a in additional:
                    matches = list(filter(lambda x: a in x, matches))
            except IndexError:
                pass
            if matches:
                print("Found {} results: ".format(len(matches)))
                shuffle(matches)
                if len(matches) > 20:
                    matches = matches[:20]
                    print("Printing the first twenty results: ")
                for m in matches:
                        print(m)
            else:
                print("No matches found for that string/combination.")
