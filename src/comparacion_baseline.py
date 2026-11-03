
# ============================================================
# SMARTPAY
# COMPARACION DEL ARBOL DE DECISION CON MODELO BASELINE
# Autora: Linda Ortiz
# ============================================================

import pandas as pd
import joblib

from pathlib import Path
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    ConfusionMatrixDisplay
)

import matplotlib.pyplot as plt


# ------------------------------------------------------------
# 1. UBICACION DE LOS ARCHIVOS
# ------------------------------------------------------------

ruta_proyecto = Path(__file__).resolve().parent.parent

carpeta_datos = ruta_proyecto / "data" / "processed"
carpeta_modelos = ruta_proyecto / "models"
carpeta_metricas = ruta_proyecto / "reports" / "metricas"
carpeta_graficas = ruta_proyecto / "reports" / "graficas"

carpeta_metricas.mkdir(parents=True, exist_ok=True)
carpeta_graficas.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. CARGAR DATOS DE PRUEBA
# ------------------------------------------------------------

X_test = pd.read_csv(carpeta_datos / "X_test.csv")

y_test = pd.read_csv(
    carpeta_datos / "y_test.csv"
)["resultado_procesamiento"].astype(int)

y_train = pd.read_csv(
    carpeta_datos / "y_train.csv"
)["resultado_procesamiento"].astype(int)

print("=== COMPARACION DE MODELOS SMARTPAY ===")

print(f"\nRegistros de prueba: {len(X_test)}")


# ------------------------------------------------------------
# 3. CARGAR EL ARBOL DE DECISION ENTRENADO
# ------------------------------------------------------------

ruta_modelo = (
    carpeta_modelos / "arbol_decision_smartpay.joblib"
)

if not ruta_modelo.exists():
    raise FileNotFoundError(
        "No se encuentra el modelo entrenado. "
        "Ejecute primero entrenamiento.py."
    )

modelo_arbol = joblib.load(ruta_modelo)

print("\nArbol de Decision cargado correctamente.")


# ------------------------------------------------------------
# 4. CREAR Y ENTRENAR EL MODELO BASELINE
# ------------------------------------------------------------

modelo_baseline = DummyClassifier(
    strategy="most_frequent"
)

modelo_baseline.fit(
    pd.read_csv(carpeta_datos / "X_train.csv"),
    y_train
)

print("Modelo DummyClassifier entrenado correctamente.")


# ------------------------------------------------------------
# 5. GENERAR PREDICCIONES
# ------------------------------------------------------------

predicciones_arbol = modelo_arbol.predict(X_test)

predicciones_baseline = modelo_baseline.predict(X_test)


# ------------------------------------------------------------
# 6. CALCULAR METRICAS
# ------------------------------------------------------------

def calcular_metricas(y_real, y_predicho):

    return {
        "Accuracy": accuracy_score(
            y_real, y_predicho
        ),

        "Precision_Rechazado": precision_score(
            y_real,
            y_predicho,
            pos_label=0,
            zero_division=0
        ),

        "Recall_Rechazado": recall_score(
            y_real,
            y_predicho,
            pos_label=0,
            zero_division=0
        ),

        "F1_Rechazado": f1_score(
            y_real,
            y_predicho,
            pos_label=0,
            zero_division=0
        )
    }


metricas_arbol = calcular_metricas(
    y_test,
    predicciones_arbol
)

metricas_baseline = calcular_metricas(
    y_test,
    predicciones_baseline
)


# ------------------------------------------------------------
# 7. COMPARAR RESULTADOS
# ------------------------------------------------------------

resultados = pd.DataFrame(
    [metricas_arbol, metricas_baseline],
    index=["Arbol de Decision", "Baseline"]
)

print("\n=== RESULTADOS COMPARATIVOS ===")

print(
    (resultados * 100).round(2).to_string()
)

# Guardar resultados en CSV

ruta_resultados = (
    carpeta_metricas / "comparacion_modelos.csv"
)

resultados.to_csv(ruta_resultados)


# ------------------------------------------------------------
# 8. MATRIZ DE CONFUSION DEL BASELINE
# ------------------------------------------------------------

matriz = confusion_matrix(
    y_test,
    predicciones_baseline,
    labels=[0, 1]
)

visualizacion = ConfusionMatrixDisplay(
    confusion_matrix=matriz,
    display_labels=["Rechazado", "Aceptado"]
)

visualizacion.plot(
    cmap="Blues",
    values_format="d"
)

plt.title("Matriz de confusion - Baseline SmartPay")
plt.tight_layout()

ruta_grafica = (
    carpeta_graficas / "matriz_confusion_baseline.png"
)

plt.savefig(
    ruta_grafica,
    dpi=200,
    bbox_inches="tight"
)

plt.close()


# ------------------------------------------------------------
# 9. CONCLUSION AUTOMATICA
# ------------------------------------------------------------

print("\n=== ANALISIS COMPARATIVO ===")

if (
    metricas_arbol["Accuracy"]
    > metricas_baseline["Accuracy"]
):
    print(
        "El Arbol de Decision obtuvo mayor Accuracy "
        "que el modelo baseline."
    )

elif (
    metricas_arbol["Accuracy"]
    < metricas_baseline["Accuracy"]
):
    print(
        "El modelo baseline obtuvo mayor Accuracy "
        "que el Arbol de Decision."
    )

else:
    print(
        "Ambos modelos obtuvieron el mismo Accuracy."
    )

print("\nArchivos generados:")
print(f"- {ruta_resultados}")
print(f"- {ruta_grafica}")

print("\n=== COMPARACION FINALIZADA ===")
