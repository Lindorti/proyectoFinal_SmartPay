
# ============================================================
# SMARTPAY
# EVALUACION DEL MODELO DE MACHINE LEARNING
# Modelo: Arbol de Decision
# Autora: Linda Ortiz
# ============================================================

import pandas as pd
import joblib
import matplotlib.pyplot as plt

from pathlib import Path
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)


# ------------------------------------------------------------
# 1. UBICACION DE LOS ARCHIVOS
# ------------------------------------------------------------

ruta_proyecto = Path(__file__).resolve().parent.parent

carpeta_datos = ruta_proyecto / "data" / "processed"
carpeta_modelos = ruta_proyecto / "models"

carpeta_graficas = (
    ruta_proyecto / "reports" / "graficas"
)

carpeta_metricas = (
    ruta_proyecto / "reports" / "metricas"
)

carpeta_graficas.mkdir(parents=True, exist_ok=True)
carpeta_metricas.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. CARGAR MODELO Y DATOS DE PRUEBA
# ------------------------------------------------------------

ruta_modelo = (
    carpeta_modelos / "arbol_decision_smartpay.joblib"
)

modelo = joblib.load(ruta_modelo)

X_test = pd.read_csv(carpeta_datos / "X_test.csv")
y_test = pd.read_csv(carpeta_datos / "y_test.csv")

y_test = y_test["resultado_procesamiento"].astype(int)

# Verificar que las variables coincidan con el entrenamiento
variables_modelo = list(modelo.feature_names_in_)

faltantes = [
    variable for variable in variables_modelo
    if variable not in X_test.columns
]

if faltantes:
    raise ValueError(
        f"Faltan variables requeridas por el modelo: {faltantes}"
    )

X_test = X_test.reindex(columns=variables_modelo)

print("=== EVALUACION DEL MODELO SMARTPAY ===")

print(f"\nRegistros de prueba: {len(X_test)}")
print(f"Variables predictoras: {X_test.shape[1]}")


# ------------------------------------------------------------
# 3. REALIZAR PREDICCIONES
# ------------------------------------------------------------

predicciones = modelo.predict(X_test)

print("\nPredicciones realizadas correctamente.")


# ------------------------------------------------------------
# 4. CALCULAR METRICAS DE EVALUACION
# ------------------------------------------------------------

# Codificacion:
# 0 = Rechazado
# 1 = Aceptado
#
# Para Precision, Recall y F1 se toma como clase positiva
# el resultado Rechazado (clase 0).

accuracy = accuracy_score(y_test, predicciones)

precision = precision_score(
    y_test,
    predicciones,
    pos_label=0,
    zero_division=0
)

recall = recall_score(
    y_test,
    predicciones,
    pos_label=0,
    zero_division=0
)

f1 = f1_score(
    y_test,
    predicciones,
    pos_label=0,
    zero_division=0
)


print("\n=== METRICAS DEL MODELO ===")

print(f"Accuracy:  {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall:    {recall * 100:.2f}%")
print(f"F1-Score:  {f1 * 100:.2f}%")


# ------------------------------------------------------------
# 5. GENERAR MATRIZ DE CONFUSION
# ------------------------------------------------------------

# Filas: valores reales
# Columnas: valores predichos
# Orden: Rechazado (0), Aceptado (1)

matriz = confusion_matrix(
    y_test,
    predicciones,
    labels=[0, 1]
)

print("\n=== MATRIZ DE CONFUSION ===")

print("Orden: Rechazado, Aceptado")
print(matriz)


# ------------------------------------------------------------
# 6. IDENTIFICAR TP, FP, TN Y FN
# ------------------------------------------------------------

# Clase positiva: Rechazado
#
# TP: Rechazados identificados correctamente.
# FP: Aceptados clasificados incorrectamente como rechazados.
# TN: Aceptados identificados correctamente.
# FN: Rechazados clasificados incorrectamente como aceptados.

TP = matriz[0, 0]
FN = matriz[0, 1]
FP = matriz[1, 0]
TN = matriz[1, 1]

print("\n=== INTERPRETACION DE LA MATRIZ ===")

print(f"Verdaderos positivos (TP): {TP}")
print(f"Falsos positivos (FP): {FP}")
print(f"Verdaderos negativos (TN): {TN}")
print(f"Falsos negativos (FN): {FN}")


# ------------------------------------------------------------
# 7. REPORTE DE CLASIFICACION
# ------------------------------------------------------------

print("\n=== REPORTE DE CLASIFICACION ===")

reporte = classification_report(
    y_test,
    predicciones,
    labels=[0, 1],
    target_names=["Rechazado", "Aceptado"],
    zero_division=0
)

print(reporte)


# ------------------------------------------------------------
# 8. GRAFICAR MATRIZ DE CONFUSION
# ------------------------------------------------------------

visualizacion = ConfusionMatrixDisplay(
    confusion_matrix=matriz,
    display_labels=["Rechazado", "Aceptado"]
)

visualizacion.plot(
    cmap="Blues",
    values_format="d"
)

plt.title("Matriz de confusion - SmartPay")
plt.tight_layout()

ruta_imagen = (
    carpeta_graficas / "matriz_confusion_smartpay.png"
)

plt.savefig(
    ruta_imagen,
    dpi=200,
    bbox_inches="tight"
)

plt.close()


# ------------------------------------------------------------
# 9. GUARDAR RESULTADOS DE LAS METRICAS
# ------------------------------------------------------------

resultados = pd.DataFrame({
    "Metrica": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score"
    ],
    "Valor": [
        accuracy,
        precision,
        recall,
        f1
    ]
})

ruta_resultados = (
    carpeta_metricas / "metricas_smartpay.csv"
)

resultados.to_csv(
    ruta_resultados,
    index=False,
    encoding="utf-8-sig"
)


# ------------------------------------------------------------
# 10. FINALIZACION
# ------------------------------------------------------------

print("\n=== ARCHIVOS GENERADOS ===")

print(f"Matriz de confusion: {ruta_imagen}")
print(f"Metricas: {ruta_resultados}")

print("\n=== EVALUACION FINALIZADA ===")
