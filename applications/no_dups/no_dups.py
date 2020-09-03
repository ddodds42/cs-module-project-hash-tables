def no_dups(s):
    words = s.split()
    chekr = {}
    for w in words:
        if w not in chekr:
            chekr[w] = 0
    undup = list(chekr.keys())
    output = ""
    for w in undup:
        if output == '':
            output += w
        else:
            output += ' ' + w
    return output



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))