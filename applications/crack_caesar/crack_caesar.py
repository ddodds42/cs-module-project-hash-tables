# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

qraqt = {
    'A':'C','B':'F','C':'H','D':'N','E':'M','F':'Y','G':'U','H':'V',
    'I':'I','J':'T','K':'R','L':'X','M':'A','N':'S','O':'W','P':'K',
    'Q':'G','R':'Z','S':'L','T':'J','U':'D','V':'Q','W':'E','X':'O',
    'Y':'B','Z':'P'
}

with open("ciphertext.txt") as f:
    corpus = f.read()

def brutus(s):
    decoded = ""
    for let in s:
        if let in qraqt:
            decoded += qraqt[let]
        else:
            decoded += let
    return decoded

print(brutus(corpus))