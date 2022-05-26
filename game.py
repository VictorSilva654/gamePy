from models.calcular import Calcular

def main() -> None:
    pontos: int = 0
    jogar(pontos)

def jogar(pontos) -> None:
    
    dificuldade = int(input("Informe o nível da dificuldade: (1, 2, 3 ou 4): "))

    calc = Calcular(dificuldade)

    print("Informe o resultado da operação: ")
    calc.mostrar_operacao()

    resultado = int(input())

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f"Você tem {pontos} pontos.")

    continuar = input("Deseja continuar no jogo, sim ou não? ")

    if continuar == "sim":
        jogar(pontos)
    else:
        print("Até a próxima!!")


if __name__ == '__main__':
    main()