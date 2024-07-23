vowel="aeiou"
consonent="bcdefghijklmnpqrstuvwxyz"
count=0
c=0
i="anitha"
inp=i.lower()
for i in inp:
    if(i in vowel):
        count+=1
for i in inp:
    if(i in consonent):
        count+=1
print(count)




