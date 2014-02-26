from sys import argv
from risk import play

def main():
    einheiten = 1
    iterations = int(argv[1])

    angreifer_wins = 0
    verteidiger_wins = 0

    while einheiten < 10:
        for i in range(iterations):
            game = play(einheiten, einheiten)

            if (game > 0):
                angreifer_wins += 1
            else:
                verteidiger_wins += 1
        
        print("Bei", einheiten, "Einheiten:")
        print("Angreifer:\t", angreifer_wins)
        print("Verteidiger:\t", verteidiger_wins)
        print()

        angreifer_wins = 0
        verteidiger_wins = 0
        einheiten += 1

if __name__ == '__main__':
    main()