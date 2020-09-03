import random
from word_shadow import word_shadow

# Read in all the words in one go
with open("input.txt") as f:
    words = f.read()

# print(type(words))
# print(word_shadow('Hello, my cat. And my cat doesn\'t say "hello" back.'))
lexicon = word_shadow(words)
# print(lexicon)

# TODO: construct 5 random sentences

for i in range(5):
    intro = random.choice(list(lexicon.items()))[0]
    jibbish = intro
    for i in range(random.randint(20, 40)):
        nex = random.choice(lexicon[intro])
        jibbish += ' ' + nex
        intro = nex
    print('\n', jibbish, '\n')