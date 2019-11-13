numeros = [i for i in range(100)]
# numeros = [0,1,2,3,4,5,]
print(numeros)


vector = []
for i in numeros:
    if i%2 == 0:  # 1 0
        j = i**2
        vector.append(j)
    else:
        j = i*5
        vector.append(j)
print(vector)

vector_2 = [i**2 if i%2==0 else i*5 for i in numeros]
print(vector_2)

