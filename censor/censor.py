# Opiszmy co tu się wyrabia:
def censor(text, word):  # definiujesz funkcję, która ma ocenzurować wszystkie wystąpienia słowa 'word' w tekście 'text'
    for char in text:   # przechodzisz po wszystkich znakach zadanego tekstu 'text'
        x = text.lower()  # 'x' staje się tekstem 'text' zapisanym tylko małymi literami, ale to nie istotne, bo nie używasz tej zmiennej
        if word == "posiada":   # sprawdzasz, czy słowo 'word', które podałaś dla funkcji ma wartość 'posiada' - w tym przypadku zawsze jest to prawda
            for char in word:   # jeśli to prawda, to dla każdej litery w słowie 'word' (czyli dla liter 'p', 'o', 's', 'i', 'a', 'd', 'a') wykonujesz co następuje:
                new = replace(char, "*")    # zmienna 'new' dostaje wartość, jaką zwróci funkcja 'replace(c,r)' - na dobrą sprawę nie wiem, czego oczekujesz, bo znalazłem kilka zupełnie różnych implementacji tej funkcji
    print(new)  # po przejściu wszystkich liter zadanego tekstu 'text' wypisuje ostatni wynik funkcji 'replace', czyli 'replace("a", "*")'
# no i tyle. Funkcja 'censor' kończy się ale nic nie zwraca.

zdanie = "Ania posiada kota"
slowo = "posiada"
print(censor(zdanie, slowo))    # tu wywołujesz powyższą funkcję podając jej argumenty. Spodziewasz się, że funkcja coś zwróci, a ty chcesz to wypisać.
