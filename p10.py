#print the element in a particular index,the condition is cyclic printing.(find the element present in the ith index)
#k=20
#70 54 36 72 76 9999 0089        k=20,length=7
#1  2  3  4  5   6    7          index=6
#===================================================
#k=18
#80 70 54 36 77                  k=18,5
#1  2  3   4  5                  idx=3
#===================================================
#k=3
#70 54 36 72 566                 k=3,5
#1  2  3  4   5                  idx=3

my_list=list(map(int,input().split(" ")))
k=int(input())
idx=k%len(my_list)
print(my_list[idx])