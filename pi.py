def find_word_with_max_elimination(prompt, letter_bank, word_list):
    max_score = 0
    best_word = None

    for word in word_list:
        if prompt in word:
            score = calculate_elimination_score(letter_bank.copy(), word)
            print(word, score)
            if score > max_score:
                max_score = score
                best_word = word

    return best_word


def calculate_elimination_score(letter_bank, word):
    score = 0
    for letter in word:
        if letter in letter_bank:
            letter_bank.remove(letter)
            score += 1

    return score


# Example usage
prompt = "e"
letter_bank = ["a", "s", "e", "t", "r"]
word_list = ["race", "ace", "assert", "embrace", "trace"]

result = find_word_with_max_elimination(prompt, letter_bank, word_list)
print(result)  # Output: "trace"
