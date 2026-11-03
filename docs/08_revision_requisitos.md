# 08. Revisión de requisitos y estado del proyecto SmartPay

## 1. Requisitos de Machine Learning

| Requisito | Estado | Evidencia / acción |
|---|---|---|
| Seleccionar un modelo sencillo | Realizado | Árbol de Decisión. |
| Justificar el modelo | Documentado | `02_modelo_y_resultados.md`. |
| Describir el dataset | Documentado | `01_dataset.md`. |
| Mostrar una tabla pequeña de datos | Realizado parcialmente | Se dispone de una muestra ficticia explicativa. Incorporar una muestra literal del CSV si el docente lo exige. |
| Explicar variables y objetivo | Documentado | Diccionario de datos y sección de preprocesamiento. |
| Calcular métricas | Realizado | Accuracy, Precision, Recall y F1-score. |
| Presentar e interpretar resultados | Documentado | `02_modelo_y_resultados.md`. |
| Incluir matriz de confusión | Realizado | Matriz con valores 151, 49, 27 y 173. |
| Explicar TP, FP, TN y FN | Documentado | Clase positiva definida como Rechazado. |
| Realizar análisis ético y de sesgos | Documentado | `06_analisis_etico.md`. |
| Evaluar equidad, privacidad e impacto social | Documentado | `06_analisis_etico.md`. |
| Presentar conclusiones técnicas y recomendaciones | Documentado | `02_modelo_y_resultados.md`. |
| Comparar el modelo con un baseline | Realizado | `comparacion_baseline.py` y `comparacion_modelos.csv`. |
| Establecer criterios de aceptación | Documentado | `02_modelo_y_resultados.md`. |

## 2. Requisitos de arquitectura y repositorio

| Requisito | Estado | Evidencia / acción |
|---|---|---|
| README que explique problema, datos, solución y validación | Actualizado | `README.md`. |
| Definir qué hará y qué no hará el sistema | Documentado | `README.md` y `03_arquitectura_c4.md`. |
| Diagrama C4 de contexto | Documentado | Diagrama Mermaid en `03_arquitectura_c4.md`. |
| Decisiones de arquitectura (ADR) | Documentado | `04_adr.md`. |
| Entre 3 y 5 riesgos técnicos y mitigaciones | Documentado | Cinco riesgos en `05_riesgos.md`. |
| Glosario y referencias | Documentado | `07_glosario_referencias.md`. |
| Commits en rama individual | En desarrollo | Rama individual publicada: `dev_jcol_10`. Continuar realizando los commits exclusivamente en esta rama. |
| Consolidar el proyecto en `develop` | Pendiente | Crear Pull Request desde `dev_jcol_10` hacia `develop` y verificar su integración. |
| Nombre del repositorio | Realizado | `proyectoFinal_SmartPay`. |

## 3. Pruebas automatizadas de validación

Se implementaron pruebas automatizadas utilizando la biblioteca `unittest` de Python para verificar el funcionamiento de las reglas de negocio de SmartPay.

Se ejecutaron 24 pruebas que contemplaron:

- Números de cuenta con longitudes de 10, 11 y 12 dígitos.
- Números de crédito con longitudes de 10, 11 y 12 dígitos.
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

Las 24 pruebas finalizaron correctamente, sin errores ni fallos. Esto permite verificar el comportamiento de las funciones individuales de validación frente a los escenarios definidos.

## 4. Resultados de la comparación con Baseline

Para evaluar el desempeño del Árbol de Decisión se implementó un modelo de referencia utilizando `DummyClassifier` de scikit-learn, con la estrategia `most_frequent`.

La comparación se realizó con los mismos conjuntos de entrenamiento y prueba.

| Métrica | Árbol de Decisión | Baseline |
|---|---:|---:|
| Accuracy | 81,00 % | 50,00 % |
| Precision (Rechazado) | 84,83 % | 50,00 % |
| Recall (Rechazado) | 75,50 % | 100,00 % |
| F1-score (Rechazado) | 79,89 % | 66,67 % |

El Árbol de Decisión obtuvo mejores resultados generales de clasificación que el modelo de referencia. El baseline alcanzó un Recall del 100 % para la clase Rechazado porque clasificó todas las solicitudes como rechazadas, incluyendo las que realmente eran aceptadas.

**Archivos de evidencia:**

- `src/comparacion_baseline.py`.
- `reports/metricas/comparacion_modelos.csv`.
- `reports/graficas/matriz_confusion_baseline.png`.

## 5. Pendientes técnicos prioritarios

Aunque se han completado varios componentes, todavía se deben realizar las siguientes verificaciones antes de considerar finalizado el proyecto:

1. **Validación del generador de datos:** revisar que las etiquetas generadas correspondan con las condiciones simuladas y que no existan inconsistencias o fuga de información.
2. **Aplicación:** revisar `src/aplicacion.py` y verificar su funcionamiento. No presentar una interfaz como terminada hasta que haya sido implementada y probada.
3. **Reproducibilidad:** verificar que `requirements.txt` incluya todas las dependencias necesarias y que el proyecto pueda ejecutarse desde una instalación limpia.
4. **Preprocesamiento:** revisar que las transformaciones y codificaciones se ajusten correctamente y que no se produzca fuga de información entre entrenamiento y prueba.
5. **Evidencias:** conservar los gráficos originales generados por los scripts y verificar que las imágenes incluidas en el repositorio sean legibles y correspondan a los resultados reportados.
6. **Integración en GitHub:** publicar los últimos cambios y consolidar el proyecto en `develop` mediante un Pull Request.

## 6. Revisión metodológica

El modelo Árbol de Decisión obtuvo una exactitud de entrenamiento de 81,81 % y una exactitud de prueba de 81,00 %.

La diferencia entre ambos resultados es pequeña, pero no es suficiente por sí sola para descartar sobreajuste.

El dataset utilizado contiene registros sintéticos y sus etiquetas se construyeron a partir de reglas simuladas. Por esta razón, los resultados permiten evaluar el comportamiento experimental del algoritmo, pero no demuestran que pueda clasificar correctamente solicitudes reales de una entidad bancaria.

La comparación con el baseline mostró que el Árbol de Decisión obtuvo un Accuracy de 81 %, frente al 50 % del modelo de referencia.

También se debe prestar especial atención a los falsos negativos: solicitudes que realmente pertenecen a la clase Rechazado, pero que el modelo clasifica como Aceptado. En la evaluación se identificaron 49 casos de este tipo.

La predicción del modelo no debe autorizar pagos ni reemplazar las validaciones determinísticas del proceso.

## 7. Control de ramas y repositorio

El repositorio del proyecto es:

https://github.com/Lindorti/proyectoFinal_SmartPay

La rama individual de trabajo es:

`dev_jcol_10`

Esta rama fue publicada correctamente en GitHub y quedó configurada para realizar seguimiento a `origin/dev_jcol_10`.

El procedimiento pendiente es:

1. Continuar realizando los cambios y commits exclusivamente en `dev_jcol_10`.
2. Verificar que todos los archivos requeridos estén incluidos y actualizados.
3. Publicar los últimos cambios en GitHub.
4. Crear un Pull Request desde `dev_jcol_10` hacia `develop`.
5. Verificar que los cambios queden integrados correctamente en `develop`.
6. Conservar el historial de commits como evidencia del desarrollo individual.

No eliminar las ramas anteriores hasta verificar que el historial y los cambios requeridos estén correctamente consolidados.

## 8. Estado general del proyecto

SmartPay cuenta con una estructura organizada de desarrollo, generación de datos sintéticos, validaciones de negocio, entrenamiento de un Árbol de Decisión y evaluación del modelo mediante métricas y matriz de confusión.

Durante el desarrollo también se implementó una comparación con un modelo baseline y se construyeron 24 pruebas automatizadas para verificar las funciones principales de validación.

La documentación técnica y académica se encuentra distribuida en ocho archivos Markdown, además del README principal.

Los siguientes pasos se concentran en revisar la aplicación, verificar la reproducibilidad, validar el generador de datos y completar la consolidación del proyecto en la rama `develop`, de acuerdo con las instrucciones académicas.

## 9. Consideraciones finales

Los resultados obtenidos corresponden a un ejercicio académico realizado con datos sintéticos y no deben interpretarse como una validación de desempeño en operaciones financieras reales.

El prototipo mantiene las reglas de negocio como controles principales y utiliza el modelo de Machine Learning únicamente con fines experimentales.

Cualquier implementación futura requeriría datos representativos y autorizados, controles de seguridad, pruebas independientes, auditoría, supervisión humana y aprobación de las áreas responsables.

## 10. Pruebas funcionales de la aplicación SmartPay

Se implementó una interfaz web utilizando Streamlit para integrar el registro de solicitudes, las validaciones de negocio y la clasificación experimental mediante el Árbol de Decisión.

Durante las pruebas funcionales se evaluaron dos escenarios con información completamente ficticia.

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

### Conclusión de las pruebas funcionales

Los dos escenarios ejecutados demostraron que la aplicación integra correctamente el formulario, las reglas de negocio y el modelo de clasificación experimental.

Se comprobó que una solicitud que supera las validaciones puede continuar hacia la clasificación, mientras que una solicitud con inconsistencias queda detenida antes de utilizar el modelo.

Las pruebas se realizaron exclusivamente con datos sintéticos. Estos resultados corresponden a una verificación funcional inicial y no representan una validación en sistemas financieros reales.