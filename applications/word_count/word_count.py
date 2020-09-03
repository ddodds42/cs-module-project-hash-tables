def word_count(s):
    slow = s.lower()
    lean = slow.strip(
        '''
        : ; + = / \ | [ ] { } * ^ &
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
    pesqy = pesqy.replace(":", '')
    pesqy = pesqy.replace(";", '')
    pesqy = pesqy.replace("+", '')
    pesqy = pesqy.replace("=", '')
    pesqy = pesqy.replace("/", '')
    pesqy = pesqy.replace("\\", '')
    pesqy = pesqy.replace("|", '')
    pesqy = pesqy.replace("[", '')
    pesqy = pesqy.replace("]", '')
    pesqy = pesqy.replace("{", '')
    pesqy = pesqy.replace("}", '')
    pesqy = pesqy.replace("*", '')
    pesqy = pesqy.replace("^", '')
    pesqy = pesqy.replace("&", '')

    lex = pesqy.split()

    endgame = {}

    if len(lex) ==0:
        return endgame
    for word in lex:
        if word in endgame:
            endgame[word] +=1
        else:
            endgame[word] = 1
    return endgame

if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))