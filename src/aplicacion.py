
# ============================================================
# SMARTPAY
# APLICACION PARA REGISTRO Y CLASIFICACION DE SOLICITUDES
# Autora: Linda Ortiz
# ============================================================

import sys
import joblib
import pandas as pd
import streamlit as st

from pathlib import Path

# Permitir importar el modulo de validaciones
ruta_proyecto = Path(__file__).resolve().parent.parent
sys.path.append(str(Path(__file__).resolve().parent))

from validaciones import (
    validar_cuenta,
    validar_credito,
    validar_campos_obligatorios,
    validar_valor_pago,
    validar_valor_operacion
)


# ------------------------------------------------------------
# 1. CONFIGURACION
# ------------------------------------------------------------

st.set_page_config(
    page_title="SmartPay",
    page_icon="💳",
    layout="centered"
)

st.title("💳 SmartPay")
st.subheader(
    "Registro, validación y clasificación de solicitudes de pagos"
)

st.info(
    "Prototipo académico. Utiliza datos ficticios y no "
    "ejecuta pagos ni movimientos financieros reales."
)

carpeta_modelos = ruta_proyecto / "models"

ruta_modelo = (
    carpeta_modelos / "arbol_decision_smartpay.joblib"
)


# ------------------------------------------------------------
# 2. CARGAR MODELO
# ------------------------------------------------------------

@st.cache_resource
def cargar_modelo(ruta):
    return joblib.load(ruta)


if ruta_modelo.exists():
    try:
        modelo = cargar_modelo(str(ruta_modelo))
        modelo_disponible = True
    except Exception as error:
        modelo = None
        modelo_disponible = False
        st.error(f"No fue posible cargar el modelo: {error}")
else:
    modelo = None
    modelo_disponible = False
    st.warning(
        "No se encuentra el modelo entrenado. "
        "Ejecuta primero entrenamiento.py."
    )


# ------------------------------------------------------------
# 3. FUNCION DE PREPARACION DE DATOS
# ------------------------------------------------------------

def preparar_solicitud(datos):

    solicitud = pd.DataFrame([{
        "tipo_cuenta": datos["tipo_cuenta"],
        "tipo_operacion": datos["tipo_operacion"],
        "valor_pago": datos["valor_pago"],
        "cuota_pendiente": datos["cuota_pendiente"],
        "capital_pendiente": datos["capital_pendiente"],
        "intereses_pendientes": datos["intereses_pendientes"],
        "valor_liquidacion": datos["valor_liquidacion"],
        "estado_cuenta": datos["estado_cuenta"],
        "saldo_disponible": datos["saldo_disponible"],
        "estado_credito": datos["estado_credito"],
        "credito_corresponde_nit": int(
            datos["credito_corresponde_nit"]
        ),
        "cuenta_longitud_valida": int(
            validar_cuenta(datos["numero_cuenta"])[0]
        ),
        "credito_longitud_valida": int(
            validar_credito(datos["numero_credito"])[0]
        )
    }])

    solicitud = pd.get_dummies(
        solicitud,
        columns=[
            "tipo_cuenta",
            "tipo_operacion",
            "estado_cuenta",
            "estado_credito"
        ],
        dtype=int
    )

    # Mantener exactamente las variables usadas en entrenamiento.
    columnas_modelo = list(modelo.feature_names_in_)

    solicitud = solicitud.reindex(
        columns=columnas_modelo,
        fill_value=0
    )

    return solicitud


# ------------------------------------------------------------
# 4. FORMULARIO DE SOLICITUD
# ------------------------------------------------------------

st.header("1. Datos de la solicitud")

with st.form("formulario_smartpay"):

    nit = st.text_input("NIT ficticio")
    nombre_cliente = st.text_input("Nombre del cliente ficticio")

    numero_cuenta = st.text_input(
        "Número de cuenta (11 dígitos)"
    )

    tipo_cuenta = st.selectbox(
        "Tipo de cuenta",
        ["Ahorros", "Corriente"]
    )

    numero_credito = st.text_input(
        "Número de crédito (11 dígitos)"
    )

    tipo_operacion = st.selectbox(
        "Tipo de operación",
        [
            "Pago de cuota",
            "Abono a capital",
            "Abono a intereses",
            "Pago total"
        ]
    )

    valor_pago = st.number_input(
        "Valor del pago",
        min_value=0.0,
        step=1000.0
    )

    st.header("2. Condiciones simuladas")

    cuota_pendiente = st.number_input(
        "Cuota pendiente",
        min_value=0.0,
        step=1000.0
    )

    capital_pendiente = st.number_input(
        "Capital pendiente",
        min_value=0.0,
        step=1000.0
    )

    intereses_pendientes = st.number_input(
        "Intereses pendientes",
        min_value=0.0,
        step=1000.0
    )

    valor_liquidacion = st.number_input(
        "Valor de liquidación",
        min_value=0.0,
        step=1000.0
    )

    saldo_disponible = st.number_input(
        "Saldo disponible simulado",
        min_value=0.0,
        step=1000.0
    )

    estado_cuenta = st.selectbox(
        "Estado de cuenta",
        ["Activa", "Inactiva"]
    )

    estado_credito = st.selectbox(
        "Estado del crédito",
        ["Vigente", "Cancelado"]
    )

    credito_corresponde_nit = st.selectbox(
        "¿El crédito corresponde al NIT?",
        ["Sí", "No"]
    )

    enviar = st.form_submit_button(
        "Validar y clasificar solicitud"
    )


# ------------------------------------------------------------
# 5. VALIDAR Y CLASIFICAR
# ------------------------------------------------------------

if enviar:

    datos = {
        "nit": nit,
        "nombre_cliente": nombre_cliente,
        "numero_cuenta": numero_cuenta,
        "tipo_cuenta": tipo_cuenta,
        "numero_credito": numero_credito,
        "tipo_operacion": tipo_operacion,
        "valor_pago": valor_pago
    }

    errores = validar_campos_obligatorios(datos)

    cuenta_valida, mensaje_cuenta = validar_cuenta(
        numero_cuenta
    )

    credito_valido, mensaje_credito = validar_credito(
        numero_credito
    )

    pago_valido, mensaje_pago = validar_valor_pago(
        valor_pago
    )

    if not cuenta_valida:
        errores.append(mensaje_cuenta)

    if not credito_valido:
        errores.append(mensaje_credito)

    if not pago_valido:
        errores.append(mensaje_pago)

    operacion_valida, mensaje_operacion = validar_valor_operacion(
        tipo_operacion,
        valor_pago,
        cuota_pendiente=cuota_pendiente,
        capital_pendiente=capital_pendiente,
        intereses_pendientes=intereses_pendientes,
        valor_liquidacion=valor_liquidacion
    )

    if not operacion_valida:
        errores.append(mensaje_operacion)

    # Validaciones adicionales del prototipo
    if estado_cuenta != "Activa":
        errores.append("La cuenta se encuentra inactiva.")

    if estado_credito != "Vigente":
        errores.append("El crédito se encuentra cancelado.")

    if saldo_disponible < valor_pago:
        errores.append("El saldo disponible es insuficiente.")

    if credito_corresponde_nit != "Sí":
        errores.append("El crédito no corresponde al NIT informado.")

    st.header("3. Resultado de la validación")

    if errores:

        st.error("La solicitud no cumple las validaciones.")

        for error in errores:
            st.write(f"- {error}")

        st.warning(
            "La clasificación no se ejecuta porque existen "
            "validaciones de negocio pendientes."
        )

    elif not modelo_disponible:

        st.error(
            "No se puede realizar la clasificación porque "
            "el modelo no está disponible."
        )

    else:

        datos_modelo = {
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
            "credito_corresponde_nit": credito_corresponde_nit == "Sí",
            "numero_cuenta": numero_cuenta,
            "numero_credito": numero_credito
        }

        entrada = preparar_solicitud(datos_modelo)

        prediccion = modelo.predict(entrada)[0]

        st.success("Las validaciones de negocio fueron superadas.")

        st.subheader("Clasificación experimental del modelo")

        if prediccion == 1:
            st.success("Resultado del modelo: ACEPTADO")
        else:
            st.warning("Resultado del modelo: RECHAZADO")

        st.info(
            "Esta predicción es experimental. No autoriza pagos "
            "ni reemplaza los controles del proceso."
        )

st.divider()

st.caption(
    "SmartPay | Prototipo académico desarrollado con datos sintéticos."
)
