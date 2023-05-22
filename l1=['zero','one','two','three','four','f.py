print("Name:Ritik\nROllno:25513\nBranch:ECS\n")
l1=['zero','one','two','three','four','five','six','seven',
    'eight','nine','ten','eleven','twelve','thirteen',
    'fourteen','fiveteen','sixteen','seventeen','eighteen','nineteen']

l2=['  ','  ','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']

n= int(input("enter the number"))
if(n<=19):
    print(l1[n])
elif(n%10==0):
    print(l2[n//10])
else:
    print(l2[n//10]+'  '+l1[n%10])

