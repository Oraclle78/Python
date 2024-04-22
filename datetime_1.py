color = {"clear": "\033[m", "blue": "\033[1;34m"}
from datetime import date

print("-=" * 20)
ano = int(input("Digite o seu Ano de Nascimento:"))
anoa = date.today().year
categoria = "{}MASTER{}".format(color["blue"], color["clear"])
if anoa - ano <= 9:
    categoria = "MIRIM"
elif anoa - ano > 9 and anoa - ano <= 14:
    categoria = "{}INFANTIL{}".format(color["blue"], color["clear"])
elif anoa - ano > 14 and anoa - ano <= 19:
    categoria = "{}JUNIOR{}".format(color["clear"], color["clear"])
elif anoa - ano > 19 and anoa - ano <= 20:
    categoria = "{}SÊNIOR{}".format(color["blue"], color["clear"])
print("Você tem {} anos e sua categoria é:".format(anoa - ano), categoria, "!")
print("-=" * 20)
 # type: ignore