words = open("book.txt","r").read().split()
words = [x.strip(".,()$:;?!\"'") for x in words]

def freq(word):
    return len(filter(lambda x: x.lower() == word.lower(), words))



def freqs(wordlist):
    return reduce(lambda a,b: a + b, map(freq, wordlist))

def mostcommon(words):
    words2 = set(words)
    def freq2(word):
        return filter(lambda x: x.lower() == word.lower(), words)

    return reduce(lambda a,b: a if len(a) > len(b) else b,(map(freq2, words2)))[0]


print freq("the")

print freq("not")

print freq("in")

print freq("the") + freq("in") + freq("not")

print freqs(["the", "not", "in"])

print mostcommon(words)
