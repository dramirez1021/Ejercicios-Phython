x= [367,4,5,2,56,34,6]
j=0
n= len(x)
i=0
while i < n-1 :
 while j < n-1 :
    if x[j] > x [j + 1]:
        aux =x[j]
        x[j] = x[j + 1]
        x[j+1]= aux

    j += 1
 i +=1
 j=0
print(x)

