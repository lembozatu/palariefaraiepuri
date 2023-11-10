sir=[]
numar=int(input("Introdu numarul:"))
def fac(numar):
    n=1
    for i in range(1,numar+1):
        n=n*i
        sir.append(n)
        print(i,sir[i-1])
fac(numar)
