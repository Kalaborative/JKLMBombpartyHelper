print("Choose dictionary: English or French")
language = input("> ")

dictionary = False
if language.lower() == "english":
    dictionary = "sowpods.txt"
elif language.lower() == "french":
    dictionary = "touslesmots.txt"

if dictionary:
    while True:
        print("Enter the word or words you want to remove")
        print("Include the plus symbol if you want to delete all words that starts with the string.")
        print("Example: 'holly+' will delete all words that start with holly.")
        remove = input("> ")
        query = remove.split(" ")
        query = [q.lower() for q in query]
        with open(dictionary, 'r+') as f:
            d = f.readlines()
            f.seek(0)
            words = f.read().splitlines()
            for q in query:
                if q[-1:] == "+":
                    print("Expression triggered.")
                    root = q[:-1]
                    print("Deleting all words starting with {}...".format(root))
                    f.seek(0)
                    for i in d:
                        if not i.strip("\n").startswith(root):
                            f.write(i)
                        else:
                            print("Matching word '{}' removed.".format(i.strip("\n")))
                    print("Done!\n")
                elif q in words:
                    print("Removing {}...".format(q))
                    f.seek(0)
                    for i in d:
                        if i.strip("\n") != q:
                            f.write(i)
                    # f.truncate()
                    print("Done!\n")
                else:
                    print("Word '{}' not found in dictionary.\n".format(q))
else:
    print("Invalid language. Please type 'English' or 'French'")