import pickle
import time
import os
import sys


with open(os.devnull, 'w') as fnull:
    old_stdout = sys.stdout
    sys.stdout = fnull
    import pygame
    sys.stdout = old_stdout

pygame.init()

opcoes_validas = ["1", "2", "3"]

racas_descricoes = {
    "humano": "Os humanos são uma raça versátil e adaptável, conhecidos por sua diversidade e habilidades gerais.",
    "elfo": "Os elfos são criaturas místicas e elegantes, conhecidos por sua afinidade com a natureza e longevidade.",
    "anão": "Os anões são habilidosos mineiros e ferreiros, conhecidos por sua resistência e expertise em trabalhos manuais.",
    "fada": "As fadas são seres mágicos pequenos, conhecidos por sua agilidade e habilidades mágicas sutis.",
    "animal": "Os animais são criaturas da floresta, conhecidos por sua conexão com a natureza e sentidos aguçados.",
    "vampiro": "Os vampiros são seres da noite, conhecidos por se alimentarem de sangue e possuírem habilidades sobrenaturais.",
    "goblin": "Os goblins são criaturas astutas, conhecidas por sua engenhosidade e propensão para travessuras.",
    "troll": "Os trolls são gigantes e robustos, conhecidos por sua força física e resistência.",

}

dados_personagem = {
    "nome": "",
    "idade": "",
    "altura": "",
    "raca": ""
}

def audio(som):
    pygame.mixer.init()
    sound = pygame.mixer.Sound(som)
    sound.play()
    time.sleep(2)
    pygame.mixer.quit()
    return

def escolher_raca():
    while True:
        raca_personagem = input(
            "Qual é a raça do seu personagem?\nhumano\nelfo\nanão\nfada\nanimal\nvampiro\ngoblin\ntroll \n R: ").strip().lower()
        audio("select.wav")

        if raca_personagem in racas_descricoes:
            descricao_raca = racas_descricoes[raca_personagem]
            print(descricao_raca)

            escolha_raca = input("Você deseja confirmar essa raça ou ver outra? (confirmar/outra): ").strip().lower()
            audio("select.wav")

            while escolha_raca != "confirmar" and escolha_raca != "outra":
                print("Escolha inválida.")
                escolha_raca = input("Você deseja confirmar essa raça ou ver outra? (confirmar/outra): ").strip().lower()
                audio("select.wav")

            if escolha_raca == "confirmar":
                dados_personagem["raca"] = raca_personagem
                print(f"Você escolheu a raça {raca_personagem}.")
                break
        else:
            print("Raça inválida. Escolha uma das opções disponíveis.")
            audio("erro.wav")

def salvar_dados(dados, dadinhos):
    try:
        with open(dadinhos, 'wb') as arquivo:
            pickle.dump(dados, arquivo)
        print("Dados salvos com sucesso!")
    except Exception as e:
        print(f"Erro ao salvar dados: {e}")


def carregar_dados(dadinhos):
    try:
        with open(dadinhos, 'rb') as arquivo:
            return pickle.load(arquivo)
    except FileNotFoundError:
        return None
audio("musics.wav")

esc = input("Ola! Oque quer fazer? :\n1 - Começar um novo jogo\n2 - Carregar um jogo salvo\n3 - Sair do programa\nR: ")

if esc == "3":
    print("Até a próxima!")
    audio("musics.wav")


elif esc == "2":
    audio("select.wav")
    time.sleep(1)
    dados_salvos = carregar_dados('')

    if dados_salvos:
        dados_personagem = dados_salvos
        print(f"Carregando o jogo salvo para {dados_personagem['nome']}...")
    else:
        print("Não há jogo salvo para carregar.")

elif esc == "1":
    print("Talvez possa ter algum jogo salvo tem certeza de iniciar um novo? ")
    audio("select.wav")

    log = input("sim ou nao ? ")
    audio("select.wav")

    if log == "sim":
        print("E lá vamos nós!")
        dados_personagem["nome"] = input("Qual é o nome do seu personagem? ")
        audio("select.wav")

        dados_personagem["idade"] = input("Quantos anos seu personagem tem? ")
        audio("select.wav")

        dados_personagem["altura"] = input("Qual é a altura do seu personagem? ")
        audio("select.wav")

        escolher_raca()

        salvar_dados(dados_personagem, 'E:/Users/lu/PycharmProjects/pythonProject/projetorpg/dadinhos.pk1')

    elif log.lower() == "não":
        audio("encerramento.wav")
        time.sleep(5)
        print("Encerrado.")


    else:
        print("Número inválido")
        audio("erro.wav")

        escolha = input("Quer escolher de novo? (sim/não): ")
        audio("select.wav")

    if escolha.lower() == "sim":
        esc = input("Você quer:\n1 - Começar um novo jogo\n2 - Carregar um jogo salvo\n3 - Sair do programa\nR: ")
        if esc in opcoes_validas:
            if esc == "3":
                print("Até a próxima!")
                audio("yamete.wav")

            elif esc == "2":
                print("Ok, vamos carregar um jogo salvo...")
                audio("select.wav")

            elif esc == "1":
                print("E lá vamos nós!")
                audio("select.wav")

                nome_personagem = input("Qual é o nome do seu personagem? ")
                audio("select.wav")

                idade_personagem = input("Quantos anos seu personagem tem? ")
                audio("select.wav")

                altura_personagem = input("Qual é a altura do seu personagem? ")
                audio("select.wav")

                escolher_raca()

    elif escolha.lower() == "não":
        print("Encerrando (nome jogo).")
        audio("musics.wav")

    else:
        print("Escolha inválida. Por favor, digite 'sim' ou 'não'.")
        audio("erro.wav")
