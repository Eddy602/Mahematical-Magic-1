def codenum(romanum):
    roman={'010':2, '001':12 ,'1101':13, '0101':50, '1100':6, '01001':5}
    resultint=0 
    for x in range(0, len(romanum)-1):
          if roman [romanum[x]]<roman[romanum[x+1]]:
               resultint-=roman[romanum[x]]
          else:
               resultint+=roman[romanum[x]]  
          return resultint+roman[romanum[-1]]  
num=input('enter a code number')  
print(codenum(num))   
print("the decimal value for",num,"is",codenum(num))  