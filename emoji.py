from random import randint
from time import sleep
from emoji import emojize

num = randint(0, 5)
print("-=-" * 20)
print("Tente advinhar em qual número eu pensei")
print("-=-" * 20)
x = int(input("Tente advinhar digitando um número de 0 a 5:"))
print(emojize("PROCESSANDO....:stopwatch:", language="alias"))
sleep(2)
if x > 5:
    print("O número tem que estar entre 0 e 5!")
if num == x:
    print(
        emojize(
            "Parabéns voce acertou!!! :squinting_face_with_tongue:", language="alias"
        )
    )
else:
    print(
        emojize(
            "Não foi desta vez, tente denovo!! Eu pensei no número {} e não no número {} :sleepy_face:".format(
                num, x
            ),
            language="alias",
        )
    )
print("-=-" * 20)