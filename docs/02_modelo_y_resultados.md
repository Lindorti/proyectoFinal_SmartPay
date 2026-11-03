# 02. Modelo de Machine Learning y resultados

## 1. Introducción

El proyecto SmartPay utiliza técnicas de Machine Learning para clasificar solicitudes simuladas de aplicación de pagos de cartera de créditos en dos categorías: Aceptado y Rechazado.

Para este propósito se implementó un modelo de clasificación supervisada basado en un Árbol de Decisión, utilizando Python y la biblioteca scikit-learn.

El objetivo es identificar patrones en las características de las solicitudes y generar una clasificación experimental que permita evaluar el comportamiento del modelo dentro del prototipo académico.

## 2. Selección y justificación del modelo

Se seleccionó el algoritmo Árbol de Decisión (Decision Tree Classifier), porque permite realizar tareas de clasificación y representar las condiciones que intervienen en una predicción mediante una estructura de decisiones.

Las principales razones para elegirlo fueron:

- Es un algoritmo adecuado para problemas de clasificación supervisada.
- Permite trabajar con variables numéricas y categóricas después de su transformación.
- Facilita la interpretación de las condiciones utilizadas para clasificar las solicitudes.
- Permite visualizar gráficamente las decisiones del modelo.
- Es apropiado para un ejercicio académico que busca comprender el funcionamiento de Machine Learning.

El modelo clasifica las solicitudes en dos categorías: Rechazado y Aceptado.

## 3. Configuración del modelo

Para el entrenamiento se utilizó `DecisionTreeClassifier` de la biblioteca scikit-learn.

La configuración implementada fue:

| Parámetro | Valor |
|---|---|
| Algoritmo | Árbol de Decisión |
| Clase de scikit-learn | DecisionTreeClassifier |
| Criterio de división | Gini |
| Profundidad máxima | 8 |
| Mínimo de muestras por hoja | 5 |
| Semilla aleatoria | 42 |

La profundidad máxima y el mínimo de muestras por hoja se establecieron para controlar el crecimiento del árbol y reducir el riesgo de sobreajuste.

## 4. Preparación y división de los datos

El entrenamiento se realizó utilizando el dataset sintético de 2.000 solicitudes generado para SmartPay.

Antes de entrenar el modelo se aplicaron las siguientes actividades:

1. Selección de las variables predictoras y la variable objetivo.
2. Generación de indicadores relacionados con la longitud válida de las cuentas y los créditos.
3. Codificación de las variables categóricas mediante One-Hot Encoding.
4. Conversión de la variable objetivo a valores numéricos.
5. División del conjunto de datos en entrenamiento y prueba.

La variable objetivo se codificó de la siguiente manera:

| Categoría | Codificación |
|---|---:|
| Rechazado | 0 |
| Aceptado | 1 |

La división de los datos se realizó utilizando el 80 % para entrenamiento y el 20 % para prueba, con una semilla aleatoria de 42 y estratificación de las clases.

| Conjunto | Registros | Porcentaje |
|---|---:|---:|
| Entrenamiento | 1.600 | 80 % |
| Prueba | 400 | 20 % |
| **Total** | **2.000** | **100 %** |

La estratificación permite conservar la proporción de las categorías en ambos conjuntos.

## 5. Resultados del entrenamiento

Durante el entrenamiento, el Árbol de Decisión obtuvo una exactitud de 81,81 % sobre los datos de entrenamiento.

La configuración final del modelo presentó una profundidad de 8 niveles y 29 hojas.

Estos resultados muestran que el modelo logró identificar patrones presentes en los datos utilizados para su entrenamiento.

Sin embargo, el resultado obtenido sobre los datos de entrenamiento no es suficiente para determinar su capacidad de generalización. Por esta razón, también se evaluó utilizando el conjunto de prueba.

## 6. Métricas de evaluación

La evaluación se realizó sobre 400 registros que no participaron en el entrenamiento.

Los resultados obtenidos fueron:

| Métrica | Resultado |
|---|---:|
| Accuracy | 81,00 % |
| Precision (Rechazado) | 84,83 % |
| Recall (Rechazado) | 75,50 % |
| F1-score (Rechazado) | 79,89 % |

### Interpretación de las métricas

**Accuracy:** el modelo clasificó correctamente el 81 % del total de solicitudes evaluadas.

**Precision:** de las solicitudes que el modelo clasificó como Rechazado, el 84,83 % realmente pertenecían a esa categoría.

**Recall:** el modelo identificó correctamente el 75,50 % de las solicitudes que realmente pertenecían a la categoría Rechazado.

**F1-score:** obtuvo un valor de 79,89 %, que representa el equilibrio entre Precision y Recall para la clase Rechazado.

Para este ejercicio se considera Rechazado como la clase positiva, debido a la importancia de identificar las solicitudes que incumplen las condiciones simuladas.

## 7. Matriz de confusión

La matriz de confusión obtenida durante la evaluación fue:

| Clase real / Predicción | Rechazado (0) | Aceptado (1) |
|---|---:|---:|
| Rechazado (0) | 151 | 49 |
| Aceptado (1) | 27 | 173 |

La matriz permite identificar los aciertos y errores del modelo.

### Interpretación de los resultados

- **Verdaderos positivos (TP = 151):** solicitudes realmente rechazadas que el modelo clasificó correctamente como Rechazado.
- **Falsos negativos (FN = 49):** solicitudes realmente rechazadas que el modelo clasificó incorrectamente como Aceptado.
- **Falsos positivos (FP = 27):** solicitudes realmente aceptadas que el modelo clasificó incorrectamente como Rechazado.
- **Verdaderos negativos (TN = 173):** solicitudes realmente aceptadas que el modelo clasificó correctamente como Aceptado.

Los falsos negativos requieren especial atención, porque representan solicitudes que incumplían las condiciones simuladas, pero fueron clasificadas como aceptadas.

Por esta razón, el resultado del modelo no debe utilizarse como autorización de una operación financiera.

### Evidencia gráfica

El proyecto incluye las siguientes evidencias generadas durante la evaluación:

- `reports/graficas/matriz_confusion_smartpay.png`
- `reports/graficas/arbol_decision_smartpay.png`

Estas imágenes permiten observar la distribución de los resultados y la estructura de decisiones aprendida por el algoritmo.

## 8. Análisis del desempeño

El modelo obtuvo una exactitud de entrenamiento de 81,81 % y una exactitud de prueba de 81,00 %. La diferencia entre ambos valores es pequeña, lo cual constituye un resultado inicial favorable.

Sin embargo, esta diferencia no permite descartar por completo el sobreajuste ni garantiza que el modelo tenga un comportamiento similar frente a datos diferentes.

El Recall de 75,50 % para la clase Rechazado indica que el modelo no logró identificar todas las solicitudes que realmente incumplían las reglas simuladas.

Los 49 falsos negativos evidencian la necesidad de mejorar la identificación de solicitudes rechazadas y mantener las validaciones de negocio como controles obligatorios.

Además, como los datos fueron generados artificialmente a partir de reglas definidas para el ejercicio, el modelo aprende patrones de un escenario controlado. Por ello, no se puede afirmar que estos resultados representen el comportamiento de solicitudes financieras reales.

## 9. Comparación con un modelo de referencia (Baseline)

Para evaluar si el Árbol de Decisión aporta una mejora frente a una estrategia básica, se implementó un modelo de referencia utilizando `DummyClassifier` de scikit-learn, con la estrategia `most_frequent`.

Este algoritmo predice siempre la clase más frecuente observada durante el entrenamiento, sin aprender relaciones entre las variables predictoras.

La comparación se realizó utilizando los mismos conjuntos de entrenamiento y prueba: 1.600 registros para entrenamiento y 400 para evaluación.

### Resultados comparativos

| Métrica | Árbol de Decisión | Baseline |
|---|---:|---:|
| Accuracy | 81,00 % | 50,00 % |
| Precision (Rechazado) | 84,83 % | 50,00 % |
| Recall (Rechazado) | 75,50 % | 100,00 % |
| F1-score (Rechazado) | 79,89 % | 66,67 % |

### Interpretación

El Árbol de Decisión obtuvo un Accuracy de 81 %, superior al 50 % alcanzado por el baseline. Esto representa una mejora de 31 puntos porcentuales.

El baseline obtuvo un Recall del 100 % para la clase Rechazado porque clasificó todas las solicitudes como rechazadas. Sin embargo, también clasificó incorrectamente las 200 solicitudes que realmente eran aceptadas.

Por su parte, el Árbol de Decisión logró identificar ambas categorías, obteniendo mejores resultados de precisión y F1-score para la clase Rechazado.

La comparación evidencia que el Árbol de Decisión aprende patrones presentes en el dataset sintético y ofrece una clasificación más equilibrada que la estrategia básica de referencia.

### Matriz de confusión del Baseline

| Clase real / Predicción | Rechazado (0) | Aceptado (1) |
|---|---:|---:|
| Rechazado (0) | 200 | 0 |
| Aceptado (1) | 200 | 0 |

El resultado muestra que el baseline no identifica solicitudes aceptadas, por lo que no resulta suficiente para el propósito de clasificación de SmartPay.

### Evidencias de la comparación

Los resultados de la comparación se almacenan en:

- `reports/metricas/comparacion_modelos.csv`
- `reports/graficas/matriz_confusion_baseline.png`

## 10. Criterios de aceptación académicos

Para evaluar el resultado del ejercicio se establecieron los siguientes criterios:

1. El Árbol de Decisión debe superar el Accuracy del modelo baseline utilizando la misma partición de prueba.
2. El modelo debe alcanzar un Recall mínimo del 75 % para la clase Rechazado, como umbral académico de evaluación del prototipo.
3. Se deben presentar las métricas Accuracy, Precision, Recall y F1-score.
4. Se debe incluir e interpretar la matriz de confusión.
5. Se deben identificar los falsos negativos y falsos positivos.
6. Las reglas de negocio deben mantenerse independientes de la predicción del modelo.

El Árbol de Decisión cumplió los dos criterios cuantitativos establecidos: obtuvo 81 % de Accuracy frente al 50 % del baseline y 75,50 % de Recall para la clase Rechazado.

También se presentaron las métricas de evaluación, la matriz de confusión y la interpretación de los errores.

Estos criterios son académicos y experimentales. No representan umbrales de autorización ni de seguridad para operaciones financieras reales.

## 11. Limitaciones del modelo

El modelo presenta las siguientes limitaciones:

- Fue entrenado con datos sintéticos y no con información real de operaciones financieras.
- Las etiquetas fueron construidas a partir de reglas simuladas.
- La distribución de las clases fue establecida artificialmente.
- Puede cometer errores de clasificación, especialmente falsos negativos.
- La comparación realizada utiliza un baseline sencillo y no demuestra superioridad frente a todos los algoritmos posibles.
- Su desempeño debe evaluarse con nuevos escenarios y metodologías adicionales.
- No ha sido validado en un entorno bancario real.

Por lo anterior, sus resultados tienen un alcance exclusivamente académico y experimental.

## 12. Conclusiones

La implementación del Árbol de Decisión permitió desarrollar un modelo de clasificación supervisada para las solicitudes simuladas del proyecto SmartPay.

El modelo obtuvo una exactitud del 81 % en los datos de prueba, con una precisión del 84,83 % y un Recall del 75,50 % para la categoría Rechazado.

La comparación con el modelo baseline permitió comprobar que el Árbol de Decisión obtuvo mejores resultados generales de clasificación que una estrategia que predice siempre la clase más frecuente.

La matriz de confusión permitió identificar 151 clasificaciones correctas de solicitudes rechazadas y 49 falsos negativos, lo que demuestra que todavía existen oportunidades de mejora en la identificación de solicitudes que incumplen las condiciones simuladas.

El ejercicio permitió comprender la importancia de preparar los datos, seleccionar variables predictoras, entrenar un modelo y evaluar su desempeño mediante diferentes métricas.

## 13. Recomendaciones

1. Continuar evaluando el modelo con nuevos escenarios sintéticos.
2. Fortalecer las pruebas de validación de las reglas de negocio.
3. Analizar los falsos negativos y los falsos positivos para identificar oportunidades de mejora.
4. Mantener las validaciones determinísticas como controles obligatorios e independientes del modelo.
5. Realizar futuras pruebas con datos representativos y autorizados antes de considerar cualquier aplicación en un entorno real.
6. Mantener supervisión humana sobre cualquier resultado generado por el modelo.
7. Evaluar otros algoritmos de clasificación en futuras etapas académicas, utilizando las mismas condiciones de evaluación.

## 14. Consideración de uso responsable

SmartPay es un prototipo académico que utiliza datos sintéticos. El modelo de Machine Learning tiene una finalidad experimental y no autoriza pagos, no ejecuta débitos ni modifica cuentas o créditos.

Las reglas de negocio determinísticas son las responsables de verificar las condiciones de las solicitudes simuladas. Cualquier implementación futura requerirá pruebas adicionales, controles de seguridad, evaluación independiente y aprobación de las áreas responsables.