import sys
import csv

# Read Min Word Length and Characters from the Command Line
minWordLength = sys.argv[1]
characters = []
n = len(sys.argv)
for x in range(2, n):
    characters.append(sys.argv[x])
special_char = characters[-1]

'''
TrieNode Class
'''


class TrieNode(object):
    def __init__(self, char: str):
        self.char = char
        self.children = []
        # Is it the last character of the word.`
        self.word_finished = False
        # How many times this character appeared in the addition process
        self.current_substring = ''
        self.counter = 1

    def add(root, word: str):
        node = root
        for char in word:
            found_in_child = False
            for child in node.children:
                if child.char == char:
                    child.counter += 1
                    node = child
                    found_in_child = True
                    break
            if not found_in_child:
                new_node = TrieNode(char)
                new_node.current_substring = node.current_substring + char
                node.children.append(new_node)
                node = new_node
        node.word_finished = True


'''
Iterates through the Trie Data Structure peforming a DFS to find words
'''


def nyt(root, chars):
    if root != None:
        if root.word_finished and len(root.current_substring) >= int(minWordLength):
            if special_char in root.current_substring:
                print(root.current_substring)
        for char in chars:
            for child in root.children:
                if child.char == char:
                    nyt(child, chars)


if __name__ == '__main__':
    dict = TrieNode('')
    filepath = "words.csv"
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            dict.add(row[0])
    nyt(dict, characters)
