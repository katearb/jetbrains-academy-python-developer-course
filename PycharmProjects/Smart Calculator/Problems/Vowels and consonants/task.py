phrase = str(input())
vowels = 'eyuioa'
conconants = 'qwrtpsdfghjklmnbvcxz'
for s in phrase:
    if s in vowels:
        print('vowel')
    elif s in conconants:
        print('consonant')
    else:
        break
