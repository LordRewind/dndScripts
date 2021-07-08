import random

# Weapon 1
weapon1Name = "Great Sword"
numberOfDamageDice1 = 2
sizeOfDamageDice1 = 6
minimumCrit1 = 19
critMulti1 = 2

# Weapon 2
weapon2Name = "Greataxe"
numberOfDamageDice2 = 1
sizeOfDamageDice2 = 12
minimumCrit2 = 20
critMulti2 = 3

# General Adjustments /salute
damageBonus = 5
toHitBonus = 5
ac = 10
confirmCrits = 1

# For calculation process
executions = 10000
targetPeak = 40
weapon1Peaks = 0
weapon2Peaks = 0
damageSum1 = 0
damageSum2 = 0

runs=0

while runs < executions:
    hit = random.randint(1, 20)

    diceSum1 = 0
    diceSum2 = 0

    y = 0
    while y < numberOfDamageDice1:
        diceSum1 = diceSum1 + random.randint(1, sizeOfDamageDice1)
        y = y+1
    diceSum1 = diceSum1 + damageBonus

    y = 0
    while y < numberOfDamageDice2:
        diceSum2 = diceSum2 + random.randint(1, sizeOfDamageDice2)
        y = y+1
    diceSum2 = diceSum2 + damageBonus

    multi = critMulti1
    if hit >= minimumCrit1:
        if confirmCrits:
            confirmHit = random.randint(1, 20) + toHitBonus
            if confirmHit < ac:
                multi = 1
        diceSum1 = diceSum1*multi

    multi = critMulti2
    if hit >= minimumCrit2:
        if confirmCrits:
            confirmHit = random.randint(1, 20) + toHitBonus
            if confirmHit < ac:
                multi = 1
        diceSum2 = diceSum2*multi

    print("Weapon 1={0}\t\t\tWeapon 2={1}".format(diceSum1, diceSum2))

    if diceSum1 >= targetPeak:
        weapon1Peaks = weapon1Peaks + 1

    if diceSum2 >= targetPeak:
        weapon2Peaks = weapon2Peaks + 1

    damageSum1 = damageSum1 + diceSum1
    damageSum2 = damageSum2 + diceSum2

    runs = runs+1

weapon1Avg = damageSum1/executions
weapon2Avg = damageSum2/executions

print("{2} Damage at {0} or higher count={1}".format(targetPeak, weapon1Peaks, weapon1Name))
print("{2} Damage at {0} or higher count={1}".format(targetPeak, weapon2Peaks, weapon2Name))

print("{1} average damage={0}".format(weapon1Avg, weapon1Name))
print("{1} average damage={0}".format(weapon2Avg, weapon2Name))
