# 08. Revisión de requisitos y estado final del proyecto SmartPay

## 1. Requisitos de Machine Learning

| Requisito | Estado | Evidencia |
|---|---|---|
| Seleccionar un modelo de Machine Learning | Realizado | Árbol de Decisión. |
| Justificar el modelo seleccionado | Documentado | `02_modelo_y_resultados.md`. |
| Describir el dataset | Documentado | `01_dataset.md`. |
| Presentar una muestra de datos | Realizado | Tabla de cuatro registros sintéticos tomada del CSV, incluida en `README.md` y `01_dataset.md`. |
| Explicar variables y variable objetivo | Documentado | Diccionario de datos y preprocesamiento. |
| Calcular métricas de evaluación | Realizado | Accuracy, Precision, Recall y F1-score. |
| Presentar e interpretar resultados | Documentado | `02_modelo_y_resultados.md`. |
| Incluir matriz de confusión | Realizado | Matriz con valores 151, 49, 27 y 173. |
| Explicar TP, FP, TN y FN | Documentado | Interpretación de la clase positiva Rechazado. |
| Realizar análisis ético y de sesgos | Documentado | `06_analisis_etico.md`. |
| Evaluar privacidad e impacto social | Documentado | `06_analisis_etico.md`. |
| Presentar conclusiones y recomendaciones | Documentado | `02_modelo_y_resultados.md`. |
| Comparar el modelo con un baseline | Realizado | `comparacion_baseline.py` y resultados documentados. |
| Establecer criterios de aceptación | Documentado | `02_modelo_y_resultados.md`. |

## 2. Requisitos de arquitectura y repositorio

| Requisito | Estado | Evidencia |
|---|---|---|
| README con problema, datos, solución y validación | Realizado | `README.md`. |
| Definir alcance y funcionalidades fuera del alcance | Documentado | `README.md` y `03_arquitectura_c4.md`. |
| Diagrama C4 de contexto | Realizado | `03_arquitectura_c4.md`. |
| Decisiones de arquitectura (ADR) | Realizado | `04_adr.md`. |
| Identificar riesgos técnicos y mitigaciones | Realizado | `05_riesgos.md`. |
| Glosario y referencias | Realizado | `07_glosario_referencias.md`, con documentación oficial de las herramientas y fuente propia del dataset. |
| Mantener una rama individual de desarrollo | Realizado | `dev_jcol_10`. |
| Consolidar el desarrollo en `develop` | Realizado | Pull Requests #1 y #2 integrados. |
| Publicar el repositorio con el nombre establecido | Realizado | `proyectoFinal_SmartPay`. |

## 3. Pruebas automatizadas de validación

Se implementaron pruebas automatizadas utilizando la biblioteca `unittest` de Python para verificar el funcionamiento de las reglas de negocio de SmartPay.

Se ejecutaron 24 pruebas relacionadas con:

- Longitud de los números de cuenta y crédito.
- Identificadores con caracteres no numéricos.
- Campos obligatorios completos e incompletos.
- Valores de pago positivos, negativos, cero y no numéricos.
- Validaciones de pago de cuota.
- Validaciones de abono a capital.
- Validaciones de abono a intereses.
- Validaciones de pago total.
- Tipos de operación no reconocidos.

**Resultado de ejecución:**

| Indicador | Resultado |
|---|---|
| Herramienta utilizada | unittest |
| Pruebas ejecutadas | 24 |
| Pruebas exitosas | 24 |
| Pruebas fallidas | 0 |
| Estado final | OK |

**Archivo de pruebas:** `src/test_validaciones.py`.

**Módulo evaluado:** `src/validaciones.py`.

**Comando de ejecución:**

```bash
python src/test_validaciones.py
```

Las 24 pruebas finalizaron correctamente. Esto permite verificar el comportamiento de las funciones de validación frente a los escenarios definidos.

## 4. Resultados de la comparación con Baseline

Para evaluar el desempeño del Árbol de Decisión se implementó un modelo de referencia mediante `DummyClassifier` de scikit-learn, utilizando la estrategia `most_frequent`.

La comparación se realizó con los mismos conjuntos de entrenamiento y prueba.

| Métrica | Árbol de Decisión | Baseline |
|---|---:|---:|
| Accuracy | 81,00 % | 50,00 % |
| Precision (Rechazado) | 84,83 % | 50,00 % |
| Recall (Rechazado) | 75,50 % | 100,00 % |
| F1-score (Rechazado) | 79,89 % | 66,67 % |

El Árbol de Decisión obtuvo mejores resultados generales de clasificación que el modelo de referencia. El baseline clasificó todas las solicitudes como rechazadas, incluyendo las que realmente eran aceptadas.

**Archivos de evidencia:**

- `src/comparacion_baseline.py`.
- `reports/metricas/comparacion_modelos.csv`.
- `reports/graficas/matriz_confusion_baseline.png`.

## 5. Aplicación y validación funcional

Se implementó una interfaz web utilizando Streamlit para integrar el registro de solicitudes, las validaciones de negocio y la clasificación experimental mediante el Árbol de Decisión.

Durante las pruebas funcionales se evaluaron dos escenarios con información ficticia.

### Prueba 1. Solicitud válida

Se ingresaron datos de prueba con número de cuenta y crédito de 11 dígitos, cuenta activa, crédito vigente, correspondencia correcta entre crédito y NIT, saldo suficiente y valor de pago igual a la cuota pendiente.

**Resultado obtenido:**

- Las validaciones de negocio fueron superadas.
- El modelo realizó la clasificación experimental.
- La predicción obtenida fue ACEPTADO.

### Prueba 2. Solicitud inválida

Se modificó el número de cuenta para que tuviera 10 dígitos y se ingresó un valor de pago diferente al de la cuota pendiente.

**Resultado obtenido:**

- La aplicación detectó que la cuenta no cumplía la longitud requerida.
- Identificó que el valor del pago no coincidía con la cuota pendiente.
- Impidió ejecutar la clasificación del modelo debido a los errores encontrados.

Las pruebas permitieron verificar la integración del formulario, las reglas de negocio y la clasificación experimental. Se comprobó que las solicitudes que presentan inconsistencias no continúan hacia la predicción del modelo.

## 6. Revisión metodológica y técnica

El modelo Árbol de Decisión obtuvo una exactitud de entrenamiento de 81,81 % y una exactitud de prueba de 81,00 %.

El dataset utilizado contiene registros sintéticos y sus etiquetas fueron construidas a partir de reglas simuladas. Por esta razón, los resultados permiten evaluar el comportamiento experimental del algoritmo, pero no demuestran que pueda clasificar correctamente solicitudes reales de una entidad bancaria.

También se debe prestar especial atención a los falsos negativos: solicitudes que realmente pertenecen a la clase Rechazado, pero que el modelo clasifica como Aceptado. En la evaluación se identificaron 49 casos de este tipo.

La predicción del modelo no debe autorizar pagos ni reemplazar las validaciones determinísticas del proceso.

Para reproducir la aplicación desde una descarga nueva del repositorio se deben regenerar los datos y el modelo, debido a que los archivos generados están excluidos del control de versiones mediante `.gitignore`.

## 7. Control de ramas y repositorio

El repositorio del proyecto es:

https://github.com/Lindorti/proyectoFinal_SmartPay

La rama individual de desarrollo es:

`dev_jcol_10`

La consolidación del proyecto en la rama `develop` se realizó mediante los siguientes Pull Requests:

- Pull Request #1: Consolidación del desarrollo individual de SmartPay.
- Pull Request #2: Actualización del README y documentación final de SmartPay.

Ambos Pull Requests fueron integrados en `develop`.

La rama individual se conserva como evidencia del desarrollo y del historial de commits. La rama `develop` contiene la versión consolidada del proyecto.

No se requiere eliminar las ramas anteriores, ya que forman parte del historial de trabajo y permiten conservar la trazabilidad del desarrollo.

## 8. Estado general del proyecto

SmartPay cuenta con una estructura organizada para la generación de datos sintéticos, validaciones de negocio, entrenamiento de un Árbol de Decisión y evaluación del modelo mediante métricas y matriz de confusión.

También se implementó una aplicación local con Streamlit, una comparación con un modelo baseline y 24 pruebas automatizadas para verificar las funciones principales de validación.

La documentación técnica y académica se encuentra distribuida en ocho archivos Markdown, además del README principal.

El desarrollo individual fue consolidado en la rama `develop` mediante Pull Requests, conservando el historial de cambios en GitHub.

## 9. Consideraciones finales

Los resultados obtenidos corresponden a un ejercicio académico realizado con datos sintéticos y no deben interpretarse como una validación de desempeño en operaciones financieras reales.

El prototipo mantiene las reglas de negocio como controles principales y utiliza el modelo de Machine Learning únicamente con fines experimentales.

Cualquier implementación futura requeriría datos representativos y autorizados, controles de seguridad, pruebas independientes, auditoría, supervisión humana y aprobación de las áreas responsables.