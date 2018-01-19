# 'A' --> 'A' * multiplier * 1
# 'E' --> 'E' * multiplier * 2
# 'I' --> 'I' * multiplier * 3
# 'O' --> 'O' * multiplier * 4
# 'U' --> 'U' * multiplier * 5
VOWELS = ['A','E','I','O','U']
def LongShout(word, multiplier):
    word = word.upper()
    count = 1
    for vowel in VOWELS:
        long_vowels = vowel * multiplier * count
        word = word.replace(vowel, long_vowels)
        count += 1
    return word

print LongShout('COOKIE',4)
print LongShout('Ivanna',7)
