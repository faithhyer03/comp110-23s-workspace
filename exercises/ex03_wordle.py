"""Worlde fr"""
__author__= "730471008"

def contains_char(wordsearch: str, character: str) -> bool:
    """Returns T/F if the character is in the word string"""
    assert len(character) == 1
    i: int = 0
    while i < len(wordsearch):
        if wordsearch[i] == character:
            return True
        i = i + 1
    return False
                 
def emojified(key_word: str, guess: str) -> str:
    assert len(guess) == len(key_word)
    x: int = 0
    y: str = ""
    WHITE_BOX: str = "\U00002B1C"  # wrongletter
    GREEN_BOX: str = "\U0001F7E9"  # rightplace
    YELLOW_BOX: str = "\U0001F7E8"  # rightletter/wrongplace
    while x < len(key_word):
        if guess[x] == key_word[x]:
            y = y + GREEN_BOX
        else:
            if contains_char(guess, key_word[x]) == True:
                y = y + YELLOW_BOX
            else:
                contains_char(guess, key_word[x]) == False
                y = y + WHITE_BOX
        x = x + 1
    return y

def input_guess(word_length: int) -> str:
    guess: str = input(f"Enter a {word_length} character word: ")
    while len(guess) != word_length:
        guess_again: str = input(f"That wasn't {word_length} chars! Try again: ")
        guess = guess_again
    return guess

def main() -> None:
    won: bool = False
    turn: int = 1
    key_word: str = "codes"
    while won == False and turn <= 6:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(key_word))
        print(emojified(key_word, guess))
        if key_word == guess:
            won = True
            print(f"You won in {turn}/6 turns!")
        else:
            turn = turn + 1
    if won == False:
        print("X/6 - Sorry, try again tomorrow")

if __name__ == "__main__":
    main()
        