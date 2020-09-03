def word_shadow(s):
    slow = s.lower()
    lean = slow.strip(
        '''
        ":;,.-+=/\|[]{}()*^&?!
        '''
)
    peski = lean.replace('"', '')
    peskee = peski.replace("'", '')
    pesky = peskee.replace(".", '')
    pesqy = pesky.replace(",", '')
    pesqy = pesqy.replace("-", ' ')
    pesqy = pesqy.replace("(", '')
    pesqy = pesqy.replace(")", '')
    pesqy = pesqy.replace("?", '')
    pesqy = pesqy.replace("!", '')

    lex = pesqy.split()

    endgame = {}

    if len(lex) ==0:
        return endgame
    for w in range(len(lex)-1):
        if lex[w] in endgame:
            endgame[lex[w]].append(lex[w+1])
        else:
            endgame[lex[w]] = [lex[w+1]]
    return endgame

if __name__ == "__main__":
    print(word_shadow(""))
    print(word_shadow("Hello"))
    print(word_shadow('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_shadow('This is a test of the emergency broadcast network. This is only a test.'))