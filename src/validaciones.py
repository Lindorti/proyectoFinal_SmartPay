
# ============================================================
# SMARTPAY
# MODULO DE VALIDACIONES Y REGLAS DE NEGOCIO
# ============================================================


# 1. VALIDAR NUMERO DE 11 DIGITOS
def validar_numero_11_digitos(numero, nombre_campo):
    """
    Valida que el numero de cuenta o credito
    contenga exactamente 11 digitos numericos.
    """

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


# 2. VALIDAR NUMERO DE CUENTA
def validar_cuenta(numero_cuenta):
    return validar_numero_11_digitos(
        numero_cuenta,
        "numero de cuenta"
    )


# 3. VALIDAR NUMERO DE CREDITO
def validar_credito(numero_credito):
    return validar_numero_11_digitos(
        numero_credito,
        "numero de credito"
    )


# 4. VALIDAR CAMPOS OBLIGATORIOS
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


# 5. VALIDAR VALOR DEL PAGO
def validar_valor_pago(valor):
    """
    Verifica que el valor del pago sea numerico y positivo.
    """

    try:
        valor = float(valor)

        if valor <= 0:
            return False, (
                "El valor del pago debe ser mayor que cero."
            )

        return True, "El valor del pago es valido."

    except (ValueError, TypeError):
        return False, (
            "El valor del pago debe ser numerico."
        )


# 6. VALIDAR VALOR SEGUN EL TIPO DE OPERACION
def validar_valor_operacion(
    tipo_operacion,
    valor_pago,
    cuota_pendiente=0,
    capital_pendiente=0,
    intereses_pendientes=0,
    valor_liquidacion=0
):
    """
    Valida el valor ingresado segun el tipo de pago de cartera.

    Pago de cuota: debe coincidir exactamente con la cuota.
    Abono a capital: no puede superar el capital pendiente.
    Abono a intereses: no puede superar los intereses pendientes.
    Pago total: debe coincidir con la liquidacion.
    """

    try:
        valor_pago = float(valor_pago)

        if valor_pago <= 0:
            return False, (
                "El valor debe ser mayor que cero."
            )

        if tipo_operacion == "Pago de cuota":

            if valor_pago != float(cuota_pendiente):
                return False, (
                    "El valor debe coincidir exactamente "
                    "con la cuota pendiente."
                )

        elif tipo_operacion == "Abono a capital":

            if valor_pago > float(capital_pendiente):
                return False, (
                    "El abono supera el capital pendiente."
                )

        elif tipo_operacion == "Abono a intereses":

            if valor_pago > float(intereses_pendientes):
                return False, (
                    "El abono supera los intereses pendientes."
                )

        elif tipo_operacion == "Pago total":

            if valor_pago != float(valor_liquidacion):
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

    except (ValueError, TypeError):
        return False, (
            "Los valores de la operacion deben ser numericos."
        )
