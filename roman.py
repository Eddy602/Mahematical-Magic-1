def roman(romanum):
    #DICTIONARY
    romans={'M':1000, 'D':500 ,'C':100, '1':50, 'X':10, 'V':5}
    resultint=0 
    for x in range(0, len(romanum)-1):
          if romans[romanum[x]]<romans[romanum[x+1]]:
               resultint-=romans[romanum[x]]
          else:
               resultint+=romans[romanum[x]]  
          return resultint+romans[romanum[-1]]  
num=input('enter roman number')  
print(roman(num))   
print('The inter value for',num,"romanum")  