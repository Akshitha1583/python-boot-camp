# Print all the vowels followed by the consonents.
vowel="aeiou"
consonent="bcdfghjklmnpqrstvwxyz"
ans=""
i="hello world"
inp=i.lower()
for i in inp:
    if(i in vowel):
        ans+=i
for i in inp:
    if(i in consonent):
        ans+=i
print()
