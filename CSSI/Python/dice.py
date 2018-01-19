#takes in a list of numbers
import random
def RollManyDungeonsAndDragonsDice(sides):
    total = 0
    for side in sides:
        roll = random.randint(1,side)
        total += roll
    print "You may move " + str(total) + " spaces"

RollManyDungeonsAndDragonsDice([4,3,6])
