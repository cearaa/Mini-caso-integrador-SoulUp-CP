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
    print("3. Setor de fantasminhas da SoulUp.")
    print("4. Sair.\n")

def voltar_ao_menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def finalizar_app():
    exibir_subtitulo('Finalizar app')

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

def scan_almas():
    exibir_subtitulo("Scan de Fantasminhas Soulp")
    tipo_alma = input("Dígite a raridade da alma scaneada: ")
    local_scan = input("Digite a estação ou lugar que o Fantasminha foi coletado: ")
    print("\nEspere um pêriodo de 24h para outra solicitação. Mais informações via e-mail.")

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










def main():
    os.system('cls')
    exibir_nome_programa()
    usuario_info()
    mostrar_menu()


if __name__ == '__main__':
    main()