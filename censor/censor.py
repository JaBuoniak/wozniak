# Opiszmy co tu się wyrabia:
def censor(text, word):  # definiujesz funkcję, która ma ocenzurować wszystkie wystąpienia słowa 'word' w tekście 'text'
    censoredText = ""
    wordLength = len(word)
    positionOfFirstFoundWord = text.find(word)
    actualPosition = 0
    while(actualPosition < len(text)):

        if actualPosition >= positionOfFirstFoundWord and actualPosition < positionOfFirstFoundWord+wordLength:
            censoredText += "*"
        else:
            censoredText += text[actualPosition]

        actualPosition += 1

    return censoredText


zdanie = "Ania posiada kota"
slowo = "posiada"
print(censor(zdanie, slowo))    # tu wywołujesz powyższą funkcję podając jej argumenty. Spodziewasz się, że funkcja coś zwróci, a ty chcesz to wypisać.
