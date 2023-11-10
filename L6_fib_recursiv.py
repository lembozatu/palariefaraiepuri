sir=[0,1]
i=0
numar=int(input("Introdu numarul:"))
def fib(numar,i):
    if(numar<1+2):
        return
    else:
        sir.append(sir[i]+sir[i+1])
        i=i+1
        fib(numar-1,i)
fib(numar,i)
print(sir)
