import pickle

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


def escolher_raca():
    while True:
        raca_personagem = input(
            "Qual é a raça do seu personagem?\nhumano\nelfo\nanão\nfada\nanimal\nvampiro\ngoblin\ntroll \n R: ").strip().lower()

        if raca_personagem in racas_descricoes:
            descricao_raca = racas_descricoes[raca_personagem]
            print(descricao_raca)

            escolha_raca = input("Você deseja confirmar essa raça ou ver outra? (confirmar/outra): ").strip().lower()

            while escolha_raca != "confirmar" and escolha_raca != "outra":
                print("Escolha inválida.")
                escolha_raca = input("Você deseja confirmar essa raça ou ver outra? (confirmar/outra): ").strip().lower()

            if escolha_raca == "confirmar":
                dados_personagem["raca"] = raca_personagem
                print(f"Você escolheu a raça {raca_personagem}.")
                break
        else:
            print("Raça inválida. Escolha uma das opções disponíveis.")

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


esc = input("Você quer:\n1 - Começar um novo jogo\n2 - Carregar um jogo salvo\n3 - Sair do programa\nR: ")

if esc == "3":
    print("Até a próxima!")
elif esc == "2":
    dados_salvos = carregar_dados('E:/Users/lu/PycharmProjects/pythonProject/projetorpg/dadinhos.pk1')

    if dados_salvos:
        dados_personagem = dados_salvos
        print(f"Carregando o jogo salvo para {dados_personagem['nome']}...")
    else:
        print("Não há jogo salvo para carregar.")

elif esc == "1":
    print("Talvez possa ter algum jogo salvo tem certeza de iniciar um novo? ")
    log = input("sim ou nao ?")
    if log == "sim":
        print("E lá vamos nós!")
        dados_personagem["nome"] = input("Qual é o nome do seu personagem? ")
        dados_personagem["idade"] = input("Quantos anos seu personagem tem? ")
        dados_personagem["altura"] = input("Qual é a altura do seu personagem? ")

        escolher_raca()

        salvar_dados(dados_personagem, 'E:/Users/lu/PycharmProjects/pythonProject/projetorpg/dadinhos.pk1')  # Salva os dados aqui
    elif log.lower() == "não":
        print("Encerrando (nome jogo).")



else:
    print("Número inválido")
    escolha = input("Quer escolher de novo? (sim/não): ")

    if escolha.lower() == "sim":
        esc = input("Você quer:\n1 - Começar um novo jogo\n2 - Carregar um jogo salvo\n3 - Sair do programa\nR: ")
        if esc in opcoes_validas:
            if esc == "3":
                print("Até a próxima!")
            elif esc == "2":
                print("Ok, vamos carregar um jogo salvo...")
            elif esc == "1":
                print("E lá vamos nós!")
                nome_personagem = input("Qual é o nome do seu personagem? ")
                idade_personagem = input("Quantos anos seu personagem tem? ")
                altura_personagem = input("Qual é a altura do seu personagem? ")

                escolher_raca()

    elif escolha.lower() == "não":
        print("Encerrando (nome jogo).")

    else:
        print("Escolha inválida. Por favor, digite 'sim' ou 'não'.")
