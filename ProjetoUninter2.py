print("--- SISTEMA DE VENDAS PARA EMPREENDEDORAS ---")

# 1. Entrada de Dados
produto = input("O que foi vendido? ")
valor_venda = float(input("Qual o valor total (R$)? "))

print("\nFORMAS DE PAGAMENTO:")
print("1 - Dinheiro")
print("2 - Cartão")
opcao = input("Escolha a opção (1 ou 2): ")

# 2. Lógica de Decisão e Cálculo
if opcao == "1":
    print("\n--- PAGAMENTO EM DINHEIRO ---")
    valor_pago = float(input("Quanto a cliente entregou em dinheiro (R$)? "))
    
    if valor_pago >= valor_venda:
        troco = valor_pago - valor_venda
        print(f"Troco a devolver: R$ {troco:.2f}")
    else:
        print("Erro: O valor pago é menor que o valor da venda!")

elif opcao == "2":
    print("\n--- PAGAMENTO EM CARTÃO ---")
    print("Venda registrada! Não esqueça de conferir a taxa da maquininha.")

else:
    print("Opção inválida!")

print("\n--- VENDA FINALIZADA ---")