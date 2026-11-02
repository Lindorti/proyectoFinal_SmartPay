
# ============================================================
# SMARTPAY
# PRUEBAS DE LAS VALIDACIONES
# ============================================================

from validaciones import (
    validar_cuenta,
    validar_credito,
    validar_campos_obligatorios,
    validar_valor_pago,
    validar_valor_operacion
)


# 1. PRUEBAS DE NUMERO DE CUENTA

print("\n=== VALIDACION DE CUENTA ===")

print(validar_cuenta("12345678901"))
print(validar_cuenta("1234567890"))
print(validar_cuenta("123456789012"))


# 2. PRUEBAS DE NUMERO DE CREDITO

print("\n=== VALIDACION DE CREDITO ===")

print(validar_credito("98765432109"))
print(validar_credito("9876543210"))
print(validar_credito("9876543210A"))


# 3. PRUEBA DE CAMPOS OBLIGATORIOS

print("\n=== VALIDACION DE SOLICITUD ===")

solicitud = {
    "nit": "900123456",
    "nombre_cliente": "Cliente de prueba",
    "numero_cuenta": "12345678901",
    "tipo_cuenta": "Ahorros",
    "numero_credito": "98765432109",
    "tipo_operacion": "Pago de cuota",
    "valor_pago": 500000
}

errores = validar_campos_obligatorios(solicitud)

if errores:
    for error in errores:
        print(error)
else:
    print("Todos los campos obligatorios estan completos.")


# 4. PRUEBAS DEL VALOR DEL PAGO

print("\n=== VALIDACION DEL VALOR ===")

print(validar_valor_pago(500000))
print(validar_valor_pago(-100))
print(validar_valor_pago("abc"))


# 5. PRUEBAS DE LAS CUATRO OPERACIONES DE CARTERA

print("\n=== VALIDACION DE OPERACIONES DE CARTERA ===")


print("\n1. Pago de cuota:")

print(validar_valor_operacion(
    "Pago de cuota",
    500000,
    cuota_pendiente=500000
))


print("\n2. Abono a capital:")

print(validar_valor_operacion(
    "Abono a capital",
    200000,
    capital_pendiente=300000
))


print("\n3. Abono a intereses:")

print(validar_valor_operacion(
    "Abono a intereses",
    100000,
    intereses_pendientes=150000
))


print("\n4. Pago total:")

print(validar_valor_operacion(
    "Pago total",
    2500000,
    valor_liquidacion=2500000
))


print("\n5. Pago de cuota con valor incorrecto:")

print(validar_valor_operacion(
    "Pago de cuota",
    450000,
    cuota_pendiente=500000
))


# 6. FINALIZACION DE LAS PRUEBAS

print("\n=== FIN DE LAS PRUEBAS SMARTPAY ===")
