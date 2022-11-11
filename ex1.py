"""
Exercícios - Python

Observação: Todos os exercícios devem utilizar a função input,
de forma que o usuário possa determinar os dados de entrada.

plataformas para treinar sua lógica: site - uri

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais qual
será o valor do mesmo com desconto de (??)%.

"""
"""
ex1

base = input("Digite o valor da base ")
altura = input("Digite o valor da Altura ")

area = float(base) * float(altura)

print("sua area eh de: ", area)
"""
"""
ex2
lado = input("Digite o valor do Lado? ")

area = float(lado) * float(lado)

print("sua area eh de: ", area)
"""
v_produto = input("Qual o valor do Produto? ")
v_deconto = input("Qual a porcentagem de desconto? ")
v_deconto2 = float(v_deconto) / 100 * float(v_produto)


v_final = float(v_produto) - float(v_deconto2)
print(f"O valor com desconto sera de: {v_final} R$")
