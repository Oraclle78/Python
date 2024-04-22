while True:
    print("=-" * 20)
    num = int(input("Quer ver a Tabuada de qual valor (-1 para sair): "))
    c = 1
    print("=-" * 20)
    if num == -1:
        break
    while c <= 10:
        print(f"{num}x{c} = {num*c}")
        c += 1
print("Programa TAUADA encerrado. Volte Sempre!")