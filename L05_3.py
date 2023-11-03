note = [7, 6, 8, 10, 5, 6, 2 , 1 , 5, 7]
l=len(note)
l//=2
for i in range(l):
    if(i==0):
        note[i],note[i-1] = note[i-1], note[i]
    else:
        note[i], note[-(i+1)] = note[-(i+1)], note[i]
print(note)
