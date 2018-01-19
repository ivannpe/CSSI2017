import random
die1 = 0
die2 = 0
count = 0
while not(die1 == 6 and die2 == 6):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print "Rolls: {0} {1}".format(die1, die2)
    if die1 == 1 and die2 == 1:
        print "Got Snake Eyes!"
    elif die1 == 6 and die2 == 6:
        print "Got Double Sixes!"
    count += 1
print str(count) + ' Rolls'
