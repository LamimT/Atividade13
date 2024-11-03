def validar_idade(idade):
    return isinstance(idade, int) and idade >= 0

def calcular_soma_produto(idades_homens, idades_mulheres):
    homem_mais_velho = max(idades_homens)
    homem_mais_novo = min(idades_homens)
    mulher_mais_velha = max(idades_mulheres)
    mulher_mais_nova = min(idades_mulheres)

    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    return soma, produto

# Entrada de dados
idades_homens = []
idades_mulheres = []

# Leitura das idades dos homens
for i in range(2):
    idade = input(f"Digite a idade do homem {i + 1}: ")
    if idade.isdigit():
        idades_homens.append(int(idade))
    else:
        print("Erro: Por favor, insira um número inteiro positivo.")
        break
else:
    for i in range(2):
        idade = input(f"Digite a idade da mulher {i + 1}: ")
        if idade.isdigit():
            idades_mulheres.append(int(idade))
        else:
            print("Erro: Por favor, insira um número inteiro positivo.")
            break
    else:

        soma, produto = calcular_soma_produto(idades_homens, idades_mulheres)

        # Resultados
        print(f"Soma da idade do homem mais velho com a mulher mais nova: {soma}")
        print(f"Produto da idade do homem mais novo com a mulher mais velha: {produto}")