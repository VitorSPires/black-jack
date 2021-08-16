import ascii
import variables as var
import random
import os

print(ascii.logo)

input("Pressione ENTER para iniciar o jogo\n")

while True:

    var.computer.clear()
    var.player.clear()
    var.more = "s"
    var.end = False

    os.system('cls' if os.name == 'nt' else 'clear')

    var.player.append(random.choice(var.cards))
    if 11 in var.player:
        var.player.pop(-1)
        var.player.append(int(input("Você recebeu um A, deseja que seu valor seja 1 ou 11?: ")))

    var.computer.append(random.choice(var.cards))

    while var.more == 's':

        print(ascii.logo)

        var.player.append(random.choice(var.cards))
        if var.player[-1] == 11:
            var.player.pop(-1)
            var.player.append(int(input("Você recebeu um A, deseja que seu valor seja 1 ou 11?: ")))

        print(f"\nCartas do dealer: {var.computer}",
            f"\nTotal: {sum(var.computer)}",
            f"\n\n{'-' * 20}",
            f"\n\nsuas cartas: {var.player}",
            f"\nTotal: {sum(var.player)}\n")

        if sum(var.player) > 20 or sum(var.computer) > 20:
            var.end = True
            var.more ="n"
        else:
            var.more = input("\nDeseja pegar outra carta? ( S | N): ").lower()

        if sum(var.computer) <= 17 and len(var.computer) <= 5 and var.end == False:
            var.computer.append(random.choice(var.cards))
            if var.computer[-1] == 11:
                if sum(var.computer[:-1]) < 11:
                    var.computer.append(11)
                else:
                    var.player.pop(-1)
                    var.computer.append(1)

        os.system('cls' if os.name == 'nt' else 'clear')

    while sum(var.computer) <= 17 and len(var.computer) <= 5 and var.more == "n" and var.end == False:
        var.computer.append(random.choice(var.cards))
        if var.computer[-1] == 11:
            if sum(var.computer[0:-1]) < 11:
                var.computer.append(11)
            else:
                var.computer.append(1)

    print(ascii.logo)

    print(f"\nCartas do dealer: {var.computer}",
            f"\nTotal: {sum(var.computer)}",
            f"\n\n{'-' * 20}",
            f"\n\nsuas cartas: {var.player}",
            f"\nTotal: {sum(var.player)}\n")

    if sum(var.player) > 21 and sum(var.computer) > 21:
        print("Empate")
    elif sum(var.player) > 21 and sum(var.computer) <= 21:
        print("Computador venceu")
    elif sum(var.player) <= 21 and sum(var.computer) > 21:
        print("Você venceu!")
    elif sum(var.player) == sum(var.computer):
        print("Empate")
    else:
        if sum(var.player) > sum(var.computer):
            print("Você venceu!")
        else:
            print("Computador venceu")

    input("\nPressione ENTER para jogar de novo")

    print(ascii.logo)