from sys import argv
from risk import play

DEFENDER_UNITS = int(argv[1])
WINNING_UNITS = int(argv[2]) if len(argv) > 2 else 1
PROBABILITY = int(argv[3]) if len(argv) > 3 else 75

print("Objective:")
print("win against", DEFENDER_UNITS, "opposing units")
print("with at least", WINNING_UNITS, "units left")
print("with a probability of at least", PROBABILITY, "percent")
print()

my_units = 1

while True:
    success = 0

    for i in range(100):
        game = play(my_units, DEFENDER_UNITS)

        if (game >= WINNING_UNITS):
            success += 1
    
    if success >= PROBABILITY:
        break
    else:
        my_units += 1

print("Attack with at least", my_units, "units")
