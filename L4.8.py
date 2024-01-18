import random
r1=random.randint(0,20)
incercari=0
ng=-1
ng= int(ng)
while(r1!=ng):
    ng=input("Introdu numar:")
    ng= int(ng)
    incercari+=1
    if(ng>r1):
        print("Prea mare!")
    if(ng<r1):
        print("Prea mic!")
    if(ng==r1):
        print("castigator")
    
