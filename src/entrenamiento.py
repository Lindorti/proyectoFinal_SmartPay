
# ============================================================
# SMARTPAY
# ENTRENAMIENTO DEL MODELO DE MACHINE LEARNING
# Modelo: Arbol de Decision
# Autora: Linda Ortiz
# ============================================================

import pandas as pd
import joblib
from pathlib import Path

from sklearn.tree import DecisionTreeClassifier


# ------------------------------------------------------------
# 1. UBICACION DE LOS ARCHIVOS
# ------------------------------------------------------------

ruta_proyecto = Path(__file__).resolve().parent.parent

carpeta_datos = ruta_proyecto / "data" / "processed"
carpeta_modelos = ruta_proyecto / "models"

carpeta_modelos.mkdir(parents=True, exist_ok=True)


# ------------------------------------------------------------
# 2. CARGAR DATOS DE ENTRENAMIENTO
# ------------------------------------------------------------

X_train = pd.read_csv(carpeta_datos / "X_train.csv")

y_train = pd.read_csv(carpeta_datos / "y_train.csv")

y_train = y_train["resultado_procesamiento"].astype(int)

print("=== ENTRENAMIENTO DEL MODELO SMARTPAY ===")

print("\nDatos cargados correctamente.")
print(f"Registros de entrenamiento: {len(X_train)}")
print(f"Variables predictoras: {X_train.shape[1]}")


# ------------------------------------------------------------
# 3. VERIFICAR LOS DATOS
# ------------------------------------------------------------

if X_train.isnull().any().any():
    raise ValueError("Existen valores faltantes en X_train.")

if y_train.isnull().any():
    raise ValueError("Existen valores faltantes en y_train.")

if len(X_train) != len(y_train):
    raise ValueError("La cantidad de registros no coincide.")

print("\nVerificacion de datos completada.")


# ------------------------------------------------------------
# 4. CREAR EL MODELO ARBOL DE DECISION
# ------------------------------------------------------------

modelo = DecisionTreeClassifier(
    criterion="gini",
    max_depth=8,
    min_samples_leaf=5,
    random_state=42
)


# ------------------------------------------------------------
# 5. ENTRENAR EL MODELO
# ------------------------------------------------------------

modelo.fit(X_train, y_train)

print("\nModelo entrenado correctamente.")


# ------------------------------------------------------------
# 6. EVALUAR EL AJUSTE SOBRE ENTRENAMIENTO
# ------------------------------------------------------------

predicciones_train = modelo.predict(X_train)

exactitud_train = (
    modelo.score(X_train, y_train) * 100
)

print("\n=== RESULTADO DEL ENTRENAMIENTO ===")

print(
    f"Exactitud sobre entrenamiento: "
    f"{exactitud_train:.2f}%"
)

print(
    f"Profundidad del arbol: "
    f"{modelo.get_depth()}"
)

print(
    f"Numero de hojas: "
    f"{modelo.get_n_leaves()}"
)


# ------------------------------------------------------------
# 7. GUARDAR EL MODELO ENTRENADO
# ------------------------------------------------------------

ruta_modelo = (
    carpeta_modelos / "arbol_decision_smartpay.joblib"
)

joblib.dump(modelo, ruta_modelo)


# ------------------------------------------------------------
# 8. GENERAR VISUALIZACION DEL ARBOL DE DECISION
# ------------------------------------------------------------

import matplotlib.pyplot as plt
from sklearn.tree import plot_tree

# Crear carpeta para guardar la imagen
carpeta_graficas = (
    ruta_proyecto / "reports" / "graficas"
)

carpeta_graficas.mkdir(parents=True, exist_ok=True)

# Crear figura del arbol
plt.figure(figsize=(28, 16))

plot_tree(
    modelo,
    feature_names=X_train.columns,
    class_names=["Rechazado", "Aceptado"],
    filled=True,
    rounded=True,
    fontsize=7
)

plt.title("Arbol de Decision - SmartPay", fontsize=18)
plt.tight_layout()

# Guardar imagen
ruta_arbol = (
    carpeta_graficas / "arbol_decision_smartpay.png"
)

plt.savefig(
    ruta_arbol,
    dpi=200,
    bbox_inches="tight"
)

plt.close()

print("\nVisualizacion del arbol generada correctamente.")
print(f"Imagen guardada en: {ruta_arbol}")


print("\n=== MODELO GUARDADO ===")
print(f"Archivo: {ruta_modelo}")

print("\n=== FIN DEL ENTRENAMIENTO SMARTPAY ===")
