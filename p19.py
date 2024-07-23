# pssword verifier
# mr.x is trying to create a new password for his instagram account. these are the required conditions for creating a new password
#condition1:minimum length is 8,maximum length is 15
#condition2:only @,/ are allowed in a password(these are must)
#condition3:no space are allowed
#condition4:only alphanumerics are allowed
#you are supposed to print weak if length is exact 8,medium:length is between 8 to 12,strong:if length is between 12 to 15.  
password=input()
n=len(password)
if(n<8):
    print("follow the conditions")
elif(n>=8 and n<12):
  print(n)