Recently I've been addicted to the New York Times' Spelling Bee game.
For those of you that don't know how it works:
You are given 7 letters, with one of those letters being a special letter.
And you have to try to come up with as many English words as
you can that using those letters. Every word must contain the special
letter, and have a minimum length of 4 characters.

The solution is implemented with a Trie Data Structure, and the
word dataset was taken from UMich's jlawler wordlist, and
contains 69,903 words.

Application is simple, and is designed to run through the command
line. Format for running the application is:

python trie.py <Minimum Word Length> <List of Non-Special Characters> <Special Char>

Example call using with characters h, m, b, l, e, and d. Special Char is d, and
minimum Word Length is 4:
python trie.py 4 h m b l e d u
