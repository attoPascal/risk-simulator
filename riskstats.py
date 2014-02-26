from sys import argv
from risk import play

attacker_units = int(argv[1])
defender_units = int(argv[2])
games = int(argv[3])

attacker_wins = 0
defender_wins = 0

for i in range(games):
    game = play(attacker_units, defender_units)

    if (game > 0):
        attacker_wins += 1
    else:
        defender_wins += 1

print("Games won:")
print("Attacker: {}\t({}%)".format(attacker_wins, 100*attacker_wins/games))
print("Defender: {}\t({}%)".format(defender_wins, 100*defender_wins/games))