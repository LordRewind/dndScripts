import random

# Weapon 1
weapon1Name = "Pickaxe"
numberOfDamageDice1 = 1
sizeOfDamageDice1 = 8
minimumCrit1 = 20
critMulti1 = 4

# Weapon 2
weapon2Name = "Falchion"
numberOfDamageDice2 = 2
sizeOfDamageDice2 = 4
minimumCrit2 = 18
critMulti2 = 2

# General Adjustments /salute
damageBonus = 20
toHitBonus = 20
# Set this to a target AC for crit confirmation purposes
targetAC = 10
confirmCrits = 1

# For calculation process
executions = 100000

# DO NOT TOUCH THESE
weapon1Peaks = 0
weapon1DoublePeaks = 0
weapon1TriplePeaks = 0
weapon2Peaks = 0
weapon2DoublePeaks = 0
weapon2TriplePeaks = 0
weapon1CritCount = 0
weapon2CritCount = 0
weapon1CritAvg = 0
weapon1CritSum = 0
weapon2CritAvg = 0
weapon2CritSum = 0
damageSum1 = 0
damageSum2 = 0
runs = 0

peak1 = ((numberOfDamageDice1*sizeOfDamageDice1) + damageBonus)*critMulti1
peak2 = ((numberOfDamageDice2*sizeOfDamageDice2) + damageBonus)*critMulti2

if peak1 < peak2:
    targetPeak = peak1
else:
    targetPeak = peak2

while runs < executions:
    hit = random.randint(1, 20)
    confirmHit = random.randint(1, 20) + toHitBonus

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
            if confirmHit < targetAC:
                multi = 1
        diceSum1 = diceSum1*multi
        if multi > 1:
            weapon1CritCount = weapon1CritCount + 1
            weapon1CritSum = weapon1CritSum + diceSum1

    multi = critMulti2
    if hit >= minimumCrit2:
        if confirmCrits:
            if confirmHit < targetAC:
                multi = 1
        diceSum2 = diceSum2*multi
        if multi > 1:
            weapon2CritCount = weapon2CritCount + 1
            weapon2CritSum = weapon2CritSum + diceSum1

    print("Weapon 1={0}\t\t\tWeapon 2={1}".format(diceSum1, diceSum2))

    if diceSum1 >= targetPeak:
        weapon1Peaks = weapon1Peaks + 1

    if diceSum1 >= (targetPeak*2):
        weapon1DoublePeaks = weapon1DoublePeaks + 1

    if diceSum1 >= (targetPeak*3):
        weapon1TriplePeaks = weapon1TriplePeaks + 1

    if diceSum2 >= targetPeak:
        weapon2Peaks = weapon2Peaks + 1

    if diceSum2 >= (targetPeak * 2):
        weapon2DoublePeaks = weapon2DoublePeaks + 1

    if diceSum2 >= (targetPeak * 3):
        weapon2TriplePeaks = weapon2TriplePeaks + 1

    damageSum1 = damageSum1 + diceSum1
    damageSum2 = damageSum2 + diceSum2

    runs = runs+1

weapon1Avg = damageSum1/executions
weapon2Avg = damageSum2/executions

weapon1CritAvg = weapon1CritSum / weapon1CritCount
weapon2CritAvg = weapon2CritSum / weapon2CritCount

print("{0} Executions yields:".format(executions))

print("{2} Damage at {0} or higher count={1}".format(targetPeak, weapon1Peaks, weapon1Name))
print("{2} Damage at {0} or higher count={1}".format(targetPeak, weapon2Peaks, weapon2Name))

if weapon1DoublePeaks > 0 or weapon2DoublePeaks > 0:
    print("{2} Damage at {0} or higher count={1}".format(targetPeak*2, weapon1DoublePeaks, weapon1Name))
    print("{2} Damage at {0} or higher count={1}".format(targetPeak*2, weapon2DoublePeaks, weapon2Name))

if weapon1TriplePeaks > 0 or weapon2TriplePeaks > 0:
    print("{2} Damage at {0} or higher count={1}".format(targetPeak*3, weapon1TriplePeaks, weapon1Name))
    print("{2} Damage at {0} or higher count={1}".format(targetPeak*3, weapon2TriplePeaks, weapon2Name))

print("{1} average damage={0}".format(round(weapon1Avg, 2), weapon1Name))
print("{1} average damage={0}".format(round(weapon2Avg, 2), weapon2Name))

print("{1} average critical damage={0}".format(round(weapon1CritAvg, 2), weapon1Name))
print("{1} average critical damage={0}".format(round(weapon2CritAvg, 2), weapon2Name))