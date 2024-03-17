def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Función para calcular el descuento en función del monto total de la compra y un porcentaje de descuento dado.
    """
    descuento = monto_total * porcentaje_descuento / 100
    return descuento

monto_compra1 = 1000
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1

print(f"Monto total de la compra: {monto_compra1} USD")
print(f"Descuento aplicado: {descuento1} USD")
print(f"Monto final a pagar después del descuento: {monto_final1} USD")
print()

monto_compra2 = 1500
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2

print(f"Monto total de la compra: {monto_compra2} USD")
print(f"Descuento aplicado: {descuento2} USD")
print(f"Monto final a pagar después del descuento: {monto_final2} USD")