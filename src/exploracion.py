
# ============================================================
# SMARTPAY
# EXPLORACION Y CALIDAD DEL DATASET
# Autora: Linda Ortiz
# ============================================================

import pandas as pd
from pathlib import Path

# Ubicacion del dataset
ruta = (
    Path(__file__).resolve().parent.parent
    / "data" / "raw" / "solicitudes_smartpay.csv"
)

# Cargar informacion
df = pd.read_csv(ruta)

print("=== EXPLORACION DEL DATASET SMARTPAY ===")

# 1. Dimensiones
print("\n1. DIMENSIONES")
print(f"Registros: {df.shape[0]}")
print(f"Variables: {df.shape[1]}")

# 2. Nombres de las variables
print("\n2. VARIABLES DEL DATASET")
print(df.columns.tolist())

# 3. Valores faltantes
print("\n3. VALORES FALTANTES")
print(df.isnull().sum())

# 4. Registros duplicados
print("\n4. REGISTROS DUPLICADOS")
print(df.duplicated().sum())

# 5. Distribucion del resultado
print("\n5. RESULTADO DEL PROCESAMIENTO")
print(df["resultado_procesamiento"].value_counts())

# 6. Distribucion por operacion
print("\n6. TIPOS DE OPERACION")
print(df["tipo_operacion"].value_counts())

# 7. Motivos de rechazo
print("\n7. MOTIVOS DE RECHAZO")
print(
    df[df["resultado_procesamiento"] == "Rechazado"]
    ["motivo_rechazo"]
    .value_counts()
)

# 8. Primeros registros
print("\n8. MUESTRA DE LOS PRIMEROS 10 REGISTROS")
print(df.head(10).to_string(index=False))

print("\n=== FIN DE LA EXPLORACION ===")


# ============================================================
# 9. GENERACION DE GRAFICAS ESTADISTICAS
# ============================================================

import matplotlib.pyplot as plt

# Crear carpeta para almacenar las graficas
carpeta_graficas = (
    Path(__file__).resolve().parent.parent
    / "reports" / "graficas"
)

carpeta_graficas.mkdir(parents=True, exist_ok=True)


# GRAFICA 1: SOLICITUDES ACEPTADAS Y RECHAZADAS

resultados = df["resultado_procesamiento"].value_counts()

plt.figure(figsize=(8, 5))
resultados.plot(kind="bar")

plt.title("Solicitudes aceptadas y rechazadas")
plt.xlabel("Resultado del procesamiento")
plt.ylabel("Cantidad de solicitudes")
plt.xticks(rotation=0)
plt.tight_layout()

plt.savefig(
    carpeta_graficas / "distribucion_resultados.png"
)
plt.close()


# GRAFICA 2: DISTRIBUCION POR TIPO DE OPERACION

operaciones = df["tipo_operacion"].value_counts()

plt.figure(figsize=(9, 5))
operaciones.plot(kind="bar")

plt.title("Distribucion por tipo de operacion")
plt.xlabel("Tipo de operacion")
plt.ylabel("Cantidad de solicitudes")
plt.xticks(rotation=20, ha="right")
plt.tight_layout()

plt.savefig(
    carpeta_graficas / "distribucion_operaciones.png"
)
plt.close()


# GRAFICA 3: MOTIVOS DE RECHAZO

rechazos = df[
    df["resultado_procesamiento"] == "Rechazado"
]

motivos = rechazos["motivo_rechazo"].value_counts()

plt.figure(figsize=(10, 6))
motivos.sort_values().plot(kind="barh")

plt.title("Principales motivos de rechazo")
plt.xlabel("Cantidad de solicitudes")
plt.ylabel("Motivo de rechazo")
plt.tight_layout()

plt.savefig(
    carpeta_graficas / "motivos_rechazo.png"
)
plt.close()


print("\n=== GRAFICAS GENERADAS ===")
print("1. distribucion_resultados.png")
print("2. distribucion_operaciones.png")
print("3. motivos_rechazo.png")
print(f"Carpeta: {carpeta_graficas}")
