import os

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

def usuario_info():
    print("\nBem vindo ao conversor de pontos da SoulUp. Aqui você pode trocar seus pontos por passagens!!")
    nome_login = input("\nDigite seu nome de login: ")
    email = input("Digíte seu e-mail para notificações: ")
    print(f"\nBem vindo {nome_login}! Você tem {email} pontos para troca. Agora nos informe o que você precisa.")

def mostrar_menu():
    os.system('cls')
    exibir_nome_programa()
    print("\nInfotmações recebidas, agora tecle no menu a sua necessidade!!\n\n")
    print("---------------------------------- Menu -------------------------------------------")
    print("\n1. Converter pontos em passagens de metrô.")
    print("2. Converter seus pontos em passagens de ônibus.")
    print("3. Juntar almas.")
    print("4. Sair.\n")

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def converter_pontos_metro():
    exibir_subtitulo("Conversor de pontos de metrô")
    pontuacao = input("Digite sua pontuação na SoulUp: ")
    tipo_metro = input("Digite o nome do seu tipo de serviço de transporte (CPTM/Metrô/SPTrans/EMTU/TOP...")
    dados_coletados = {"Pontuação": pontuacao, "Tipo de transporte": tipo_metro}
    print("Seus dados foram coletados com sucesso!! Verifique-os: ", dados_coletados)

    voltar_ao_menu_principal()

def converter_pontos_onibus():
    exibir_subtitulo("Conversor de pontos de onibus")
    pontuacao = input("Digite sua pontuação na SoulUp: ")
    tipo_onibus = input("Digite o nome do seu tipo de serviço de transporte (/SPTrans/EMTU/TOP/Fretamento...")
    dados_coletados = {"Pontuação": pontuacao, "Tipo de transporte": tipo_onibus}
    print("Seus dados foram coletados com sucesso!! Verifique-os: ", dados_coletados)

    voltar_ao_menu_principal()

def
#def escolher_menu():
#    try:
#        if opcao_escolhida == 1






def main():
    os.system('cls')
    exibir_nome_programa()
    usuario_info()
    mostrar_menu()


if __name__ == '__main__':
    main()