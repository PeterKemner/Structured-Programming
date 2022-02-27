import random
import itertools

#bronvermelding:
#https://www.geeksforgeeks.org/randrange-in-python/ voor de random.randrange()
#https://docs.python.org/3/library/itertools.html voor de itertools.product()
#https://stackoverflow.com/questions/13712229/simultaneously-replacing-all-values-of-a-dictionary-to-zero-python voor de dictionary values terug naar 0 zetten
#hulp van Mo bij eigen_algoritme, Mo liet zijn code zien en heeft me geholpen met het begrijpen en het maken van de functie


kleuren = ['R', 'O', 'Y', 'G', 'C', 'B']


def Random_Code_Generator(kleuren):
    # pakt een random getal tussen 0 en 6
    # pakt een randomg getal en gebruikt dat getal als index en pakt uit de lijst kleuren een kleur, en dat 4 keer
    # die letters worden in een lijst gedaan (random_code) en die wordt dan gereturned
    random_code = []
    for x in range(0, 4):
        random_code.append(kleuren[random.randrange(0, 6)])
    return random_code


# gegenereerd de code
De_Code = Random_Code_Generator(kleuren)
print(De_Code)


def Alle_Mogelijkheden(kleuren):
    # maakt een lijst met alle kleuren combinaties met dubbele letters voor een codecombinatie met een lengte van 4
    # door itertools.product te gebruiken en die om te zetten naar een lijst en die te returnen
    y = itertools.product(kleuren, repeat=4)
    combos = list(y)
    return combos



def Code_Gebruiker():
    # maakt een lijst met de input van de gebruiker
    # door om een input te vragen en die om te zetten in en lijst en die te returnen
    guess = input('Voer een code in: ')
    antwoord = list(guess)
    return antwoord



def Code_Algoritme():
    # maakt een lijst met de input van het algoritme
    # door de eerste combinatie uit de Alle_Mogelijkheden lijst te pakken met de index 0 ([0]) en die om te zetten in en list en die te returnen
    guess = Alle_Mogelijkheden(kleuren)[0]
    antwoord = list(guess)
    return antwoord



def Checken(guess, De_Code):
    # kijkt hoeveel kleuren op de juist positie staan (aantal_zwarte) en hoeveel er op de verkeerde plaats staan (aantal_wit) en die twee variable in een lijst te returnen
    aantal_zwart = 0
    aantal_wit = 0
    kleuren_in_code = 0
    resultaat = []

    for i in range(0, 4):
        # loop die van 0 tot 4 gaat voor de index
        if guess[i] == De_Code[i]:
        # als de kleur van de guess en van de gegenereerde code (De_Code) gelijk zijn dan is aantal_zwart + 1
            aantal_zwart += 1
    for x in kleuren:
        # loop die alle kleuren in de kleuren lijst af gaat
        kleuren_in_code += min(De_Code.count(x), guess.count(x))
        # kijkt hoeveel keer de kleur in de gegenereerde code voorkomt en de guess, en pakt daarvan de kleinste want als er een aantal groter is dan de ander dan is de kleinere aantal
        # gelijk voor bijde codes, kleuren_in_code is alle kleuren die over een komden dus het aantal zwarte pinnen zitter er ook bij
        aantal_wit = kleuren_in_code - aantal_zwart
        # het aantal zwarte pinnen wordt van het aantal kleuren_in_code afgehaald zodat je het aantal witte pinnen overhoudt

    # het aantal van zwart en wit worden in een lijst gedaan en die wordt gereturned
    resultaat.append(aantal_zwart)
    resultaat.append(aantal_wit)
    return resultaat



def Evalueer_Mogelijke_Combinaties(De_Code, alle_mogelijkheden, guess_index):
    aantal = 0
    aantal_voor_eerste_gok = 0
    while aantal < 10:
        #er wordt na elke beurt 1 bij aantal opgeteld zodat je maar 10 beurten hebt
        if aantal_voor_eerste_gok == 0:
            guess = alle_mogelijkheden[guess_index]
        else:
            guess = alle_mogelijkheden[0]
        # voor de eerste gok wordt de guess_index gebruikt, dit is zodat de andere algoritmes hun index als eerste gok kunnen doen en daarna de eerste uit de kleirere lijst

        feedback = Checken(guess, De_Code)

        print(guess)
        print(feedback)
        alle_overige_mogelijkheden = []

        if Checken(guess, De_Code) == [4, 0]:
        # als de gok gelijk is aan [4, 0] (4 zwarte pinnen) dan is de gok goed en stopt de loop
            print('HOERA! Code gekraakt! ')
            break

        for code in alle_mogelijkheden[1:]:
            zwarte_pinnen = Checken(guess, code)[0]
            witte_pinnen = Checken(guess, code)[1]
        # alle combinaties behalve de eerste wordt naar het aantal witte en zwarte pinnen gekeken, als het aantal zwart een aantal wit van de combinatie gelijk
        # is aan het aantal zwart en aantal wit van de gok dan word die combinatie in de lijst alle_overige_mogelijkheden toegevoegt

            if zwarte_pinnen == feedback[0] and witte_pinnen == feedback[1]:
                alle_overige_mogelijkheden.append(code)

        alle_mogelijkheden = alle_overige_mogelijkheden
        # de inhoud van alle_mogelijheden wordt het zelfde als alle_overige_mogelijkheden
        aantal += 1
        aantal_voor_eerste_gok += 1



def Worst_Case_Algoritme():
    #dictionary met alle mogelijke uitkomsten van Checken()
    alle_score_mogelijkheden = {
        "[0, 0]": 0,
        "[0, 1]": 0,
        "[0, 2]": 0,
        "[0, 3]": 0,
        "[0, 4]": 0,
        "[1, 0]": 0,
        "[1, 1]": 0,
        "[1, 2]": 0,
        "[1, 3]": 0,
        "[2, 0]": 0,
        "[2, 1]": 0,
        "[3, 0]": 0,
        "[4, 0]": 0

    }

    beste_eerste_gok = []
    for y in range(len(Alle_Mogelijkheden(kleuren))):
    # y gaat van 0 tot de lengte van de lijst ALle_Mogelijkheden, (1296)

        for x in Alle_Mogelijkheden(kleuren):
        # x gaat alle combinaties van Alle_Mogelijkheden af

            feedback = Checken(x, Alle_Mogelijkheden(kleuren)[y])
            # de loop zorgt voor het aantal wit en zwarte pinnen van ALle_Mogelijkheden[y]

            for i in alle_score_mogelijkheden:
            # i gaat door alles in de dictionary

                if f"{feedback}" == i:
                    alle_score_mogelijkheden[i] += 1
                # als de feedback gelijk is aan iets dat in de dictionary staat dan wordt daarbij +1 gedaan

        all_score_value = alle_score_mogelijkheden.values()
        grootste_score = max(all_score_value)
        # de grootste variabele (grootste_score) uit de dictionary wordt in de beste_eerste_gok lijst gezet

        beste_eerste_gok.append(grootste_score)
        for j, value in alle_score_mogelijkheden.items():
            alle_score_mogelijkheden[j] = 0
        # alle variabele in de dictionary wordt terug naar 0 gezet voor de volgende combinatie

    kleinste_gok = min(beste_eerste_gok)
    index = beste_eerste_gok.index(kleinste_gok)
    # de index van het kleinste getal wordt gereturned
    return index



def Eigen_Algoritme():
    # gaat alle combinaties af en vergelijkt die met alle combinaties en telt alle [0, 0] en de combinatie met de minste [0, 0], die index wordt gereturned
    beste_eerst_poging = []
    aantal_list = [1000]
    # aantal_list heeft 1000 zodat bij de eerste loop het resultaat sowieso vervangt

    for y in range(len(Alle_Mogelijkheden(kleuren))):
        # y gaat van 0 tot de lengte van de lijst ALle_Mogelijkheden, (1296)

        aantal = 0
        for x in Alle_Mogelijkheden(kleuren):
        # x gaat alle combinaties van Alle_Mogelijkheden af

            feedback = Checken(x, Alle_Mogelijkheden(kleuren)[y])
            # de loop zorgt voor het aantal wit en zwarte pinnen van ALle_Mogelijkheden[y]

            if feedback == [0, 0]:
                aantal += 1
            # als de feedback 0, 0 is dan wordt aantal + 1

        if aantal <= aantal_list[0]:
        # als het aantal [0, 0] van de combinatie kleiner is dan het aantal in de lisjt aantal_list
        # dan wordt de list gecleared en wordt het lagere aantal toegevoegt
        # de lijst met de index wordt ook gecleared en de nieuwe index wordt toegevoegt en op het eind gereturned
            aantal_list.clear()
            beste_eerst_poging.clear()
            aantal_list.append(aantal)
            beste_eerst_poging.append(y)
    return beste_eerst_poging[0]



input_gebruiker = input('(1) zelf of (2) computer: ')
# vraagt om een input voor welke keuze de gebuiker wilt
aantal = 0
if input_gebruiker == '1':
    while aantal != 10:
        x = Checken(Code_Gebruiker(), De_Code)
        # vraagt de gebruiker om een code en geeft de score van de code
        print(x)
        if x == [4, 0]:
            print('HOERA! Code gekraakt! ')
            # als de gok gelijk is aan [4, 0] (4 zwarte pinnen) dan is de gok goed en stopt de loop
            break
        aantal += 1
        # aantal wordt na elke gok +1 en als het aantal 10 is dan stop het spel

elif input_gebruiker == '2':
    input_gebruiker2 = input('(1) Simple_Algoritme, (2) Worst_Case_Algoritme, (3) Eigen_Algoritme. ')
    # als de gebruiker 2 kiest dan krijgt hij nog 3 opties voor de verschillende algoritmes
    if input_gebruiker2 == '1':
        # als de gebruiker 1 kiest dan activeert hij de Simple_Algoritme
        Checken(Code_Algoritme(), De_Code)
        Evalueer_Mogelijke_Combinaties(De_Code, Alle_Mogelijkheden(kleuren), 0)

    elif input_gebruiker2 == '2':
        # als de gebruiker 2 kiest dan activeert hij de Worst_Case_Algoritme
        print('Computer is guessing the code. ')
        Evalueer_Mogelijke_Combinaties(De_Code, Alle_Mogelijkheden(kleuren), Worst_Case_Algoritme())

    elif input_gebruiker2 == '3':
        # als de gebruiker 3 kiest dan activeert hij de Eigen_Algoritme
        print('Computer is guessing the code. ')
        Evalueer_Mogelijke_Combinaties(De_Code, Alle_Mogelijkheden(kleuren), Eigen_Algoritme())

    else:
        # als de gebruiker iets anders dan 1, 2, of 3 kiest dan activeert hij de niks en wordt er 'Error' geprint
        print('Error ')

