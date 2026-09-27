# Pesquisa de satisfação - TudoWeb

excelente = 0
ruim = 0

print("========================================")
print("     PESQUISA DE ATENDIMENTO TUDOWEB")
print("========================================")

for i in range(50):
    print(f"\nEntrevistado {i + 1}")

    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))

    print("\nOpções de atendimento:")
    print("1 - EXCELENTE")
    print("2 - BOM")
    print("3 - RUIM")

    opiniao = int(input("Digite sua opinião: "))

    if opiniao == 1:
        excelente += 1
    elif opiniao == 2:
        pass
    elif opiniao == 3:
        ruim += 1
    else:
        print("Opção inválida.")

print("\n========================================")
print("           RESULTADO DA PESQUISA")
print("========================================")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")
print("========================================")