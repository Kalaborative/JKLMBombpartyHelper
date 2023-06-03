file_path = "sowpods.txt"

while True:
    # Read the existing words from the file
    with open(file_path, "r") as file:
        existing_words = {word.strip() for word in file.readlines()}

    # Prompt the user for words (comma-separated)
    user_input = input("Enter word(s) separated by commas (or 'quit' to exit): ")

    if user_input.lower() == "quit":
        break

    # Split the input into individual words
    input_words = [word.strip() for word in user_input.split(",")]

    # Track removed and non-existing words
    removed_words = []
    non_existing_words = []

    for word in input_words:
        if word in existing_words:
            # Remove the word from the list
            existing_words.remove(word)
            removed_words.append(word)
        else:
            non_existing_words.append(word)

    # Save the updated list back to the file
    with open(file_path, "w") as file:
        for word in existing_words:
            file.write(word + "\n")

    if removed_words:
        print("Word(s) removed successfully:", ', '.join(removed_words))
    else:
        print("No words to remove.")

    if non_existing_words:
        print("Word(s) not found in the list:", ', '.join(non_existing_words))

