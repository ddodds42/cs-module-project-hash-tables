import sys
sys.path.insert(1, "../word_count/")
from word_count import word_count

with open("robin.txt") as f:
    words = f.read()

def fquncy(s):
    wordkey = word_count(s)
    quincy = {}
    for w in wordkey:
        hertz = wordkey[w] 
        if hertz in quincy:
            quincy[hertz].append(w)
        else:
            quincy[hertz] = [w]
    hzs = list(quincy.keys())
    hzs.sort(reverse=True)
    for f in hzs:
        for word in quincy[f]:
            print(word, ' '*(20-len(word)), '#'*f)
    # return hzs

tast = fquncy(words)

print(tast)