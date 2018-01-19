word_count = {}
def GetUniqueWords(text):
    #return len(set(text.split()))
    words = text.split()
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    print "Number of times Alice occurs: " + str(word_count['Alice'])
    print "Number of times Wonderland occurs: " + str(word_count['Wonderland'])
    return len(word_count)

def mostFrequent():
    sorted_words = sorted(word_count, key = word_count.get, reverse=True)
    i = 0
    while i < 10:
        word = sorted_words[i]
        print word + ': ' + str(word_count[word])
        i += 1

def leastFrequent():
    sorted_words = sorted(word_count, key = word_count.get)
    i = 0
    while i < 10:
        word = sorted_words[i]
        print word + ': ' + str(word_count[word])
        i += 1
def moreThan100():
    for word in word_count:
        if word_count[word] >= 100:
            print '===== MORE THAN 100 ===='
            print word + ': ' + str(word_count[word])
def main():
    with open('alice_in_wonderland') as alice_file:
        alice_text = alice_file.read()

    print 'Unique words:', GetUniqueWords(alice_text)
    mostFrequent()
    leastFrequent()
    moreThan100()
