n=int(input('cat'))
for ran in range(1,n+1):
    for col in range(1,n+1):
        print(ran*col, end="\t")
    print()
