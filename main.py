from ETL.coleta import pegar_dados_api
from ETL.coleta import mostrar_previsao_futura
from database.conexao import salvar_previsao


# === MENUS ===
def adicionar_cidade():
    while True:
        cidade = input("\nDigite o nome da cidade ou [0] para sair: ").strip().capitalize()
        if cidade == '0':
            break

        clima = pegar_dados_api(cidade)
        if clima:
            salvar_previsao(clima)
            print(f"✅ Dados de {cidade} inseridos com sucesso!")

def ver_clima():
    while True:
        cidade = input("\nDigite o nome da cidade ou [0] para voltar: ").strip().capitalize()
        if cidade == '0':
            break

        clima = pegar_dados_api(cidade)
        if clima:
            print(f"\n🌆 Cidade: {clima['cidade']}")
            print(f"🌡️ Temperatura: {clima['temperatura']}°C")
            print(f"💨 Sensação térmica: {clima['sensacao_termica']}°C")
            print(f"💧 Umidade: {clima['umidade']}%")
            print(f"☁️ Clima: {clima['clima']}")
            print(f"💬 Descrição: {clima['descricao']}")
            print(f"💨 Vento: {clima['vento']} m/s")
            print("-" * 50)

def ver_previsao():
    while True:
        cidade = input("\nDigite o nome da cidade ou [0] para sair: ").strip().capitalize()
        if cidade == '0':
            break

        try:
            dias = int(input("Quantos dias de previsão? (1 a 4): "))
            if not 1 <= dias <= 5:
                print("⚠️ Digite um número entre 1 e 5.")
                continue
        except ValueError:
            print("⚠️ Entrada inválida.")
            continue

        mostrar_previsao_futura(cidade, dias)

def menu_principal():
    while True:
        print("\n======= MENU =======")
        opcao = input("[1] Adicionar cidade\n[2] Ver clima atual\n[3] Ver previsão futura\n[4] Sair\nEscolha: ")

        if opcao == '1':
            adicionar_cidade()
        elif opcao == '2':
            ver_clima()
        elif opcao == '3':
            ver_previsao()
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("⚠️ Opção inválida.")

# === EXECUÇÃO ===
menu_principal()
print("Obrigado por usar o programa!")
