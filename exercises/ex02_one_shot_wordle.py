"""EX02 - Wordle- The Real Deal."""

__author__ = "730471008"

KEY_WORD: str = "python"
length: int = len(KEY_WORD)
guess: str = input(f"What is your {length}-letter guess? ")
game: bool = True
i: int = 0
emoji_call: str = ""
WHITE_BOX: str = "\U00002B1C"  # wrongletter
G: str = "\U0001F7E9"  # rightplace
YELLOW_BOX: str = "\U0001F7E8"  # rightletter/wrongplace

# Length has to be same length as key word
while len(guess) != length:
    wrong_guess: str = input(f"That was not {length} letters! Try again: ")
    guess = wrong_guess
# Continue on if length is right to see if the word is right 
while i < length:
    # Print green box if the letter is right
    if guess[i] == KEY_WORD[i]:
        emoji_call = emoji_call + G
    else:
        second_int: int = 0
        wrong_place: bool = False
        # Wrong boxes
        while second_int < length and wrong_place is False:
            if guess[i] == KEY_WORD[second_int]:
                wrong_place = True
            else:
                second_int = second_int + 1
        # Print yellow if right letter, wrong place
        if wrong_place is True:
            emoji_call = emoji_call + YELLOW_BOX
        else:
            # Print white if nothing is right
            emoji_call = emoji_call + WHITE_BOX
    i = i + 1
# Game win or lose
print(emoji_call)
if guess != KEY_WORD:
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")