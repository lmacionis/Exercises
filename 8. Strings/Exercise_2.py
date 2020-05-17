"""
Modify:

prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print(letter + suffix)

so that Ouack and Quack are spelled correctly.
"""

# My answer
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter in ("O", "Q"):
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)


# Stack owerflow ex 1:
prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
 if letter in ('O','Q'):
  letter+="u"
 print (letter + suffix)


# Stack owerflow ex 2:
prefixes = list('JKLMNP')
prefixes.extend(['Ou', 'Qu'])
suffix = 'ack'
for pref in prefixes:
    print (pref + suffix)