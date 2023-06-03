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
    input_words = [word.strip().lower() for word in user_input.split(",")]

    # Track added and existing words
    added_words = []
    existing_input_words = []

    for new_word in input_words:
        # Check if the word is already in the list
        if new_word in existing_words:
            existing_input_words.append(new_word)
        else:
            # Add the new word to the list
            existing_words.add(new_word)
            added_words.append(new_word)

    # Save the updated list back to the file
    with open(file_path, "w") as file:
        for word in existing_words:
            file.write(word + "\n")

    if added_words:
        print("Word(s) added successfully:", ', '.join(added_words))
    else:
        print("No new words to add.")

    if existing_input_words:
        print("Word(s) already in the list:", ', '.join(existing_input_words))

