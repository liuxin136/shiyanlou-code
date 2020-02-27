b=range(100)
for a in b:
    if a%7==0: 
       continue
    elif a%10==7:
       continue
    elif a//10==7:
        continue
    else:
       print(a)

