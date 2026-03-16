# ==============================
# SISTEMA FARMTECH SOLUTIONS
# Agricultura Digital
# ==============================

culturas = []
areas = []
insumos = []
quantidades = []


def calcular_area():

    cultura = input("Digite a cultura (Milho ou Café): ").lower()

    if cultura == "milho":

        print("\nÁrea calculada como RETÂNGULO")
        base = float(input("Base do terreno (m): "))
        altura = float(input("Altura do terreno (m): "))

        area = base * altura

    elif cultura == "café":

        print("\nÁrea calculada como CÍRCULO")
        raio = float(input("Raio do terreno (m): "))

        area = 3.1416 * (raio ** 2)

    else:

        print("Cultura inválida.")
        return None, None

    return cultura, area


def inserir_dados():

    print("\n=== INSERIR NOVOS DADOS ===")

    cultura, area = calcular_area()

    if cultura is None:
        return

    insumo = input("Tipo de insumo (fertilizante, fosfato, etc): ")

    metros = float(input("Metros de plantio: "))
    ml_por_metro = float(input("Quantidade de insumo (mL por metro): "))

    total_ml = metros * ml_por_metro
    total_litros = total_ml / 1000

    culturas.append(cultura)
    areas.append(area)
    insumos.append(insumo)
    quantidades.append(total_litros)

    print("\n✅ Registro salvo com sucesso!")
    print(f"Área calculada: {area:.2f} m²")
    print(f"Insumo necessário: {total_litros:.2f} L")


def mostrar_dados():

    print("\n=== DADOS DA LAVOURA ===")

    if len(culturas) == 0:
        print("Nenhum registro cadastrado.")
        return

    for i in range(len(culturas)):

        print("\nRegistro:", i)
        print("Cultura:", culturas[i].capitalize())
        print("Área:", round(areas[i], 2), "m²")
        print("Insumo:", insumos[i])
        print("Quantidade:", round(quantidades[i], 2), "L")


def atualizar_dados():

    print("\n=== ATUALIZAR REGISTRO ===")

    pos = int(input("Digite o número do registro: "))

    if pos >= len(culturas):
        print("Registro não encontrado.")
        return

    nova_cultura = input("Nova cultura: ")
    nova_area = float(input("Nova área: "))
    novo_insumo = input("Novo insumo: ")
    nova_quantidade = float(input("Nova quantidade (L): "))

    culturas[pos] = nova_cultura
    areas[pos] = nova_area
    insumos[pos] = novo_insumo
    quantidades[pos] = nova_quantidade

    print("✅ Registro atualizado.")


def deletar_dados():

    print("\n=== DELETAR REGISTRO ===")

    pos = int(input("Digite o número do registro: "))

    if pos >= len(culturas):
        print("Registro não encontrado.")
        return

    culturas.pop(pos)
    areas.pop(pos)
    insumos.pop(pos)
    quantidades.pop(pos)

    print("✅ Registro removido.")


def menu():

    while True:

        print("\n==============================")
        print("     FARMTECH SOLUTIONS")
        print(" Sistema de Agricultura Digital")
        print("==============================")

        print("1 - Inserir dados")
        print("2 - Mostrar dados")
        print("3 - Atualizar dados")
        print("4 - Deletar dados")
        print("5 - Sair")
        print("6 - Exportar dados para análise (CSV)")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            inserir_dados()

        elif opcao == "2":
            mostrar_dados()

        elif opcao == "3":
            mostrar_dados()
            atualizar_dados()

        elif opcao == "4":
            mostrar_dados()
            deletar_dados()

        elif opcao == "5":

            print("\nEncerrando sistema...")
            print("Obrigado por usar o FarmTech!")
            break

        elif opcao == "6":
            exportar_csv()

        else:
            print("Opção inválida.")

import csv

def exportar_csv():

    with open("dados_lavoura.csv", "w", newline="", encoding="utf-8") as arquivo:

        writer = csv.writer(arquivo)

        writer.writerow(["Cultura", "Area", "Insumo", "Quantidade_L"])

        for i in range(len(culturas)):

            writer.writerow([
                culturas[i],
                areas[i],
                insumos[i],
                quantidades[i]
            ])

    print("✅ Dados exportados para dados_lavoura.csv")

menu()