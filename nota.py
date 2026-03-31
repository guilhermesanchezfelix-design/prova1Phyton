
soma_nota = 0
for i in range(1, 4):
    nota_bimestre = float(input(f"digite a nota do {i}º bimestre:"))
    soma_nota += nota_bimestre

media = soma_nota / 3
print(f"a media final é {media: .2f}")

    
