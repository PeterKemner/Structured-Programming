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

def All_Possible_Combos(kleuren):
    y = itertools.product(kleuren, repeat=4)
    combos = list(y)
    return combos

def Checken():
    aantal_zwart = 0
    aantal_wit = 0
    kleuren_in_code = 0
    pogingen = 0
    while pogingen != 10:
        x = 0
        print(All_Possible_Combos(kleuren))
        code_van_computer = All_Possible_Combos(kleuren)[x]
        print(code_van_computer)
        for i in range(0, 4):
            if code_van_computer[i] == De_Code[i]:
                aantal_zwart += 1
        for kleur in kleuren:
            kleuren_in_code += min(De_Code.count(kleur), code_van_computer.count(kleur))
            aantal_wit = kleuren_in_code - aantal_zwart
        resultaat = [aantal_zwart, aantal_wit]
        print(resultaat)

        if resultaat == [0, 0]:
            kleuren.remove(kleuren[0])
        elif resultaat == [4, 0]:
            print('Code gekraakt! ')
            break
        else:
            x += 1
        resultaat.clear()
        aantal_zwart = 0
        aantal_wit = 0
        kleuren_in_code = 0
        print(kleuren)
        pogingen += 1
        print(len(All_Possible_Combos(kleuren)))

Checken()