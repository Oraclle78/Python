color = {
    "clear": "\033[m",
    "green": "\033[1;32m",
    "red": "\033[1;31m",
    "blue": "\033[1;34m",
    "yellow": "\033[4:33m",
}
valor = float(input("Qual o valor do produto R$:"))
pagamento = int(
    input(
        "Escolha a forma de Pagamento:\n{}1 - Á Vista no Dinheiro ou Cheque\n"
        "2 - Á Vista no Cartão\n3 - Em até 2x no Cartão\n4 - 3x ou Mais no Cartão{}\n{}Opção:{}".format(
            color["blue"], color["clear"], color["yellow"], color["clear"]
        )
    )
)
if pagamento == 1:
    vfinal = valor - (valor / 100) * 10
    print(
        "Voçê escolheu pagar á Vista no Dinheiro ou Cheque e teve {}10%{} de desconto e vai pagar {}R${:.2f}{}".format(
            color["blue"], color["clear"], color["blue"], vfinal, color["clear"]
        )
    )
elif pagamento == 2:
    vfinal = valor - (valor / 100) * 5
    print(
        "Voçê escolheu pagar á Vista no Cartão e teve {}5%{} de desconto e vai pagar {}R${:.2f}{}".format(
            color["blue"], color["clear"], color["blue"], vfinal, color["clear"]
        )
    )
elif pagamento == 3:
    parcela = valor / 2
    print(
        "Voçê escolheu pagar em 2x de {}R${:.2f}{} e o total a pagar será de {}R${:.2f}{}".format(
            color["green"],
            parcela,
            color["clear"],
            color["blue"],
            valor,
            color["clear"],
        )
    )
elif pagamento == 4:
    vezes = int(
        input(
            (
                "Em quantas Vezes deseja parcelar, {}Max 24x:{}".format(
                    color["green"], color["clear"]
                )
            )
        )
    )
    vfinal = valor + (valor / 100) * 20
    if vezes > 2 and vezes <= 24:
        parcela = (valor + (valor / 100) * 20) / vezes
        print(
            "Voçê optou por parcelar em {}{}x{} de {}R${:.2f}{} haverá um acréscimo de {}20%{},"
            "e irá pagar {}R${:.2f}{}".format(
                color["green"],
                vezes,
                color["clear"],
                color["blue"],
                parcela,
                color["clear"],
                color["green"],
                color["clear"],
                color["blue"],
                vfinal,
                color["clear"],
            )
        )
    else:
        print("{}Quantidde de Parcela inválida!{}".format(color["red"], color["clear"]))
else:
    print("{}Opção Inválida!!{}".format(color["red"], color["clear"]))
print("=-" * 20)
