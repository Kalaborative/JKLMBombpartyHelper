from random import shuffle

while True:
    query = input("Enter search: ")
    with open('sowpods.txt', 'r') as text:
        words = text.readlines()
        words = [word.strip() for word in words]
    
        matches = [w for w in words if query in w]
        print(f"Found {len(matches)} matches. ")
        if len(matches) > 10:
            print("Example results:")
            shuffle(matches)
            for m in matches[:10]:
                print(m)
        else:
            for m in matches:
                print(m)