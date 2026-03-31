continuar = "sim"

while continuar == "sim":
    continuar = input("voce deseja continuar? (sim/nao): ")

    if continuar == "sim":
        print("voce ainda esta no jogo ")
    elif continuar == "nao":
        print("game over!")
    else:
        print("Opçao invalida. Digite sim ou nao. ")
        continuar = "sim"