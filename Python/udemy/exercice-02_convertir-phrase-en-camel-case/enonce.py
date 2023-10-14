phrase = 'Phrase en camel case'
l = phrase.split(' ')

res = l[0].lower()

for i, mot in enumerate(l, 1):
    if i > 1:
        res += mot.capitalize()

print(res)


