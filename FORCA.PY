import random


def escolher_palavra():
    palavras = ['telegram', 'chatgpeteco', 'computador', 'biscoito', 'internet', 'agua']
    return random.choice(palavras)


def jogar_forca(palavra):
    palavra = palavra.lower()
    letras_corretas = set()
    tentativas = 6
    letras_tentadas = set()

    while True:

        palavra_escondida = ''.join([letra if letra in letras_corretas else '_' for letra in palavra])


        print(f"\nPalavra: {palavra_escondida}")
        print(f"Tentativas restantes: {tentativas}")
        print(f"Letras tentadas: {' '.join(letras_tentadas)}")


        if palavra_escondida == palavra:
            print("Parabéns, você ganhou!")
            break


        if tentativas == 0:
            print(f"Você perdeu! A palavra era '{palavra}'.")
            break


        tentativa = input("Digite uma letra ou adivinhe a palavra: ").lower()


        if len(tentativa) == 1 and 'a' <= tentativa <= 'z':
            if tentativa in letras_tentadas:
                print("Você já tentou esta letra. Tente outra.")
            elif tentativa in palavra:
                letras_corretas.add(tentativa)
                letras_tentadas.add(tentativa)
                print("Letra correta!")
            else:
                letras_tentadas.add(tentativa)
                tentativas -= 1
                print("Letra incorreta!")
        elif len(tentativa) > 1 and tentativa == palavra:
            print("Você acertou a palavra!")
            break
        else:
            print("Entrada inválida. Por favor, digite uma letra válida ou adivinhe a palavra.")


def main():
    print("Bem-vindo ao jogo da Forca!")
    palavra = escolher_palavra()
    jogar_forca(palavra)


if __name__ == "__main__":
    main()
