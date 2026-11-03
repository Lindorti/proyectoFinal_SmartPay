
# ============================================================
# SMARTPAY
# GENERACION DE DATASET SINTETICO DE PAGOS DE CARTERA
# Autora: Linda Ortiz
# ============================================================

import random
import pandas as pd
from pathlib import Path

# ------------------------------------------------------------
# 1. CONFIGURACION GENERAL
# ------------------------------------------------------------

random.seed(42)

TOTAL_SOLICITUDES = 2000

TIPOS_OPERACION = [
    "Pago de cuota",
    "Abono a capital",
    "Abono a intereses",
    "Pago total"
]

TIPOS_CUENTA = ["Ahorros", "Corriente"]

solicitudes = []


# ------------------------------------------------------------
# 2. GENERAR NUMEROS FICTICIOS
# ------------------------------------------------------------

def generar_numero(longitud=11):
    """
    Genera identificadores numericos ficticios.
    """

    return "".join(
        str(random.randint(0, 9))
        for _ in range(longitud)
    )


# ------------------------------------------------------------
# 3. GENERAR UNA SOLICITUD
# ------------------------------------------------------------

def generar_solicitud(id_solicitud, aceptada):
    """
    Genera una solicitud aceptada o rechazada
    mediante condiciones simuladas de negocio.
    """

    # Datos ficticios de identificacion
    nit = generar_numero(9)
    numero_cuenta = generar_numero(11)
    numero_credito = generar_numero(11)

    # Seleccion de productos y operaciones
    tipo_cuenta = random.choice(TIPOS_CUENTA)
    tipo_operacion = random.choice(TIPOS_OPERACION)

    # Valores pendientes simulados
    cuota_pendiente = random.randint(100, 1000) * 1000

    capital_pendiente = (
        random.randint(500, 10000) * 1000
    )

    intereses_pendientes = (
        random.randint(50, 500) * 1000
    )

    valor_liquidacion = (
        capital_pendiente + intereses_pendientes
    )

    # --------------------------------------------------------
    # GENERAR VALOR CORRECTO SEGUN LA OPERACION
    # --------------------------------------------------------

    if tipo_operacion == "Pago de cuota":

        valor_pago = cuota_pendiente

    elif tipo_operacion == "Abono a capital":

        valor_pago = random.randint(
            1,
            capital_pendiente // 1000
        ) * 1000

    elif tipo_operacion == "Abono a intereses":

        valor_pago = random.randint(
            1,
            intereses_pendientes // 1000
        ) * 1000

    else:

        valor_pago = valor_liquidacion

    # --------------------------------------------------------
    # CONDICIONES INICIALES VALIDAS
    # --------------------------------------------------------

    estado_cuenta = "Activa"

    saldo_disponible = (
        valor_pago + random.randint(100, 1000) * 1000
    )

    estado_credito = "Vigente"

    credito_corresponde_nit = True

    motivo_rechazo = "Ninguno"

    # --------------------------------------------------------
    # GENERAR CONDICIONES DE RECHAZO
    # --------------------------------------------------------

    if not aceptada:

        motivo_rechazo = random.choice([
            "Cuenta con longitud incorrecta",
            "Credito con longitud incorrecta",
            "Cuenta inactiva",
            "Saldo insuficiente",
            "Credito cancelado",
            "Credito no corresponde al NIT",
            "Valor de operacion incorrecto"
        ])

        if motivo_rechazo == "Cuenta con longitud incorrecta":

            numero_cuenta = generar_numero(
                random.choice([10, 12])
            )

        elif motivo_rechazo == "Credito con longitud incorrecta":

            numero_credito = generar_numero(
                random.choice([10, 12])
            )

        elif motivo_rechazo == "Cuenta inactiva":

            estado_cuenta = "Inactiva"

        elif motivo_rechazo == "Saldo insuficiente":

            saldo_disponible = max(
                0,
                valor_pago - 1000
            )

        elif motivo_rechazo == "Credito cancelado":

            estado_credito = "Cancelado"

        elif motivo_rechazo == "Credito no corresponde al NIT":

            credito_corresponde_nit = False

        elif motivo_rechazo == "Valor de operacion incorrecto":

            if tipo_operacion in [
                "Pago de cuota",
                "Pago total"
            ]:

                valor_pago += 1000

            elif tipo_operacion == "Abono a capital":

                valor_pago = capital_pendiente + 1000

            elif tipo_operacion == "Abono a intereses":

                valor_pago = intereses_pendientes + 1000

    # --------------------------------------------------------
    # 4. VALIDAR NUMERO DE CUENTA Y CREDITO
    # --------------------------------------------------------

    cuenta_valida = (
        numero_cuenta.isdigit()
        and len(numero_cuenta) == 11
    )

    credito_valido = (
        numero_credito.isdigit()
        and len(numero_credito) == 11
    )

    # --------------------------------------------------------
    # 5. VALIDAR VALOR SEGUN TIPO DE OPERACION
    # --------------------------------------------------------

    if tipo_operacion == "Pago de cuota":

        operacion_valida = (
            valor_pago == cuota_pendiente
        )

    elif tipo_operacion == "Abono a capital":

        operacion_valida = (
            0 < valor_pago <= capital_pendiente
        )

    elif tipo_operacion == "Abono a intereses":

        operacion_valida = (
            0 < valor_pago <= intereses_pendientes
        )

    else:

        operacion_valida = (
            valor_pago == valor_liquidacion
        )

    # --------------------------------------------------------
    # 6. DETERMINAR RESULTADO FINAL
    # --------------------------------------------------------

    aceptacion_final = all([
        cuenta_valida,
        credito_valido,
        estado_cuenta == "Activa",
        saldo_disponible >= valor_pago,
        estado_credito == "Vigente",
        credito_corresponde_nit,
        operacion_valida,
        valor_pago > 0
    ])

    resultado = (
        "Aceptado"
        if aceptacion_final
        else "Rechazado"
    )

    # --------------------------------------------------------
    # 7. DEVOLVER REGISTRO
    # --------------------------------------------------------

    return {
        "id_solicitud": f"SP{id_solicitud:04d}",
        "nit": nit,
        "numero_cuenta": numero_cuenta,
        "numero_credito": numero_credito,
        "tipo_cuenta": tipo_cuenta,
        "tipo_operacion": tipo_operacion,
        "valor_pago": valor_pago,
        "cuota_pendiente": cuota_pendiente,
        "capital_pendiente": capital_pendiente,
        "intereses_pendientes": intereses_pendientes,
        "valor_liquidacion": valor_liquidacion,
        "estado_cuenta": estado_cuenta,
        "saldo_disponible": saldo_disponible,
        "estado_credito": estado_credito,
        "credito_corresponde_nit": credito_corresponde_nit,
        "motivo_rechazo": motivo_rechazo,
        "resultado_procesamiento": resultado
    }


# ------------------------------------------------------------
# 8. GENERAR LAS 2000 SOLICITUDES
# ------------------------------------------------------------

for i in range(1, TOTAL_SOLICITUDES + 1):

    aceptada = (
        i <= TOTAL_SOLICITUDES // 2
    )

    solicitudes.append(
        generar_solicitud(i, aceptada)
    )


# ------------------------------------------------------------
# 9. MEZCLAR Y CONSTRUIR DATASET
# ------------------------------------------------------------

random.shuffle(solicitudes)

df = pd.DataFrame(solicitudes)


# ------------------------------------------------------------
# 10. VERIFICACION DE CONSISTENCIA
# ------------------------------------------------------------

# Verificar cantidad de registros
assert len(df) == TOTAL_SOLICITUDES, (
    "La cantidad de registros generados no es correcta."
)

# Verificar identificadores unicos
assert df["id_solicitud"].is_unique, (
    "Existen identificadores de solicitud duplicados."
)

# Separar solicitudes por resultado
aceptadas = df[
    df["resultado_procesamiento"] == "Aceptado"
]

rechazadas = df[
    df["resultado_procesamiento"] == "Rechazado"
]

# Verificar motivos de las solicitudes aceptadas
assert (
    aceptadas["motivo_rechazo"] == "Ninguno"
).all(), (
    "Existen solicitudes aceptadas con motivo de rechazo."
)

# Verificar motivos de las solicitudes rechazadas
assert (
    rechazadas["motivo_rechazo"] != "Ninguno"
).all(), (
    "Existen solicitudes rechazadas sin motivo."
)

# Verificar distribucion equilibrada
assert len(aceptadas) == 1000, (
    "La cantidad de solicitudes aceptadas no es correcta."
)

assert len(rechazadas) == 1000, (
    "La cantidad de solicitudes rechazadas no es correcta."
)

print("\n=== VERIFICACION DE CONSISTENCIA ===")

print("Cantidad de registros: correcta.")
print("Identificadores unicos: correctos.")
print("Motivos de rechazo: consistentes.")
print("Distribucion de resultados: correcta.")


# ------------------------------------------------------------
# 11. GUARDAR DATASET
# ------------------------------------------------------------

ruta_salida = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "raw"
)

ruta_salida.mkdir(
    parents=True,
    exist_ok=True
)

archivo_salida = (
    ruta_salida / "solicitudes_smartpay.csv"
)

df.to_csv(
    archivo_salida,
    index=False,
    encoding="utf-8-sig"
)


# ------------------------------------------------------------
# 12. MOSTRAR RESULTADOS
# ------------------------------------------------------------

print("\n=== DATASET SMARTPAY GENERADO ===")

print(f"\nTotal de solicitudes: {len(df)}")

print("\nDistribucion de resultados:")

print(
    df["resultado_procesamiento"].value_counts()
)

print("\nDistribucion porcentual:")

print(
    df["resultado_procesamiento"]
    .value_counts(normalize=True)
    .mul(100)
    .round(2)
)

print("\nDistribucion por tipo de operacion:")

print(
    df["tipo_operacion"].value_counts()
)

print("\nMotivos de rechazo:")

print(
    df.loc[
        df["resultado_procesamiento"] == "Rechazado",
        "motivo_rechazo"
    ].value_counts()
)

print("\nMuestra de las primeras 10 solicitudes:")

print(
    df.head(10).to_string(index=False)
)

print("\nArchivo guardado en:")

print(archivo_salida)

print("\n=== GENERACION FINALIZADA CORRECTAMENTE ===")
