original_file_path = "sowpods.txt"
new_words_file_path = "words.txt"

# Read the existing words from the original file
with open(original_file_path, "r") as file:
    existing_words = {word.strip().lower() for word in file.readlines()}

# Read the new words from the new words file
with open(new_words_file_path, "r") as file:
    new_words = [word.strip().lower() for word in file.readlines()]

# Track added and existing words
added_words = []
existing_input_words = []

for new_word in new_words:
    # Check if the word is already in the list
    if new_word in existing_words:
        existing_input_words.append(new_word)
    else:
        # Add the new word to the list
        existing_words.add(new_word)
        added_words.append(new_word)

# Save the updated list back to the original file
with open(original_file_path, "w") as file:
    for word in existing_words:
        file.write(word + "\n")

if added_words:
    print("Word(s) added successfully:", ', '.join(added_words))
else:
    print("No new words to add.")

if existing_input_words:
    print("Word(s) already in the list:", ', '.join(existing_input_words))
