# Definindo a função para o cálculo do salário final
def calcula_salario_final(salario_fixo, comissao_por_carro, percentual_vendas, bonus_adicional, num_carros, total_vendas):
    salario_final = salario_fixo
    if num_carros == 0:
        return salario_final
    salario_final += comissao_por_carro * num_carros
    salario_final += (percentual_vendas / 100) * total_vendas
    if num_carros > 10:
        salario_final += (bonus_adicional / 100) * total_vendas
    return salario_final

# Parâmetros de exemplo
salario_fixo = 2000
comissao_por_carro = 300
percentual_vendas = 5
bonus_adicional = 10

# Definindo casos de teste
def test_calcula_salario_final():
    testes = [
        # Teste 1: Apenas salário fixo (0 carros vendidos)
        {
            "num_carros": 0,
            "total_vendas": 0,
            "esperado": salario_fixo
        },
        # Teste 2: Salário padrão (5 carros vendidos, total de vendas 50.000)
        {
            "num_carros": 5,
            "total_vendas": 50000,
            "esperado": salario_fixo + (comissao_por_carro * 5) + (percentual_vendas / 100 * 50000)
        },
        # Teste 3: Salário com incentivo adicional (12 carros vendidos, total de vendas 80.000)
        {
            "num_carros": 12,
            "total_vendas": 80000,
            "esperado": salario_fixo + (comissao_por_carro * 12) + (percentual_vendas / 100 * 80000) + (bonus_adicional / 100 * 80000)
        },
    ]

    # Executando os testes
    for i, teste in enumerate(testes, 1):
        resultado = calcula_salario_final(salario_fixo, comissao_por_carro, percentual_vendas, bonus_adicional, teste["num_carros"], teste["total_vendas"])
        assert resultado == teste["esperado"], f"Teste {i} falhou: esperado {teste['esperado']}, obteve {resultado}"
        print(f"Teste {i} passou: resultado {resultado}")

# Executando a função de testes
test_calcula_salario_final()
