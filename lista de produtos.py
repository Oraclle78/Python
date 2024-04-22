produtos = (
    "Lápis",
    "1.75",
    "Borracha",
    "2.00",
    "Caderno",
    "15.90",
    "Estojo",
    "25.00",
    "Transferidor",
    "4.20",
    "Compasso",
    "9.99",
    "Mochila",
    "120.32",
    "Canetas",
    "22.30",
    "Livro",
    "34.90",
)
print("=" * 50)
print("{:^50}".format("LISTAGEM DE PREÇOS"))
print("=" * 50)
prod = 0
valor = 1
for c in range(0, 9):
    print(f"{produtos[prod]} {'.' * (30-len(produtos[prod]))} R$ {produtos[valor]}")
    prod += 2
    valor += 2
print("=" * 50)
