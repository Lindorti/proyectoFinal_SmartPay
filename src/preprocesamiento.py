
# ============================================================
# SMARTPAY
# PREPROCESAMIENTO DE DATOS PARA MACHINE LEARNING
# Autora: Linda Ortiz
# ============================================================

import pandas as pd
from pathlib import Path
from sklearn.model_selection import train_test_split

# ------------------------------------------------------------
# 1. UBICACION DE LOS ARCHIVOS
# ------------------------------------------------------------

ruta_proyecto = Path(__file__).resolve().parent.parent

ruta_dataset = (
    ruta_proyecto / "data" / "raw"
    / "solicitudes_smartpay.csv"
)

carpeta_salida = (
    ruta_proyecto / "data" / "processed"
)

carpeta_salida.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. CARGAR DATASET
# ------------------------------------------------------------

df = pd.read_csv(ruta_dataset)

print("=== PREPROCESAMIENTO SMARTPAY ===")

print("\nDataset cargado correctamente.")
print(f"Registros: {df.shape[0]}")
print(f"Variables: {df.shape[1]}")


# ------------------------------------------------------------
# 3. SELECCIONAR VARIABLES
# ------------------------------------------------------------

variables_predictoras = [
    "tipo_cuenta",
    "tipo_operacion",
    "valor_pago",
    "cuota_pendiente",
    "capital_pendiente",
    "intereses_pendientes",
    "valor_liquidacion",
    "estado_cuenta",
    "saldo_disponible",
    "estado_credito",
    "credito_corresponde_nit"
]

variable_objetivo = "resultado_procesamiento"

X = df[variables_predictoras].copy()
y = df[variable_objetivo].copy()

print("\nVariables predictoras seleccionadas:")
print(variables_predictoras)

print("\nVariable objetivo:")
print(variable_objetivo)


# ------------------------------------------------------------
# 4. CONVERTIR VARIABLE OBJETIVO A NUMERICA
# ------------------------------------------------------------

y = y.map({
    "Aceptado": 1,
    "Rechazado": 0
})

if y.isnull().any():
    raise ValueError("Existen resultados de procesamiento no reconocidos.")


# ------------------------------------------------------------
# 5. CONVERTIR VARIABLES CATEGORICAS
# ------------------------------------------------------------

X = pd.get_dummies(
    X,
    columns=[
        "tipo_cuenta",
        "tipo_operacion",
        "estado_cuenta",
        "estado_credito"
    ],
    dtype=int
)

# Convertir valores booleanos a numeros
X["credito_corresponde_nit"] = (
    X["credito_corresponde_nit"].astype(int)
)

print("\nVariables despues de la conversion:")
print(X.columns.tolist())

print(f"\nTotal de variables transformadas: {X.shape[1]}")


# ------------------------------------------------------------
# 6. DIVIDIR DATOS: 80% ENTRENAMIENTO Y 20% PRUEBA
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print("\n=== DIVISION DEL DATASET ===")

print(f"Datos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")


# ------------------------------------------------------------
# 7. GUARDAR DATOS PROCESADOS
# ------------------------------------------------------------

X_train.to_csv(
    carpeta_salida / "X_train.csv",
    index=False
)

X_test.to_csv(
    carpeta_salida / "X_test.csv",
    index=False
)

y_train.to_csv(
    carpeta_salida / "y_train.csv",
    index=False,
    header=["resultado_procesamiento"]
)

y_test.to_csv(
    carpeta_salida / "y_test.csv",
    index=False,
    header=["resultado_procesamiento"]
)


# ------------------------------------------------------------
# 8. MOSTRAR DISTRIBUCION DE RESULTADOS
# ------------------------------------------------------------

print("\nDistribucion de entrenamiento:")
print(y_train.value_counts().rename({
    1: "Aceptado",
    0: "Rechazado"
}))

print("\nDistribucion de prueba:")
print(y_test.value_counts().rename({
    1: "Aceptado",
    0: "Rechazado"
}))


print("\n=== PREPROCESAMIENTO FINALIZADO ===")
print(f"Archivos guardados en: {carpeta_salida}")
