
valor_compra = float(input("Digite o valor da compra: "))


preco_com_desconto = valor_compra * 0.9

valor_parcela = valor_compra / 6

comissao_vista = preco_com_desconto * 0.05

comissao_parcelado = valor_compra * 0.05


print(f"Valor com desconto: {preco_com_desconto:.2f}")
print(f"Valor da parcela: {valor_parcela:.2f}")
print(f"Comissão do vendedor (à vista): {comissao_vista:.2f}")
print(f"Comissão do vendedor (parcelado): {comissao_parcelado:.2f}")

