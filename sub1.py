import json

def sub1_twoletters(file_path):
    """Finds words with a unique two-letter syllable from a file."""
    syllable_dict = {}

    with open(file_path, "r") as file:
        for line in file:
            word = line.strip().lower()
            
            if "'" in word or "-" in word:
                continue
            
            for i in range(len(word) - 1):
                syllable = word[i:i+2]
                if syllable in syllable_dict:
                    syllable_dict[syllable].append(word)
                else:
                    syllable_dict[syllable] = [word]

    unique_syllable_words = []
    for syllable, words in syllable_dict.items():
        if len(words) <= 5:
            unique_syllable_words.append(words[0])
    
    return unique_syllable_words

def sub1_threeletters(file_path):
    """Finds words with a unique three-letter syllable from a file."""
    syllable_dict = {}

    with open(file_path, "r") as file:
        for line in file:
            word = line.strip().lower()
            
            if "'" in word or "-" in word:
                continue
            
            for i in range(len(word) - 2):
                syllable = word[i:i+3]
                if syllable in syllable_dict:
                    syllable_dict[syllable].append(word)
                else:
                    syllable_dict[syllable] = [word]

    unique_syllable_words = []
    for syllable, words in syllable_dict.items():
        if len(words) <= 5:
            unique_syllable_words.append(words[0])
    
    return unique_syllable_words


# Example usage
file_path = "sowpods.txt"
twolettersubs = sub1_twoletters(file_path)
threelettersubs = sub1_threeletters(file_path)

words_to_add = set()
for t in twolettersubs:
    words_to_add.add(t)
for t in threelettersubs:
    words_to_add.add(t)

output_path = 'sub1.txt'
with open(output_path, 'w') as output_file:
    for w in words_to_add:
        output_file.write(w + '\n')

print("Done")