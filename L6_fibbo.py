sir =[0,1]
numar=int(input("Introdu numarul:"))
if numar==2:
    print(sir)
elif numar==1:
    print(sir[0])
else:
    for i in range(numar-2):
            sir.append(sir[i]+sir[i+1])
    print(sir)
