#find the element that is  present in (k+i)th index. 
my_list=list(map(int,input().split()))
print(my_list)
k=int(input("enter the k input"))
n=int(input("enter the n input"))
if(len(my_list)<k+n):
    print("ERROR")
else:
    for i in range(len(my_list)):
        break
    print(my_list[k+n])