

def get_all_index(text, word):
   # return [i for i, letter in enumerate(word) if letter == text]
    found_index = []
    for i in range(len(word)):
        if word[i] == text:
            found_index.append(i)
    return found_index

# 1. l -> xxllx
# 2. e -> xellx


def get_new_masked_word(masked_word, word, indexes):
    new_masked_word_list = list(masked_word)

    for step in range(len(word)):
        if step in indexes:
            new_masked_word_list[step] = word[step]

    return "".join(new_masked_word_list)


def lost():
    print("Sorry, U have lost")
    exit(1)


def win():
    print("Congratulation, U have won")
    exit(0)


def new_guess(guess, word, masked_word):
    index_list = get_all_index(guess, word)
    return get_new_masked_word(masked_word, word, index_list)


def handle_final_guess(text, word):
    if text == word:
        win()
    else:
        lost()


if __name__ == '__main__':
    word = "hello"
    MAX_GUESS = 3
    print(f"hangman application. Try to guess my word. You have {MAX_GUESS} chance.")

    masked_word = len(word) * "x"

    for step in range(MAX_GUESS):
        print(f"{step + 1}. step, pls give me a letter")
        text = input()

        is_new_guess = len(text) == 1
        if is_new_guess:
            masked_word = new_guess(text, word, masked_word)
            print(f"masked_word {masked_word}")
            if masked_word == word:
                win()
        else:
            handle_final_guess(text, word)

    lost()