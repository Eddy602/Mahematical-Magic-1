num=int(input("Enter a number"))
 
digits=len(str(num))
results=0

temp=num
while temp>0:
    lastvalue=temp%10
    results +=lastvalue**digits
    temp//=10

if num== results:
    print(num," is an armstrong number")
else:
     print(num," is  not an armstrong number")   