# Check how many vowels are present in a string.
n=input()
check=['a','e','i','o','u']
count=0
inp="anitha"
for i in n:
    if(i in check):
        count+=1
print(count)
