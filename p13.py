#replace the elements in an array with avg of max and min elements:
#sample input is 0:
#13 2 67 20 68
#68+2=70
#35 35 35 35 35
my_list=list(map(int,input().split()))
sum=0
maxi=my_list[0]
min=my_list[0]
for i in range(len(my_list)):
    if(my_list[i]>maxi):
        maxi=my_list[i]
print(maxi)

for i in range(len(my_list)):
    if(my_list[i]<min):
        min=my_list[i]
avg=(maxi+min)//2
for i in range(len(my_list)):
    my_list[i]=avg
print(my_list)