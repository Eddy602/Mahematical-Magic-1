def factors(n):
    print("the factorial of ",n,"are")
    for x in range(1, n+1):
        if n%x ==0:
            print(x)
num=int(input("Enter a Number"))   
factors(num)        
