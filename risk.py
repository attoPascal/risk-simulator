from sys import argv
from random import randrange

def roll_dice():
    return randrange(1,7)

def attack(units):
    if units >= 3:
        cast = [roll_dice(), roll_dice(), roll_dice()]
    elif units == 2:
        cast = [roll_dice(), roll_dice()]
    else:
        cast = [roll_dice()]

    return sorted(cast, reverse=True)

def defend(units):
    if units >= 2:
        cast = [roll_dice(), roll_dice()]
    else:
        cast = [roll_dice()]

    return sorted(cast, reverse=True)

def play(attackers, defenders, verbose=False):
    if verbose:
        print("Attacker has", attackers, "units")
        print("Defender has", defenders, "units")
        print()

    while attackers > 0 and defenders > 0:
        the_attack = attack(attackers)
        the_defense = defend(defenders)

        if verbose:
            print(the_attack, "vs.", the_defense)

        while len(the_attack) > 0 and len(the_defense) > 0:
            if the_attack.pop(0) > the_defense.pop(0):
                defenders -= 1
                if verbose:
                    print("Defender unit dies ({} left)".format(defenders)) 
            else:
                attackers -= 1
                if verbose:
                    print("Attacker unit dies ({} left)".format(attackers)) 

        if verbose:
            print()

    if attackers > 0:
        if verbose:
            print("Attacker wins with", attackers, "units left")
        return attackers
    else:
        if verbose:
            print("Defender wins with", defenders, "units left")
        return -defenders

def main():
    attackers = int(argv[1])
    defenders = int(argv[2])
    play(attackers, defenders, True)

if __name__ == '__main__':
    main()
