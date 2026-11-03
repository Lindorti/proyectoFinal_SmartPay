# 05. Riesgos técnicos y estrategias de mitigación

## 1. Introducción

El desarrollo del proyecto SmartPay implica diferentes riesgos técnicos relacionados con la calidad de los datos, el entrenamiento del modelo de Machine Learning, la seguridad de la información y la confiabilidad de los resultados.

Aunque SmartPay es un prototipo académico que utiliza datos sintéticos, es importante identificar estos riesgos y establecer acciones preventivas para reducir su impacto.

Este documento presenta cinco riesgos principales identificados durante el desarrollo del proyecto, junto con sus posibles consecuencias y estrategias de mitigación.

## 2. Identificación y análisis de riesgos

### Riesgo 1. Calidad y representatividad insuficiente de los datos

**Descripción:**

El modelo se entrena con un dataset sintético de 2.000 solicitudes generadas mediante reglas previamente definidas. Aunque estos datos permiten desarrollar el ejercicio, no representan necesariamente las condiciones y variaciones de un proceso financiero real.

**Posibles consecuencias:**

- El modelo puede aprender patrones demasiado específicos del generador.
- Los resultados pueden no generalizarse a otros escenarios.
- La distribución de los datos puede diferir de la realidad operativa.

**Estrategias de mitigación:**

- Documentar claramente el origen sintético de los datos.
- Verificar la distribución de las variables y las categorías.
- Generar escenarios de prueba con diferentes condiciones.
- Comparar los resultados con un modelo de referencia.
- No utilizar los resultados como evidencia de desempeño en operaciones reales.

**Prioridad:** Alta.

### Riesgo 2. Fuga de información (Data Leakage)

**Descripción:**

La fuga de información puede ocurrir cuando el modelo utiliza variables que contienen información relacionada directamente con el resultado que intenta predecir o cuando se incorporan datos del conjunto de prueba durante el entrenamiento.

**Posibles consecuencias:**

- Métricas de evaluación artificialmente elevadas.
- Resultados que no representan la capacidad real de generalización.
- Interpretaciones incorrectas sobre el desempeño del modelo.

**Estrategias de mitigación:**

- Excluir la variable objetivo y los campos que revelen directamente el resultado.
- Mantener `motivo_rechazo` fuera de las variables predictoras.
- Separar los datos de entrenamiento y prueba antes de ajustar el modelo.
- Verificar que las transformaciones se ajusten únicamente con los datos de entrenamiento.
- Revisar periódicamente el proceso de preprocesamiento.

**Prioridad:** Alta.

### Riesgo 3. Sobreajuste del modelo

**Descripción:**

El sobreajuste ocurre cuando el Árbol de Decisión aprende demasiado los patrones específicos de los datos de entrenamiento y pierde capacidad para clasificar correctamente datos diferentes.

**Posibles consecuencias:**

- Diferencias importantes entre los resultados de entrenamiento y prueba.
- Menor capacidad de generalización.
- Clasificaciones incorrectas ante escenarios no vistos.

**Estrategias de mitigación:**

- Limitar la profundidad del árbol.
- Establecer un mínimo de muestras por hoja.
- Comparar las métricas de entrenamiento y prueba.
- Implementar un modelo baseline.
- Evaluar el modelo con nuevos escenarios sintéticos y, posteriormente, con datos representativos autorizados si se desarrolla una etapa futura.

**Prioridad:** Media-alta.

### Riesgo 4. Sesgos y errores de clasificación

**Descripción:**

El modelo puede reproducir los supuestos y desequilibrios presentes en el dataset sintético. También puede cometer falsos positivos y falsos negativos al clasificar las solicitudes.

En la evaluación realizada, se identificaron 49 falsos negativos, correspondientes a solicitudes realmente rechazadas que fueron clasificadas como aceptadas.

**Posibles consecuencias:**

- Clasificación incorrecta de solicitudes.
- Falsa confianza en las predicciones.
- Posibles decisiones equivocadas si se utilizara el modelo sin controles adicionales.

**Estrategias de mitigación:**

- Analizar la matriz de confusión y las métricas por categoría.
- Prestar especial atención al Recall de la clase Rechazado.
- Mantener las reglas de negocio como controles obligatorios.
- Evitar que la predicción del modelo autorice operaciones financieras.
- Incorporar revisión humana en cualquier escenario futuro de aplicación.

**Prioridad:** Alta.

### Riesgo 5. Fallas de reproducibilidad y control de versiones

**Descripción:**

El proyecto puede presentar dificultades para reproducir los resultados si no se mantienen organizados los scripts, las dependencias, los archivos de datos, los modelos y las versiones del código.

**Posibles consecuencias:**

- Diferencias entre resultados de ejecuciones.
- Pérdida de cambios realizados.
- Dificultad para identificar el origen de errores.
- Problemas al ejecutar el proyecto en otro equipo.

**Estrategias de mitigación:**

- Mantener actualizado `requirements.txt`.
- Utilizar semillas aleatorias para reproducir los experimentos.
- Organizar los archivos por responsabilidades.
- Utilizar Git y GitHub para conservar el historial de cambios.
- Realizar commits en la rama individual `dev_jcol_10`.
- Consolidar los cambios en `develop` mediante un Pull Request.
- Documentar los pasos de instalación y ejecución en el README.

**Prioridad:** Media.

## 3. Resumen de riesgos

| Riesgo | Probabilidad estimada | Impacto | Prioridad |
|---|---|---|---|
| Calidad y representatividad insuficiente de los datos | Alta | Alto | Alta |
| Fuga de información | Media | Alto | Alta |
| Sobreajuste del modelo | Media | Alto | Media-alta |
| Sesgos y errores de clasificación | Alta | Alto | Alta |
| Fallas de reproducibilidad y control de versiones | Media | Medio | Media |

Las probabilidades corresponden a una valoración cualitativa del equipo de desarrollo para este prototipo académico y no a una medición estadística.

## 4. Seguimiento y control

Para reducir los riesgos identificados se proponen las siguientes actividades:

1. Revisar la calidad y consistencia del dataset antes de cada entrenamiento.
2. Verificar que las variables predictoras no incluyan información que revele directamente la variable objetivo.
3. Comparar los resultados del modelo con el baseline.
4. Analizar los falsos negativos y falsos positivos después de cada evaluación.
5. Mantener actualizada la documentación y el historial de versiones del proyecto.

## 5. Conclusión

La identificación de riesgos permite reconocer las principales limitaciones técnicas de SmartPay y establecer medidas para mejorar la confiabilidad del prototipo.

Los riesgos más relevantes están relacionados con la naturaleza sintética de los datos, la posible fuga de información y los errores de clasificación del modelo.

La aplicación de las medidas de mitigación propuestas contribuye a fortalecer el desarrollo académico, mantener la trazabilidad de los cambios y promover un uso responsable de las técnicas de Machine Learning.

SmartPay no debe utilizarse en un entorno financiero productivo sin una evaluación adicional, datos representativos autorizados, controles de seguridad y supervisión de las áreas responsables.