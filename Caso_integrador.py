import os

#Professor, metade deste projeto foi usando conceitos de uma trilha da Alura, especifica para funções.
#Integrantes da Challenge
#Tárik Moussa Alma - RM: 571411
#Giovanni - RM: 569750
#Fabricio Aquiles Sales da Silva - RM: 570985
#Carlos Eduardo - RM:
#Ítalo - RM:

#Função para quando limpar com cls, aparecer essa imagem.
def exibir_nome_programa():
    print("""
░█████╗░░█████╗░███╗░░██╗██╗░░░██╗███████╗██████╗░░██████╗░█████╗░██████╗░  ██████╗░███████╗
██╔══██╗██╔══██╗████╗░██║██║░░░██║██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗  ██╔══██╗██╔════╝
██║░░╚═╝██║░░██║██╔██╗██║╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░██║░░██║██████╔╝  ██║░░██║█████╗░░
██║░░██╗██║░░██║██║╚████║░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗██║░░██║██╔══██╗  ██║░░██║██╔══╝░░
╚█████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░░███████╗██║░░██║██████╔╝╚█████╔╝██║░░██║  ██████╔╝███████╗
░╚════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚═════╝░╚══════╝

██████╗░░█████╗░███╗░░██╗████████╗░█████╗░░██████╗  ░██████╗░█████╗░██╗░░░██╗██╗░░░░░██╗░░░██╗██████╗░
██╔══██╗██╔══██╗████╗░██║╚══██╔══╝██╔══██╗██╔════╝  ██╔════╝██╔══██╗██║░░░██║██║░░░░░██║░░░██║██╔══██╗
██████╔╝██║░░██║██╔██╗██║░░░██║░░░██║░░██║╚█████╗░  ╚█████╗░██║░░██║██║░░░██║██║░░░░░██║░░░██║██████╔╝
██╔═══╝░██║░░██║██║╚████║░░░██║░░░██║░░██║░╚═══██╗  ░╚═══██╗██║░░██║██║░░░██║██║░░░░░██║░░░██║██╔═══╝░
██║░░░░░╚█████╔╝██║░╚███║░░░██║░░░╚█████╔╝██████╔╝  ██████╔╝╚█████╔╝╚██████╔╝███████╗╚██████╔╝██║░░░░░
╚═╝░░░░░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░░╚════╝░╚═════╝░  ╚═════╝░░╚════╝░░╚═════╝░╚══════╝░╚═════╝░╚═╝░░░░░""")

#Função para retornar em ordem na main e priorizar a imagem.
def usuario_info():
    print("\nBem vindo ao conversor de pontos da SoulUp. Aqui você pode trocar seus pontos por passagens!!")
    nome_login = input("\nDigite seu nome de login: ")
    email = input("Digíte seu e-mail: ")
    print(f"\nBem vindo {nome_login}!! Agora nos informe o que você precisa.")

#Função para exibir opções
def mostrar_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_programa()
    print("\nInformações recebidas, agora tecle no menu a sua necessidade!!\n\n")
    print("---------------------------------- Menu -------------------------------------------")
    print("\n1. Converter pontos em passagens de metrô.")
    print("2. Converter seus pontos em passagens de ônibus.")
    print("3. Suporte de fantasminhas da SoulUp.")
    print("4. Sair.\n")

#Função para retorno ao menu com tecla qualquer
def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

#Função para retornar o app finalizado após operação.
def finalizar_app():
    exibir_subtitulo('Finalizar app')

#Func de erro
def opcao_invalida():
    print('Erro: opção inválida!\n')
    voltar_ao_menu_principal()

#Função para que após apague com cls, retorne a opção escolhida com print automátic0
def exibir_subtitulo(texto):
    os.system('cls' if os.name == 'nt' else 'clear')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

#Cansei de explica as funções hahaha

def calcular_pontuacao(pontos):
    return pontos

def converter_pontos_em_credito(pontos):
    #regra simples de exemplo: cada ponto vale R$0,50
    return pontos * 0.5

def converter_pontos_metro():
    exibir_subtitulo("Conversor de pontos de metrô")
    try:
        pontos = float(input("Digite seus pontos da SoulUp: "))

        pontos = calcular_pontuacao(pontos)
        credito = converter_pontos_em_credito(pontos)
        valor_passagem = 5.40
        passagens = int(credito // valor_passagem)
        resto = credito % valor_passagem

        print(f"\nPontos informados: {pontos}")
        print(f"Crédito total: R$ {credito:.2f}")
        print(f"Você pode resgatar {passagens} passagens de metrô (R$ {valor_passagem})")
        print(f"Sobra de crédito: R$ {resto:.2f}")
    except:
        print("Erro: digite um número válido.")
    voltar_ao_menu_principal()

def converter_pontos_onibus():
    exibir_subtitulo("Conversor de pontos de Ônibus")
    try:
        pontos = float(input("Digite seus pontos da SoulUp: "))

        pontos = calcular_pontuacao(pontos)
        credito = converter_pontos_em_credito(pontos)
        valor_passagem = 5.30
        passagens = int(credito // valor_passagem)
        resto = credito % valor_passagem
        print(f"\nPontos informados: {pontos}")
        print(f"Crédito total: R$ {credito:.2f}")
        print(f"Você pode resgatar {passagens} passagens de ônibus (R$ {valor_passagem})")
        print(f"Sobra de crédito: R$ {resto:.2f}")
    except:
        print("Erro: digite um número válido.")
    voltar_ao_menu_principal()

def scan_almas():
    exibir_subtitulo("Scan de Fantasminhas SoulUp")
    tipo_alma = input("Dígite a raridade do Fantasminha scaneada: ")
    local_scan = input("Digite a estação ou lugar que o Fantasminha foi coletado: ")
    print("\nEspere um pêriodo de 24h para outra solicitação. Mais informações via e-mail.")
    print("Verifique as informações digitadas!  |  Raridade do fantasminha: ", tipo_alma, "Local de escaneamento: ", local_scan)

    voltar_ao_menu_principal()

def escolher_opcao():
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))
        if opcao_escolhida == 1:
            converter_pontos_metro()
        elif opcao_escolhida == 2:
            converter_pontos_onibus()
        elif opcao_escolhida == 3:
            scan_almas()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()


#Função para execução em ordem desejada e execução da Main.
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    exibir_nome_programa()
    usuario_info()
    mostrar_menu()
    escolher_opcao()

if __name__ == '__main__':
    main()