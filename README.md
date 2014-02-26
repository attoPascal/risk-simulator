# Risk Simulator
Risk Simulator is a small Python3 script for simulating the dice rolls in the board game Risk.

## Usage

### risk.py

`risk.py` takes two arguments: the number of attacking units and the number of defending units. It will then simulate the battle with all its dice rolls.

Example:

```shell
python3 risk.py 3 2
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