# comparar_cnpjs_simples.py

# Abrir os arquivos das duas bases
with open("base1.txt", "r") as f1:
    base1 = set(line.strip() for line in f1 if line.strip())

with open("base2.txt", "r") as f2:
    base2 = set(line.strip() for line in f2 if line.strip())

# CNPJs que estão na Base 1 e não estão na Base 2
unicos_base1 = sorted(base1 - base2)

# CNPJs que estão na Base 2 e não estão na Base 1
unicos_base2 = sorted(base2 - base1)

# Mostrar na tela
print("CNPJs que estão na Base 1 e não estão na Base 2:")
for cnpj in unicos_base1:
    print(cnpj)

print("\nCNPJs que estão na Base 2 e não estão na Base 1:")
for cnpj in unicos_base2:
    print(cnpj)

# Salvar em arquivos
with open("unicos_base1.txt", "w") as f:
    f.write("\n".join(unicos_base1))

with open("unicos_base2.txt", "w") as f:
    f.write("\n".join(unicos_base2))

print("\nArquivos TXT gerados: unicos_base1.txt e unicos_base2.txt")