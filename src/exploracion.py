
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
