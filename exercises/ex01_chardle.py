"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730471008"

word: str = input("Enter a 5-character word: ")
if (len(word) != 5):
    print("Error: Word must contain 5 characters")
    exit()
character: str = input("Enter a single character: ")    
if (len(character) != 1):
    print("Error: Character must be a single character")
    exit()
ch_count: int = 0

print("Searching for " + character + " in " + word)


if (character == word[0]):
    print(word[0] + " found at index 0")
    ch_count = ch_count + 1 
if (character == word[1]):
    print(word[1] + " found at index 1")
    ch_count = ch_count + 1
if (character == word[2]):
    print(word[2] + " found at index 2")
    ch_count = ch_count + 1
if (character == word[3]):
    print(word[3] + " found at index 3")
    ch_count = ch_count + 1
if (character == word[4]):
    print(word[4] + " found at index 4")
    ch_count = ch_count + 1
if (ch_count == 1):
    print(ch_count, "instance of", character, "found in", word)
if (ch_count == 0):
    print("No instances of", character, "found in", word)
else:
    print(ch_count, "instances of", character, "found in", word)
