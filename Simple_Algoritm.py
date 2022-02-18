import random
import itertools

#bronvermelding:
#https://www.geeksforgeeks.org/randrange-in-python/ voor de random.randrange()
#https://docs.python.org/3/library/itertools.html voor de itertools.product()


kleuren = ['R', 'O', 'Y', 'G', 'C', 'B']


def Random_Code_Generator(kleuren):
    random_code = []
    for x in range(0, 4):
        random_code.append(kleuren[random.randrange(0, 6)])

    return random_code

De_Code = Random_Code_Generator(kleuren)
print(De_Code)


def All_Possible_Combos(kleuren, aantal):
    y = itertools.product(kleuren, repeat=aantal)
    combos = list(y)
    return combos


def Feedback(De_Code, antwoord):
    aantal_zwart = 0
    aantal_wit = 0
    print(antwoord)

    feedback = []

    for j in range(len(De_Code)):
        if antwoord[j] == De_Code[j]:
            aantal_zwart += 1
        elif antwoord[j] in De_Code:
            aantal_wit += 1
    if aantal_zwart == 4:
        print('Virctory Royal! ')
        quit()

    feedback.append(aantal_zwart)
    feedback.append(aantal_wit)
    print(feedback)
    if feedback == [0, 0]:
        kleuren.remove(antwoord[0])


def Evaluatie_Guess():
    antwoord = All_Possible_Combos(kleuren, 4)[0]
    nieuwe_combinaties = []

    letter = f'{antwoord[0]}'

    for x in All_Possible_Combos(kleuren, 4):
        if letter in x:
            nieuwe_combinaties.append(x)

    return nieuwe_combinaties[0]

def Code_Kraken():
    aantal = 0
    lol = 0
    while lol == 0:
        Feedback(De_Code, All_Possible_Combos(kleuren, 4)[0])
        lol = 1
        while aantal != 10:
            Feedback(De_Code, Evaluatie_Guess())
            aantal += 1

def start():
    Random_Code_Generator(kleuren)
    All_Possible_Combos(kleuren, 4)
    Code_Kraken()

start()