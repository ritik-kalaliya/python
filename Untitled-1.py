print("Name:Ritik\nROllno.:25513\nBranch:ECS\n")

nterms=int(input("enter the number of terms to print"))
n1=0
n2=1
count=0
if nterms <= 0:
    print("please enter a positive number")
elif nterms == 1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence.")
    while count < nterms:
        print(n1,end="\t")
        nth = n1+n2
        n1=n2 
        n2 = nth
        count += 1 
    