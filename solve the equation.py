n=int(input())
f=0
for i in range(1,n):
    for j in range(1,n):
        for k in range(1,n):
            if(i**2+j**2+k**2+i*j+j*k+k*i)==n:
                print(i,j,k)
                f=1
if f==0:
   print("NP")                
                

