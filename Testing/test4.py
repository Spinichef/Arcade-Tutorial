"""def calculator():
    zahl1 = input("gebe eine zahl ein ")
    rechenzeichen1 = input("gebe ein rechenzeichen ein ")
    zahl2 = input("gebe eine zweite zahl ein ")
    plus = int(zahl1) + int(zahl2)
    mal = int(zahl1) * int(zahl2)
    if rechenzeichen1 == plus:
        int(zahl1) + int(zahl2)
    elif rechenzeichen1 == mal:
        int(zahl1) * int(zahl2)
    ergebnis = int(zahl1), int(rechenzeichen1), int(zahl2)
    print("Das Ergebnis ist ", ergebnis)

calculator()"""

"""def calculator():
    zahl1 = int(input("Bitte Zahl eingeben"))
    zahl2 = int(input("Bitte Zahl eingeben"))
    rechenzeichen = input("Bitte Rechenzeichen eingeben")

    if rechenzeichen == "+":
        ergebnis = zahl1 + zahl2
    elif rechenzeichen == "-":
        ergebnis = zahl1 - zahl2
    elif rechenzeichen == "":
        ergebnis = zahl1 * zahl2
    elif rechenzeichen == "/":
        ergebnis = zahl1 / zahl2

    print("Das ergebnis ist: " + str(ergebnis))

calculator()"""

def calculator():
    zahl1 = int(input("gebe eine zahl ein "))
    rechenzeichen1 = input("gebe ein rechenzeichen ein ")
    zahl2 = int(input("gebe eine zweite zahl ein "))
    if rechenzeichen1 == "+":
        ergebnis = (zahl1) + (zahl2)
    elif rechenzeichen1 == "*":
        ergebnis = (zahl1) * (zahl2)
    elif rechenzeichen1 == "/":
        ergebnis = (zahl1) / (zahl2)
    print("Das Ergebnis ist " + str(ergebnis))

calculator()