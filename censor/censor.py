def censor(text, word):

    for char in text:
        x = text.lower()
        if word == "posiada":
            for char in word:
                new = replace(char,"*")
    print new

zdanie = "Ania posiada kota"
slowo = "posiada"
print censor(zdanie, slowo)