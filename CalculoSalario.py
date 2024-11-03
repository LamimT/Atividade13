def calcula_salario_final(salario_fixo, comissao_por_carro, percentual_vendas, bonus_adicional, num_carros, total_vendas):
    # Salário inicial apenas com salário fixo
    salario_final = salario_fixo
    # Caso 2: Se o número de carros vendidos for zero
    if num_carros == 0:
        return salario_final  # Apenas o salário fixo
    
    # Caso 1 e 3: Número de carros vendidos > 0
    salario_final += comissao_por_carro * num_carros
    salario_final += (percentual_vendas / 100) * total_vendas
    
    if num_carros > 10:
        salario_final += (bonus_adicional / 100) * total_vendas
    
    return salario_final

# Exemplo
salario_fixo = 2000
comissao_por_carro = 300
percentual_vendas = 5
bonus_adicional = 10

# Exemplo de uso
num_carros = 12  # Número de carros vendidos
total_vendas = 80000  # Total das vendas

salario_final = calcula_salario_final(salario_fixo, comissao_por_carro, percentual_vendas, bonus_adicional, num_carros, total_vendas)
print("Salario final do vendedor:", salario_final)
