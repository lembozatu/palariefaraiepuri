List = [1, 2, 3, 4, 5]
l=len(List)
for i in List:
    if(i==l//2):
        List[i]=int(input("number:"))
List.remove(l)
l=len(List)
print(List,l)
