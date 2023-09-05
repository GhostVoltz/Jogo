import random

# Lista de palavras para o jogo
palavras = ["fantasma","jogo" ,"carregador","python", "banana", "elefante", "computador", "girafa","maçã", "carro", "cachorro", "montanha", "Me Segue", "tiktok", "anime"]
palavra = "fantasma","jogo" ,"carregador","python", "banana", "elefante", "computador", "girafa","maçã", "carro", "cachorro", "montanha", "Me Segue", "tiktok", "anime"
def escolher_palavra():
    return random.choice(palavras)

def exibir_dica(palavra, letras_corretas):
    dica = ""
    for letra in palavra:
        if letra in letras_corretas:
            dica += letra
        else:
            dica += "_"
    return dica

# Exemplo de uso:
#palavra = "exemplo"
#letras_corretas = ["e", "m", "o"]
#dica = exibir_dica(palavra, letras_corretas)
#print(dica)  # Certifique-se de imprimir a dica para verificar se está funcionando corretamente.

def jogo_adivinhacao():
    palavra_atual = escolher_palavra()
    letras_corretas = ["a","b","c","d","k","Me S","e","f", "j", "c", "p", "b", "e", "c", "g", "m", "c", "c", "m", "m", "s", "t", "a"]
    tentativas = 10

    print("""
  /***************************************
 / *                                    /*
|==*===================================/ *
|  *                                   | *
|  *            BEM-VINDO AO           | *
|  *          JOGO DE ADIVINHAÇÃO      | *
|  *                                   | *
| /**************************************/
|/_____________________________________|/
______________________________________________
|Bem-vindo ao Jogo de Adivinhação de Palavras!|
ππππππππππππππππππππππππππππππππππππππππππππππ
""")

    while tentativas > 0:
        dica = exibir_dica(palavra_atual, letras_corretas)
        print("Possui:", dica)
        print("Tentativas restantes:", tentativas)
        palpite = input("Digite uma letra ou adivinhe a palavra completa: ").lower()

        if len(palpite) == 1 and palpite.isalpha():
            if palpite in palavra_atual:
                letras_corretas.append(palpite)
                print("Boa! A letra está na palavra.")
            else:
                tentativas -= 1
                print("Ops! A letra não está na palavra.")
        elif len(palpite) == len(palavra_atual) and palpite.isalpha():
            if palpite == palavra_atual:
                print("Parabéns! Você adivinhou a palavra corretamente:", palavra_atual)
                palavra_atual = escolher_palavra()
                letras_corretas = []
                tentativas = 10
                dica = exibir_dica(palavra_atual, letras_corretas)
            else:
                tentativas -= 1
                print("Ops! Palavra incorreta. Tentativas restantes:", tentativas)
        else:
            print("Entrada inválida. Por favor, insira uma única letra ou tente adivinhar a palavra completa.")

    print("Fim do jogo. A palavra correta era:", palavra_atual)

if __name__ == "__main__":
    jogo_adivinhacao()
