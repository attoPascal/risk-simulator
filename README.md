# Risk Simulator
Risk Simulator is a small Python3 script for simulating the dice rolls in the board game Risk.

## Usage

### risk.py

`risk.py` takes two arguments: the number of attacking units and the number of defending units. It will then simulate the battle with all its dice rolls.

Example:

```shell
$ python3 risk.py 3 2
```

could create the following output:

```shell
Attacker has 3 units
Defender has 2 units

[6, 2, 1] vs. [4, 3]
Defender unit dies (1 left)
Attacker unit dies (2 left)

[4, 1] vs. [2]
Defender unit dies (0 left)

Attacker wins with 2 units left
```

### riskstats.py

`riskstats.py` will simulate a specified number of independent games and output the statistical results.

To simulate 50 games where the attacker has 15 units and the defender has 12 units:

```shell
$ python3 riskstats.py 15 12 50
Games won:
Attacker: 38	(76.0%)
Defender: 12	(24.0%)
```

### riskstrategy.py

`riskstrategy.py` takes the number of the opponent's units, the number of units you want to win with and the desired probability as arguments.

```shell
$ python3 riskstrategy.py 15 5 80
Objective:
win against 15 opposing units
with at least 5 units left
with a probability of at least 80 percent

Attack with at least 22 units
```

The latter two arguments can be omitted and will be initialized with default values:

```shell
$ python3 riskstrategy.py 10
Objective:
win against 10 opposing units
with at least 1 units left
with a probability of at least 75 percent

Attack with at least 13 units
```