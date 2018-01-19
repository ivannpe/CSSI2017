
def fizzbuzz():
    for i in range(0,n+1):
        if i % 3 == 0 and i % 5 == 0:
            print 'Fizzbuzz'
        elif i % 3 == 0:
            print 'Fizz'
        elif i % 5 == 0:
            print 'Buzz'
        else:
            print i

def fizzbuzzLoop():
    while True:
        n = input("Pick a number: ")
        fizzbuzz(n)
        response = raw_input("Quit? ")
        if response == 'Quit':
            break
    print 'Goodbye'

fizzbuzzLoop()
