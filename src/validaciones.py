
# ============================================================
# SMARTPAY
# MODULO DE VALIDACIONES Y REGLAS DE NEGOCIO
# Autora: Linda Ortiz
# ============================================================

from decimal import Decimal, InvalidOperation


# ------------------------------------------------------------
# FUNCION AUXILIAR PARA VALIDAR VALORES NUMERICOS
# ------------------------------------------------------------

def convertir_decimal(valor):
    """Convierte un valor a Decimal y evita valores no finitos."""

    try:
        numero = Decimal(str(valor).strip())

        if not numero.is_finite():
            return None

        return numero

    except (InvalidOperation, ValueError, TypeError):
        return None


# ------------------------------------------------------------
# 1. VALIDAR NUMERO DE 11 DIGITOS
# ------------------------------------------------------------

def validar_numero_11_digitos(numero, nombre_campo):
    """
    Valida que el numero de cuenta o credito
    contenga exactamente 11 digitos numericos.
    """

    if numero is None:
        return False, f"El {nombre_campo} es obligatorio."

    numero = str(numero).strip()

    if not numero.isdigit():
        return False, (
            f"El {nombre_campo} debe contener unicamente numeros."
        )

    if len(numero) != 11:
        return False, (
            f"El {nombre_campo} debe tener exactamente 11 digitos."
        )

    return True, f"El {nombre_campo} tiene un formato valido."


# ------------------------------------------------------------
# 2. VALIDAR NUMERO DE CUENTA
# ------------------------------------------------------------

def validar_cuenta(numero_cuenta):
    return validar_numero_11_digitos(
        numero_cuenta,
        "numero de cuenta"
    )


# ------------------------------------------------------------
# 3. VALIDAR NUMERO DE CREDITO
# ------------------------------------------------------------

def validar_credito(numero_credito):
    return validar_numero_11_digitos(
        numero_credito,
        "numero de credito"
    )


# ------------------------------------------------------------
# 4. VALIDAR CAMPOS OBLIGATORIOS
# ------------------------------------------------------------

def validar_campos_obligatorios(datos):
    """
    Verifica que todos los campos requeridos
    para registrar una solicitud esten completos.
    """

    campos_obligatorios = [
        "nit",
        "nombre_cliente",
        "numero_cuenta",
        "tipo_cuenta",
        "numero_credito",
        "tipo_operacion",
        "valor_pago"
    ]

    errores = []

    for campo in campos_obligatorios:

        valor = datos.get(campo)

        if valor is None or str(valor).strip() == "":
            errores.append(
                f"El campo {campo} es obligatorio."
            )

    return errores


# ------------------------------------------------------------
# 5. VALIDAR VALOR DEL PAGO
# ------------------------------------------------------------

def validar_valor_pago(valor):
    """
    Verifica que el valor del pago sea numerico y positivo.
    """

    numero = convertir_decimal(valor)

    if numero is None:
        return False, (
            "El valor del pago debe ser numerico."
        )

    if numero <= 0:
        return False, (
            "El valor del pago debe ser mayor que cero."
        )

    return True, "El valor del pago es valido."


# ------------------------------------------------------------
# 6. VALIDAR VALOR SEGUN EL TIPO DE OPERACION
# ------------------------------------------------------------

def validar_valor_operacion(
    tipo_operacion,
    valor_pago,
    cuota_pendiente=0,
    capital_pendiente=0,
    intereses_pendientes=0,
    valor_liquidacion=0
):
    """
    Valida el valor ingresado segun el tipo de operacion.

    Pago de cuota: debe coincidir exactamente con la cuota.
    Abono a capital: debe ser positivo y no superar el capital.
    Abono a intereses: debe ser positivo y no superar los intereses.
    Pago total: debe coincidir exactamente con la liquidacion.
    """

    pago = convertir_decimal(valor_pago)

    if pago is None:
        return False, (
            "El valor del pago debe ser numerico."
        )

    if pago <= 0:
        return False, (
            "El valor debe ser mayor que cero."
        )

    # Obtener el valor de referencia segun la operacion

    if tipo_operacion == "Pago de cuota":

        referencia = convertir_decimal(cuota_pendiente)

        mensaje_error = (
            "El valor debe coincidir exactamente "
            "con la cuota pendiente."
        )

        if referencia is None or referencia < 0:
            return False, "La cuota pendiente no es valida."

        if pago != referencia:
            return False, mensaje_error

    elif tipo_operacion == "Abono a capital":

        referencia = convertir_decimal(capital_pendiente)

        if referencia is None or referencia < 0:
            return False, "El capital pendiente no es valido."

        if pago > referencia:
            return False, (
                "El abono supera el capital pendiente."
            )

    elif tipo_operacion == "Abono a intereses":

        referencia = convertir_decimal(intereses_pendientes)

        if referencia is None or referencia < 0:
            return False, "Los intereses pendientes no son validos."

        if pago > referencia:
            return False, (
                "El abono supera los intereses pendientes."
            )

    elif tipo_operacion == "Pago total":

        referencia = convertir_decimal(valor_liquidacion)

        if referencia is None or referencia < 0:
            return False, "El valor de liquidacion no es valido."

        if pago != referencia:
            return False, (
                "El valor debe coincidir exactamente "
                "con la liquidacion."
            )

    else:
        return False, (
            "El tipo de operacion no es valido."
        )

    return True, (
        "La operacion cumple con la validacion del valor."
    )
